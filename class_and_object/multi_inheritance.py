class Bank:
    def get_name(self):
        return "Abc Bank"
    
    def get_interest(self):
        return 10

class Customer(Bank):
    __abcd = None

    def __init__(self, name, phone_number) -> None:
        self.name = name 
        self.phone_number = phone_number

    def set_abcd(self, abcd):
        self.__abcd = abcd


class CustomerAccontDetail(Customer, Bank):
    BALANCE = 0 

    def __init__(self, name, phone_number):
        self.customer = Customer(name=name, phone_number=phone_number)

    def get_balance(self):
        return self.BALANCE
    
    def get_customer_bank(self):
        return super().get_name()
    
    def get_customer_detail(self):
        return {
            "name": self.customer.name,
            "phone_number": self.customer.phone_number
        }
    

