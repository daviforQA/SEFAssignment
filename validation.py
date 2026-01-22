def get_valid_choice(valid_choices, prompt="Select an option: ", error_msg="Invalid choice. Please try again."):
    valid_choices = {str(choice) for choice in valid_choices} # Ensure all choices are strings

    while True:
        choice = input(prompt).strip()
        if choice in valid_choices:
            return choice
        print(error_msg)
