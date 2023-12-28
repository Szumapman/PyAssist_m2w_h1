import difflib
from pathlib import Path
from datetime import datetime, timedelta
from prompt_toolkit import prompt
from prompt_toolkit.completion import FuzzyWordCompleter

from utility.abstract_addressbook_interaction import AbstractAddressbookInteraction
from utility.addressbook import AddressBook
from utility.name import Name
from utility.phone import Phone
from utility.email import Email
from utility.birthday import Birthday
from utility.address import Address
from utility.street import Street
from utility.city import City
from utility.zip_code import ZipCode
from utility.country import Country
from utility.record import Record

class CliAddressBookInteraction(AbstractAddressbookInteraction):
    
    def __init__(self, addressbook: AddressBook) -> None:
        self.addressbook = addressbook

    def _set_str_name(self, argument):
        if argument:
            return argument.strip().title()
        return input("Type name or <<< if you want to cancel: ").strip().title()
    

    def add_name(self, argument) -> Name:
        while True:
            name = self._set_str_name(argument)
            if name in self.addressbook.keys():
                print(f"Contact {name} already exists. Choose another name.")
                continue
            elif name == "<<<" or name == '':
                return None
            else:
                return Name(name)
    

    def add_phone(self) -> Phone:
        phone = input("Type phone or <<< if you want to cancel: ")
        if phone == "<<<":
            return None
        return Phone(phone)
    
    
    def add_email(self) -> Email:
        email = input("Type email or <<< if you want to cancel: ")
        if email == "<<<":
            return None
        return Email(email)


    def add_birthday(self) -> Birthday:
        birthday = input("Input the date of birth as day month year (e.g. 15-10-1985 or 15 10 1985) or <<< if you want to cancel: ")
        if birthday == "<<<" or birthday == "":
            return None
        return Birthday(birthday)  
    

    def add_address(self) -> Address:
        street = input("street: ")
        city = input("city: ")
        zip_code = input("zip code: ")
        country = input("country: ")
        return Address(Street(street), City(city), ZipCode(zip_code), Country(country))
    
    
    #dict for create_record commands
    CREATE_RECORD_COMMANDS = {
        'phones': add_phone,
        'emails': add_email,
        'birthday': add_birthday,
        'address': add_address,
    }
    
    
    def create_record(self, name: Name) -> Record:
        phones = []
        emails = []
        birthday = None
        address = None
        record_fields = [phones, emails, birthday, address]
        record_fields_names = list(self.CREATE_RECORD_COMMANDS.keys())
        i = -1
        for field in record_fields:
            i += 1
            answer = input(f'Type y (yes) if you want to add {record_fields_names[i]}: ').strip().lower()
            if answer == "y" or answer == "yes":
                data = self.CREATE_RECORD_COMMANDS[record_fields_names[i]](self)
                if isinstance(field, list):
                    while True:
                        if data:
                            field.append(data)
                            answer = input(f'Type y (yes) if you want to add more {record_fields_names[i]}: ').strip().lower()
                            if answer == "y" or answer == "yes":
                                data = self.CREATE_RECORD_COMMANDS[record_fields_names[i]](self)
                                continue
                        break
                else:
                    field = data
        return Record(name, phones, emails, birthday, address)    

                
    def add_record(self, argument):
        name = self.add_name(argument)
        if name:
            self.addressbook.add_record(self.create_record(name))
            return f"A record: {name} added to your address book."
        return "Operation cancelled"
    
    
    def del_record(self, argument) -> Record:
        name = self._set_str_name(argument)
        if name == '<<<':
            return "Operation cancelled"
        elif name in self.addressbook:
            del self.addressbook[name]
            return f'Record {name} deleted successfully.'
        else:
            return f"Record {name} not found in the address book."
        
    
    def show(self, argument):
        if argument:
            name_record_to_show = self._set_str_name(argument)
            if name_record_to_show in self.addressbook:
                return f'{self.addressbook[name_record_to_show]}'
            return f"Contact {name_record_to_show} doesn't exist."
        if len(self.addressbook) == 0:
            return f'Your addressbook is empty.'
        records_info = ""       
        for record in self.addressbook.values():
            records_info += repr(record)
        return records_info
        

    def show_upcoming_birthday(self, argument):
        number_of_days = 7
        if argument:
            number_of_days = int(argument)
            if number_of_days < 1:
                raise ValueError
        current_date = datetime.now().date()
        upcoming_birthdays = {current_date + timedelta(days=i): [] for i in range(number_of_days + 1)}
        info = f"Upcoming birthdays in the next {number_of_days} days:"
        is_upcoming_birthday = False
        for record in self.addressbook.values():
            difference = record.days_to_birthday()
            if -1 < difference <= number_of_days:
                    upcoming_birthdays[current_date + timedelta(difference)].append(record)
        for day, records in upcoming_birthdays:
            if records:
                names = []
                for record in records:
                    names.append(record.name)
            info += "\n{:>10}, {:<18}: {:<60}".format(day.strftime('%A'), day.strftime('%d %B %Y'), '; '.join(names))
            is_upcoming_birthday = True
        if is_upcoming_birthday:
            return info
        return f"No upcoming birthdays in the next {number_of_days} days."    

        
    def edit_name(self, record):
        name = self.add_name(self)
        if name:
            self.addressbook.add_record(Record(name, record.phones, record.emails, record.birthday, record.address))
            return f'Name changed from {self.addressbook.pop(record.name.value).name} to {name}'
        return "Operation canceled."
            
    
    def edit_birthday(self, record):
        birthday = self.add_birthday()
        if birthday:
            self.addresbook[record.name.value].birthday = birthday
            return f"{record.name} birthday set to: {birthday}"
        return "Operation canceled."
    

    def edit_address(self, record):
        record.address = self.add_address()
        return f"{record.name} new {record.address}"
    

    # init function for phone changed
    def edit_phone(self, record):
        return self._change_data(record, "phone")
    
    
    # init function for email changed
    def edit_email(self, record):
        return self._change_data(record, "email") 


    # help function to choose email or phone
    def _item_selection(self, record, data_list, show):
        print(f"Contact {record.name} {type}s:\n{show}", end="")
        number_to_change = input("Select by typing a number (for example 1 or 2): ")
        try:
            number_to_change = int(number_to_change) - 1
            if number_to_change >= len(data_list) or number_to_change < 0:
                raise ValueError
            return number_to_change
        except ValueError:
            return -1    
    
    
    # help function to create string from phones or emails
    def _str_phones_or_emails(self, list_to_str):
        info = ''
        i = 1
        for item in list_to_str:
            info +=f'\n{i}. {item}'
            i += 1
        return info    
        
        
    # change of phone or email
    def _change_data(self, record, type):
        if type == "phone":
            data_list = record.phones
            add_type = record.add_phone
        elif type == "email":
            data_list = record.emails
            add_type = record.add_email
        show = self._str_phones_or_emails(data_list)
        while True:
            if data_list:
                while True:
                    answer = input(f"Contact {record.name} {type}s:{show}\nDo you want to change it, add another or delete? 1 chanege, 2 add, 3 delete: ")
                    if answer == "1" or answer.strip().lower() == 'change':
                        if len(data_list) == 1:
                            data_to_add = self.add_email() if type == "email" else self.add_phone()
                            if data_to_add:
                                data_list[0] = data_to_add
                                return f"{type} edited sucessfully."
                            return "Operation canceled."
                        else:
                            number_to_change = self._item_selection(record, data_list, show)
                            if number_to_change == -1:
                                print("Wrong option, try again")
                                break
                            data_to_add = self.add_email() if type == "email" else self.add_phone()
                            if data_to_add:
                                data_list[number_to_change] = data_to_add
                                return f"{type} edited sucessfully."
                            return "Operation canceled."
                    elif answer == "2" or answer.strip().lower() == 'add':
                        data_to_add = self.add_email() if type == "email" else self.add_phone()
                        if data_to_add:
                            add_type(data_to_add)
                            return f"{type} edited sucessfully."
                        return "Operation canceled."
                    elif answer == "3" or answer.strip().lower() == 'delete':
                        if len(data_list) == 1:
                            data_list.clear()
                            return f"{type} edited sucessfully."
                        else:
                            number_to_delete = self.item_selection(record, data_list, show)
                            if number_to_delete == -1:
                                print("Wrong option, try again")
                                break
                            print(f"{type} no {number_to_delete+1}: {data_list.pop(number_to_delete)} deleted.")
                            return f"{type} edited sucessfully."
                    else:
                        print("Unrecognized command, try again.")
            else:
                data_to_add = self.add_email() if type == "email" else self.add_phone()
                if data_to_add:
                    add_type(data_to_add)
                    return f"{type} edited sucessfully."
                return "Operation canceled."   


    # dict for record edit handler
    RECORD_EDIT_COMMANDS = {
        "name": edit_name, 
        "phone": edit_phone, 
        "email": edit_email,
        "address": edit_address,
        "birthday": edit_birthday,
        }

    
    def edit_record(self, argument):
        name = self._set_str_name(argument)
        if name in self.addressbook:
            record = self.addressbook[name]
            # command = prompt(f"Type what you want to change in {name} contact: ", completer=command_completer)
            command = input(f"Type what you want to change in {name} contact: ") 
            return self._execute_command(self.RECORD_EDIT_COMMANDS, command, record)
        return f"Record {name} not found in the address book."
    

    def search(self, argument):
        if argument:
            search_query = argument
        else:
            search_query = input("Enter the search query (or type '<<<' to exit): ").strip()
            if search_query == "<<<" or "":
                return "Operation canceled."
        query_addressbook = self.addressbook.search(search_query)           
        if query_addressbook:
            return "Search results:\n" + CliAddressBookInteraction(query_addressbook).show('')
        return "No matching results found."
    
    def _import_export_prepare(self,argument):
        if argument:
            filename = argument
        else:
            filename = input("Type the filename (e.g., output.csv) or <<< to cancel: ").strip()       
        if filename == "<<<" or filename == "":
            return None
        program_dir = Path(__file__).parent.parent
        return program_dir.joinpath("data/"+filename)

    def export_to_csv(self, argument):
        full_path = self._import_export_prepare(argument)
        if full_path:
            self.addressbook.export_to_csv(full_path)
            return f"Data exported successfully to {full_path}."
        return "Export cancelled."
    
    
    def import_from_csv(self, argument):
        full_path = self._import_export_prepare(argument)
        if full_path:
            self.addressbook.import_from_csv(full_path)
            return f"Data imported successfully from {full_path}."
        return "Import cancelled."


    def save_addresbook(self, filename):
        # for the time being, the path to the addressbook file is hardcoded
        program_dir = Path(__file__).parent.parent
        filename = program_dir.joinpath("data/addresbook.dat")
        self.addressbook.save_addresbook(filename)
        return "Addressbook saved."
    
    
    def load_addresbook(self, filename):
        # for the time being, the path to the addressbook file is hardcoded
        program_dir = Path(__file__).parent.parent
        filename = program_dir.joinpath("data/addresbook.dat")
        self.addressbook = self.addressbook.load_addresbook(filename)
        # return f"Addressbook loaded from file {filename}"
    
    # dict for addressbook menu
    ADDRESSBOOK_MENU_COMMANDS = {
        # "exit": cli_pyassist_exit,
        "add": add_record, 
        "edit": edit_record,
        "show": show,
        "delete": del_record,
        "export": export_to_csv, 
        "import": import_from_csv, 
        "birthday": show_upcoming_birthday, 
        "search": search,
        "save": save_addresbook, 
        # "up": pyassit_main_menu,
        # "help": addressbook_commands,
    }
    
    
    def _execute_command(self, commands_dict: dict, cmd: str, argument):
        """Function to execute user commands

        Args:
            cmd (str): user command
            argument: argument to process
        """
        if cmd not in commands_dict:
            matches = difflib.get_close_matches(cmd, self.COMMANDS)
            info =  f'\nmaybe you meant: {' or '.join(matches)}' if matches else ''
            return f'Command {cmd} is not recognized' + info
        cmd = commands_dict[cmd]
        return cmd(self, argument)
    
    
    # function that parses user input commands
    def  _parse_command(self, user_input: str) -> (str, str):
        """
        Parse user input command

        Args:
            user_input (str): user input command
        
        Returns:
            str: command
            str: argument
        """
        tokens = user_input.split()
        command = tokens[0].lower()
        argument = "".join(tokens[1:])
        return command, argument
    
    
    # receiving a command from a user
    def _user_command_input(self):
        commands_completer = FuzzyWordCompleter(self.ADDRESSBOOK_MENU_COMMANDS.keys())
        user_input = prompt(f'PyAssist  addressbook >>> ', completer=commands_completer).strip()
        if user_input:
            return self._parse_command(user_input)
        return "", ""
    
    def cli_addressbook_menu(self):
        while True:
            # cmd, arguments = user_command_input(completer, "address book")
            cmd, argument = self._user_command_input()
            info = self._execute_command(self.ADDRESSBOOK_MENU_COMMANDS, cmd, argument)
            print(info)