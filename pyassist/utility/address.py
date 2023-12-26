from utility.city import City
from utility.country import Country
from utility.street import Street
from utility.zip_code import ZipCode

class Address:
    def __init__(self, street: Street, city: City, zip_code: ZipCode, country: Country) -> None:
        self.street = street
        self.city = city
        self.zip_code = zip_code
        self.country = country
        
    
    def __repr__(self) -> str:
        return f"Address:{f'\nstreet: {self.street} ' if self.street else ''}" + f"{f'\ncity: {self.city} ' if self.city else ''}" + f"{f'\nzip code: {self.zip_code} ' if self.zip_code else ''}" + f"{f'\ncountry: {self.country} ' if self.country else ''}"
           