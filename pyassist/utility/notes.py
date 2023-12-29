from collections import UserDict

from uti

class Notes(UserDict):
    """
    The Notes class extends the UserDict class by adding the add_note method
    and checking that the items added to the dictionary are valid (keys and values based on the Note class).

    Args:
        UserDict (class): parent class
    """
    # function used as a decorator to catch errors when item is adding to notes
    def _value_error(func):
        def inner(self, record):
            if not isinstance(record, Record):
                raise ValueError
            return func(self, record)
        return inner