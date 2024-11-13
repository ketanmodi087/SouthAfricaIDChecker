from django import forms

class SAIDForm(forms.Form):
    """
    A form for validating and handling input for a South African ID number.

    This form includes a single input field for a 13-digit South African ID number.
    It validates that the provided ID number is exactly 13 digits long and consists 
    only of numerical characters.

    Fields:
        id_number (CharField): A required character field with a max length of 13,
        displayed using a text input widget with a placeholder.

    Methods:
        clean_id_number(): Custom validation logic for the `id_number` field to ensure 
        the input is exactly 13 digits and contains only numeric characters. Raises 
        a ValidationError if the input is invalid.
    """
    id_number = forms.CharField(
        max_length=13,
        required=True,
        widget=forms.TextInput(attrs={"placeholder": "Enter 13-digit SA ID Number"}),
    )

    def clean_id_number(self):
        """
        Validates that the `id_number` field contains exactly 13 digits.

        Raises:
            forms.ValidationError: If the input is not 13 digits long or contains 
            non-numeric characters.

        Returns:
            str: The cleaned `id_number` value if valid.
        """
        id_number = self.cleaned_data.get("id_number")
        if len(id_number) != 13 or not id_number.isdigit():
            raise forms.ValidationError("Please enter a valid 13-digit SA ID number.")
        return id_number
