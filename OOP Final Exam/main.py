from bank import *

admin = Admin('admin','admin','123')
user = None

# admin reg


while True:
    if user == None: # user nai
        choise = input('\nUser/Admin ? (U/A) \nExit: (press any other key) \nEnter option: ').lower()
        if choise == 'u':
            option = input('\nLogin/Register ? (L/R) \nEnter option: ').lower()
            if option == 'r':
                typ = input('\nSavings/Current Account: (S/C) \nEnter option: ').lower()
                if typ != 's' and typ != 'c':
                    print('\nInvalid Account Type!\n')
                    continue
                name = input("Name: ")
                email = input('Email: ')
                address = input('Address: ')
                if typ == 's':
                    user = SavingsAccount(name,email,address)
                elif typ == 'c':
                    user = CurrnetAccount(name,email,address)
                print(f"\nAccount Registration Successful \nYour Account No is '{user.id}'\n")
            elif option == 'l':
                if len(Bank.user_list) == 0:
                    print("\nNo Registered Account Yet!\n")
                    continue
                name = input("User Name: ")
                account_no = input("Account No: ")
                user_found = False
                for account in Bank.user_list:
                    if name == account.name and account_no == account.id:
                        user = account
                        user_found = True
                        break
                if not user_found:
                    print('\nWrong Username or Account No.!\n')
            else:
                print("\nInvalid option!\n")

        elif choise == 'a':
            # if len(Bank.admin_list) == 0:
            #     print("\nNo Registered Admin Yet!\n")
            #     continue
            name = input("User Name: ")
            passward = input("Passward: ")
            user_found = False
            for admin in Bank.admin_list:
                if name == admin.name and passward == admin.passward:
                    user = admin
                    user_found = True
                    break
            if not user_found:
                print('\nWrong Username or Passward!\n')
        
        else:
            break # break while loop

    else: # user ase
        if user.type == "Admin":
            print(f'\nWelcome {user.name},\n')
            print('1. Create Another Admin Account')
            print('2. Delete User Account')
            print("3. Show User List")      
            print("4. Show Bank Balance")
            print("5. Show Total Loan Amount")
            print("6. Manage Loan Feature")
            print("7. Logout")

            choise = input('\nEnter Option: ')
            if choise == '1':
                name = input("Name: ")
                email = input('Email: ')
                passward = input("Set Passward: ")
                Bank.admin_list.append(Admin(name,email,passward))
                print("\nAdmin Registration Successful\n")
            elif choise == '2':
                user.delete_account(input('Enter Account No: '))
            elif choise == '3':
                user.show_user_list()
            elif choise == '4':
                user.total_bank_balance()
            elif choise == '5':
                user.total_loan()
            elif choise == '6':
                print(f'\nLoan Feature is: {int(Bank.loan_avaible)}')
                user.is_loan_avaiable(int(input('Turn Loan Feature [OFF/ON] ? (0/1): ')))
            else:
                user = None #logout
        
        else: # savings/current user
            print(f'\nWelcome {user.name},\n')
            print('1. Show Balance')
            print("2. Diposit")      
            print("3. Withdraw")
            print("4. Money Transfer")
            print("5. Show Transaction History")
            if user.type == "Savings":
                print("6. Logout")
            elif user.type == "Current": #else
                print("6. Take Loan")
                print("7. Logout")

            choise = input('\nEnter Option: ')
            if choise == '1':
                user.check_balance()
            elif choise == '2':
                user.diposit(int(input('Enter Amount: ')))
            elif choise == '3':
                user.withdraw(int(input('Enter Amount: ')))
            elif choise == '4':
                reciever_account_no = input('Reciever Account No: ')
                user.money_transfer(reciever_account_no,int(input('Enter Amount: ')))
            elif choise == '5':
                user.show_transaction_history()
            elif choise == '6':
                if user.type == "Savings":
                    user = None # Logout
                elif user.type == "Current": #else
                    user.take_loan(int(input('Enter Amount: ')))
            else:
                user = None # Logout

