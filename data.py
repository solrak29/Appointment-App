from dataclasses import dataclass

@dataclass
class NewEntry:
    """
    DataClass: NewEntry
    Object to hold and pass around new entires that are entered for new client creation.
    This helps in passing 20 variables to a fucntion, where we can just pass an object

    TODO: We add classes that will cover formatting and provide other checks.
    """
    first_name: str
    last_name : str
    email     : str
    cell_phone_number : str
    user_name : str
    password : str
    is_admin : str
    provider : str
    is_active: bool