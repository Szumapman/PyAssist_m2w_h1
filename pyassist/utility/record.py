from datetime import datetime
from utility.name import Name
from utility.phone import Phone
from utility.email import Email

class Record:
    """
    Record class represents a single address book record consisting of name, phone list, email list birthday and address.
    """

    def __init__(self, name: Name, phones=[], emails=[], birthday=None, address=None) -> None:
        self.name = name
        self.phones = phones
        self.emails = emails
        self.birthday = birthday
        self.address = address
        

    # Add phone to phones list
    def add_phone(self, phone: Phone):
        self.phones.append(phone)


    # Remove phone from phones list
    def remove_phone(self, phone: Phone):
        self.phones.remove(phone)


    # Change phone - add new one and remove old one
    def change_phone(self, old_phone, new_phone):
        index = self.phones.index(old_phone)
        self.phones[index] = new_phone


    # Add email to emails list
    def add_email(self, email: Email):
        self.emails.append(email)


    # Remove email from emails list
    def remove_email(self, email: Email):
        self.emails.remove(email)


    # Change email - add new one an dremove old one
    def change_email(self, old_email, new_email):
        index = self.emails.index(old_email)
        self.emails[index] = new_email
        
    # return amount of days to the next birthday
    def days_to_birthday(self):
        current_date = datetime.now().date()
        this_year_birthday = datetime(
            year=current_date.year,
            month=self.birthday.value.month,
            day=self.birthday.value.day,
        ).date()
        difference = this_year_birthday - current_date
        if difference.days == 0:
            return f"{self.name}'s birthday is today!"
        elif difference.days > 0:  # if the birthday is before this year's end
            return f"day(s) to next birthday: {difference.days}"
        # if the next birthday is in next year
        next_birthday = datetime(
            year=this_year_birthday.year + 1,
            month=this_year_birthday.month,
            day=this_year_birthday.day,
        ).date()
        return f"day(s) to next birthday: {(next_birthday -  current_date).days}"