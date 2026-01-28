def get_valid_choice(valid_choices, prompt="Select an option: ", error_msg="Invalid choice. Please try again."):
    valid_choices = {str(choice) for choice in valid_choices} # Ensure all choices are strings

    while True:
        choice = input(prompt).strip()
        if choice in valid_choices:
            return choice
        print(error_msg)

def validate_fields(input_fields, valid_fields):
    """
    Validates that all input fields are in the list of valid fields.
    Returns a tuple (is_valid, invalid_fields).
    """
    invalid_fields = [field for field in input_fields if field not in valid_fields]
    is_valid = len(invalid_fields) == 0
    return is_valid, invalid_fields