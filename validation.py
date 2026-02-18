def get_valid_choice(valid_choices, prompt="Select an option: ", error_msg="Invalid choice. Please try again."):
    valid_choices = {str(choice) for choice in valid_choices} # Ensure all choices are strings

    while True:
        choice = input(prompt).strip()
        if choice in valid_choices:
            return choice
        print(error_msg)

def validate_text(value):
    return isinstance(value, str) and value.strip() != ""

def validate_isbn(value):
    value = value.replace("-", "").replace(" ", "")
    return value.isdigit() and len(value) in (10, 13)

def validate_year(value):
    if not value.isdigit():
        return False
    year = int(value)
    return 1000 <= year <= 2026

def validate_boolean(value):
    if not value.lower() in ("true", "false"):
        return False
    return value

VALIDATORS = {
    "text": validate_text,
    "isbn": validate_isbn,
    "year": validate_year,
    "boolean": validate_boolean
}

FIELD_TYPES = {
    "title": {"key": "title","type": "text", "view": "default", "required": True, "editable": True, "searchable": True},
    "author": {"key": "author","type": "text", "required": True, "editable": True, "searchable": True},
    "isbn": {"key": "isbn","type": "isbn", "view": "default", "required": True, "editable": False, "searchable": True},
    "publication": {"key": "publication","type": "year", "view": "", "required": True, "editable": True, "searchable": True},
    "rarity": {"key": "rarity","type": "boolean", "view": "", "required": True, "editable": True, "searchable": True},
    "genre": {"key": "genre","type": "text", "view": "", "required": False, "editable": True, "searchable": True},
    "stock": {"key": "stock","type": "text", "view": "", "required": True, "editable": True, "searchable": False},
    "unit_price": {"key": "unit_price","type": "text", "view": "", "required": False, "editable": True, "searchable": False},
    "additional_info": {"key": "additional_info","type": "text", "view": "", "required": False, "editable": True, "searchable": False},

}

def field_options_menu(menu_fields):
    searchable_fields = [
        key for key, config in FIELD_TYPES.items()
        if config.get(menu_fields)
    ]

    menu = {}
    for index, field in enumerate(searchable_fields, start=1):
        menu[str(index)] = field

    menu[str(len(menu) + 1)] = None  # Return option

    return menu


def field_definer(field): # Convert user-friendly field name to internal key and type
    field = FIELD_TYPES[field]
    field_key = field["key"]
    field_type = field["type"]
    return field_key, field_type

def normalise(value, field_type):
    if field_type == "text":
        return value.lower().strip()

    if field_type == "isbn":
        return value.replace("-", "").replace(" ", "")

    if field_type == "year":
        return int(value)

    if field_type == "boolean":
        if value.lower() == "true":
            return True
        if value.lower() == "false":
            return False

    return value
