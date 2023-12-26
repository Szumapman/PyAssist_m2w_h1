from abc import abstractmethod, ABC
from utility.addressbook import AddressBook
from utility.addressbook import Name
from utility.phone import Phone
from utility.email import Email
from utility.birthday import Birthday
from utility.address import Address
from utility.record import Record

class AbstractAddressbookInteraction(ABC):
    abstractmethod
    def __init__(self, addressbook: AddressBook) -> None:
        self.addressbook = addressbook
        
        
    @abstractmethod
    def add_name(self) -> Name:
        pass
    
    
    @abstractmethod
    def add_phone(self) -> Phone:
        pass
    
    
    @abstractmethod
    def add_email(self) -> Email:
        pass


    @abstractmethod
    def add_birthday(self) -> Birthday:
        pass
    

    @abstractmethod
    def add_address(self) -> Address:
        pass
    

    @abstractmethod
    def add_record(self):
        pass    
    
    @abstractmethod
    def del_record(self) -> Record:
        pass
    
    
    @abstractmethod
    def show(self, *args):
        pass
    
    
    @abstractmethod
    def show_upcoming_birthday(self, *args):
        pass
    
    
    @abstractmethod
    def edit_name(self, record):
        pass
    
    
    @abstractmethod
    def edit_birthday(self, record):
        pass
    
    
    @abstractmethod
    def edit_address(self, record):
        pass
    
    
    @abstractmethod
    def edit_phone(self, record):
        pass
    
    
    @abstractmethod
    def edit_email(email, record):
        pass
    
    
    @abstractmethod
    def edit_record(self, *args):
        pass
    
    
    @abstractmethod
    def search(self, *args):
        pass
    
    
    @abstractmethod
    def export_to_csv(self, *args):
        pass
    
    
    @abstractmethod
    def import_from_csv(self, *args):
        pass
    
    
    @abstractmethod
    def save_addresbook(self, filename):
        pass
    
    
    @abstractmethod
    def load_addresbook(self, filename):
        pass
    
    
    