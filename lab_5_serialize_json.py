# Python file for INFSCI Lab 5

import json

class Customer():

    def __init__(self, user_id, first_name, last_name):
        self.user_id = user_id
        self.first_name = first_name
        self.last_name = last_name

    def to_json(self):
        attr_dictionary = {
            "user_id" : self.user_id,
            "first_name" : self.first_name,
            "last_name" : self.last_name
        }
        
        return json.dumps(attr_dictionary)

john = Customer(1, "John", "Smith")
print(john.to_json())

class Account():

    def __init__(self, account_id, balance):
        self.account_id = account_id
        self.balance = balance

    def to_json(self):
        attr_dictionary = {
            "account_id" : self.account_id,
            "balance" : self.balance
        }
        
        return json.dumps(attr_dictionary)
    
first_account = Account(1, 5000)
print(first_account.to_json())

class Bank():

    def __init__(self, customers = [], accounts = []):
        self.customers = []
        self.accounts = []

    def add_customer(self, customer):
        self.customers.append(customer)

    def add_account(self, account):
        self.accounts.append(account)

    def to_json(self):
        attr_dictionary = {
            "customers" : [customer.__dict__ for customer in self.customers],
            "accounts": [account.__dict__ for account in self.accounts]
        }
        
        return json.dumps(attr_dictionary)

the_bank = Bank()
the_bank.add_customer(john)
the_bank.add_customer(Customer(1, "Jane", "Doe"))
the_bank.add_account(first_account)
the_bank.add_account(Account(2, 15000))
print(the_bank.to_json())