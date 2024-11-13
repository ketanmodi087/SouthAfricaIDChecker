from django.db import models

class SAIDRecord(models.Model):
    """
    A model representing a South African ID record.

    Attributes:
        id_number (str): The unique South African ID number associated with the record.
        date_of_birth (date): The date of birth derived from the ID number.
        gender (str): The gender of the individual associated with the ID.
        citizenship_status (str): The citizenship status of the individual (e.g., citizen, resident).
        search_count (int): The number of times this record has been searched. Defaults to 0.
    """
    id_number = models.CharField(max_length=15, unique=True)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=16)
    citizenship_status = models.CharField(max_length=20)
    search_count = models.IntegerField(default=0)

    def __str__(self):
        """
        Returns a string representation of the SAIDRecord instance.

        Returns:
            str: The ID number of the record.
        """
        return self.id_number


class PublicHoliday(models.Model):
    """
    A model representing a public holiday associated with an SA ID record.

    Attributes:
        id_record (ForeignKey): A foreign key linking to an SAIDRecord instance.
        holiday_name (str): The name of the public holiday.
        description (str): A text description of the holiday.
        date (date): The date of the public holiday.
        holiday_type (str): The type of the holiday (e.g., national holiday, religious holiday).
    """
    id_record = models.ForeignKey(SAIDRecord, on_delete=models.CASCADE)
    holiday_name = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateField()
    holiday_type = models.CharField(max_length=50)
