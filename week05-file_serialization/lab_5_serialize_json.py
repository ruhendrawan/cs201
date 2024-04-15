# Python file for INFSCI Lab 5
import json

class Customer():

    def __init__(self, user_id, first_name, last_name):
        self.user_id = user_id
        self.first_name = first_name
        self.last_name = last_name

    def to_dict(self):
        attr_dict = {
            "user_id" : self.user_id,
            "first_name" : self.first_name,
            "last_name" : self.last_name
        }
        # to return everything in a dictionary
        # return vars(self))
        return attr_dict

    def to_json(self):
        return json.dumps(self.to_dict())


class Account():

    def __init__(self, account_id, balance):
        self.account_id = account_id
        self.balance = balance

    def to_dict(self):
        return {
            "account_id" : self.account_id,
            "balance" : self.balance
        }
        
    def to_json(self):        
        return json.dumps(self.to_dict())
    

class Bank():

    def __init__(self, customers = [], accounts = []):
        self.customers = customers
        self.accounts = accounts

    def add_customer(self, customer):
        self.customers.append(customer)

    def add_account(self, account):
        self.accounts.append(account)

    def to_dict(self):
        customers_list = []
        for customer in self.customers:
            customers_list.append(customer.to_dict())
        attr_dict = {
            "customers" : customers_list,
            "accounts": [account.to_dict() for account in self.accounts]
        }
        return attr_dict

    def to_json(self):
        return json.dumps(self.to_dict(), indent=4)


john = Customer(1, "John", "Smith")
print(john.to_json())

first_account = Account(1, 5000)
print(first_account.to_json())


the_bank = Bank()
the_bank.add_customer(john)
the_bank.add_customer(Customer(1, "Jane", "Doe"))
the_bank.add_account(first_account)
the_bank.add_account(Account(2, 15000))
print(the_bank.to_json())