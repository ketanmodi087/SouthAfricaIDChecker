from datetime import datetime

def validate_sa_id_number(id_number):
    """
    Validates a South African ID number by checking its length, format, and date of birth.

    This function verifies that the provided ID number is exactly 13 digits long and
    contains only numeric characters. Additionally, it checks if the first six digits 
    represent a valid date of birth in the 'yyMMdd' format.

    Args:
        id_number (str): The South African ID number to be validated.

    Returns:
        tuple: A tuple containing a boolean and a string message. 
               The boolean indicates whether the ID number is valid (True) or not (False).
               The string provides a message describing the validation result.
               Example: (False, "Invalid SA ID Number format") or (True, "Valid ID Number")
    """
    if len(id_number) != 13 or not id_number.isdigit():
        return False, "Invalid SA ID Number format"

    birth_date = id_number[:6]
    try:
        datetime.strptime(birth_date, "%y%m%d")
    except ValueError:
        return False, "Invalid Date of Birth in ID Number"

    return True, "Valid ID Number"
