from datetime import datetime
import requests
from dateutil import parser
from django.conf import settings
from django.db import transaction
from django.shortcuts import redirect
from django.views.generic import DetailView, FormView
from idvault.forms import SAIDForm
from .helpers import validate_sa_id_number
from .models import PublicHoliday, SAIDRecord


# FormView to handle form submission, validate SA ID number, and create/update the record
class SAIDFormView(FormView):
    template_name = "id_input.html"
    form_class = SAIDForm

    @transaction.atomic
    def form_valid(self, form):
        """
        Handles the form submission when the form is valid. This method validates
        the SA ID number, extracts information from it (such as birth date, gender, 
        and citizenship), stores or updates the record in the database, and fetches 
        relevant public holiday data if it's a new record.
        """
        id_number = form.cleaned_data["id_number"]
        is_valid, message = validate_sa_id_number(id_number)

        # If the ID is invalid, return form_invalid
        if not is_valid:
            return self.form_invalid(form)

        # Decode ID Number (extract birth date, gender, citizenship)
        birth_date = datetime.strptime(id_number[:6], "%y%m%d").date()  # Extract birth date
        gender = "Male" if int(id_number[6]) < 5 else "Female"
        citizenship = "SA Citizen" if int(id_number[10]) == 0 else "Permanent Resident"

        # Store or update SAIDRecord
        record, created = SAIDRecord.objects.get_or_create(
            id_number=id_number,
            defaults={
                "date_of_birth": birth_date,
                "gender": gender,
                "citizenship_status": citizenship,
            },
        )

        # Fetch and store public holidays if it's a new record
        if created:
            API_KEY = settings.CALENDARIFIC_API_KEY
            url = f"https://calendarific.com/api/v2/holidays?api_key={API_KEY}&country=ZA&year={str(record.date_of_birth.year)}"
            response = requests.get(url)

            if response.status_code == 200:
                holidays = response.json().get("response", {}).get("holidays", [])

                for holiday in holidays:
                    # Parse the date of the holiday
                    if "T" in holiday.get("date", {}).get("iso", ""):  # ISO 8601 format with time
                        date = parser.parse(holiday.get("date", {}).get("iso", "")).date()
                    else:  # Simple date format
                        date = datetime.strptime(holiday.get("date", {}).get("iso", ""), "%Y-%m-%d").date()

                    # If the holiday matches the birth date, store it
                    if date == record.date_of_birth:
                        PublicHoliday.objects.get_or_create(
                            id_record=record,
                            holiday_name=holiday.get("name", ""),
                            description=holiday.get("description", ""),
                            date=date,
                            holiday_type=holiday.get("type", ""),
                        )
            else:
                return redirect("sa-id-result", pk=record.pk)

        # If the record already exists, increment the search count
        if not created:
            record.search_count += 1
            record.save()

        return redirect("sa-id-result", pk=record.pk)

    def form_invalid(self, form):
        """
        Handles the case where the form submission is invalid.
        Returns the form with an error message indicating the ID number is invalid.
        """
        return self.render_to_response({"form": form, "error": "Invalid ID number."})


# DetailView to show the result of the SA ID validation and related public holidays
class SAIDResultView(DetailView):
    model = SAIDRecord
    template_name = "id_results.html"
    context_object_name = "record"

    def get_context_data(self, **kwargs):
        """
        Adds the public holidays associated with the SA ID record to the context data.
        """
        context = super().get_context_data(**kwargs)
        record = self.get_object()
        holidays = PublicHoliday.objects.filter(id_record=record)
        context["holidays"] = holidays
        return context
