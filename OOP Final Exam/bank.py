from abc import ABC,abstractmethod

class Bank(ABC):
    loan_avaible = True
    admin_list = [] #ok
    user_list = [] #ok
    user_count = 0 # initailly
    balance = 0 #ok
    loan = 0
        

class Admin:
    def __init__(self,name,email,passward) -> None:
        self.type = "Admin"
        self.name = name
        self.email = email
        self.passward = passward
        Bank.admin_list.append(self)

    def delete_account(self,account_no):
        found = False
        for account in Bank.user_list:
            if account_no == account.id:
                Bank.user_list.remove(account)
                print(f'\nAccount {account_no} deleted\n')
                found = True
                break
        if not found:
            print(f'\nAccount {account_no} not found\n')

    def show_user_list(self):
        print("\n------------------------------------------")
        for account in Bank.user_list:
            print(account)
        print("------------------------------------------\n")

    def total_bank_balance(self):
        print(f"Bank Total Balance: {Bank.balance}\n")

    def total_loan(self):
        print(f"Bank Total Loan: {Bank.loan}\n")

    def is_loan_avaiable(self,avaiable:bool):
        if avaiable:
            Bank.loan_avaible = True
            print('Loan feature turned ON\n')
        else:
            Bank.loan_avaible = False
            print('Loan feature turned OFF\n')

class Account(ABC):
    def __init__(self,type,name,email,address) -> None:
        self.type = type
        self.name = name
        self.email = email
        self.address = address
        self.id = '12300' + str(Bank.user_count+1) #generate autometically
        self.balance = 0
        self.transaction_his = []

    def diposit(self,amount:int):
        if amount >= 0 :
            self.balance += amount
            Bank.balance += amount
            print(f"\nSuccessfully dipsited TK: {amount}\n")
        else:
            print("\nInvalid Amount!\n")

    def withdraw(self,amount:int):
        if amount >= 0 and amount <= self.balance:
            if Bank.balance == 0:
                print("\nThe Bank is bankrupt!\n")
            else:
                self.balance -= amount
                Bank.balance -= amount
                print(f"\nWithdrawn TK: {amount}\n")
        else:
            print("\nWithdrawal amount exceeded\n")

    def money_transfer(self,account_no,amount:int):
        if amount <= 0:
            print("\nInvalid amount\n")
        elif amount > self.balance:
            print("\nInsufficient balance!\n")
        else:
            for reciever in Bank.user_list:
                found = False
                if account_no == reciever.id:
                    found = True
                    self.balance -= amount
                    reciever.balance += amount
                    transation = Transation(self,reciever,amount)
                    self.transaction_his.append(transation)
                    reciever.transaction_his.append(transation)
                    print('\nTransation Successful\n')
                    break
            if not found:
                print("\nAccount does not exist!\n")
        
    def show_transaction_history(self):
        print("\n----------------------------------------------")
        for transation in self.transaction_his[ : : -1]:
            print(transation)
        print("----------------------------------------------\n")

    @abstractmethod
    def check_balance(self):
        raise NotImplementedError
    
    def __repr__(self) -> str:
        return f'Account Type:{self.type} Name:{self.name} Account No:{self.id}'

    
class SavingsAccount(Account):
    def __init__(self, name, email, address) -> None:
        super().__init__("Savings", name, email, address)
        Bank.user_list.append(self)
        Bank.user_count += 1

    def check_balance(self):
        print(f"\nName: {self.name} \nAccount Type: {self.type} \nAccount No: {self.id} \nBalance:  {self.balance}\n")

class CurrnetAccount(Account):
    def __init__(self, name, email, address,) -> None:
        super().__init__("Current", name, email, address)
        self.has_loan = 2
        self.loan = 0
        Bank.user_list.append(self)
        Bank.user_count += 1

    def check_balance(self):
        print(f"\nName: {self.name} \nAccount Type: {self.type} \nAccount No: {self.id} \nBalance:  {self.balance} \nLoan: {self.loan} \nLoan Avaiable: {self.has_loan}")

    def take_loan(self,amount:int):
        if not Bank.loan_avaible:
            print("\nSorry, Loan Service is not avaible right now!\n")
            return
        if self.has_loan == 0:
            print("\nSorry, you cann't take loan more than twice!\n")
        elif amount <= 0:
            print("\nInvalid Amount!\n")
        elif amount <= Bank.balance:
            Bank.balance -= amount
            self.loan += amount
            Bank.loan += amount
            self.has_loan -= 1
            print(f'\nTK {amount} Loan taken\n')
        else:
            print("\nSorry, Bank has not enough balance\n")


class Transation:
    def __init__(self,sender,reciever,amount:int) -> None:
        self.sender = sender
        self.reciever = reciever
        self.amount = amount

    def __repr__(self):
        return f'Sender: {self.sender.name} Account No: {self.sender.id}\nReciever: {self.reciever.name} Account No: {self.reciever.id}\nAmount: {self.amount}'





