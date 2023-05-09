import json
from random import randint as rand
import os


filename = 'Bank.json'
global user_name 
def welcome():
    print("\t\t\t=============================================\t\t\t")
    print("\t\t\t==== ===1.Sign up           2.Sign in==== ===\t\t\t")
    print("\t\t\t=============================================\t\t\t")
    user = input("Input your choice: ")
    if user == '1':
        signup()
    elif user == '2':
        login()


def signup():
    try:
        with open(filename, 'r') as file:
            my_dict = json.load(file)
    except(FileNotFoundError, json.JSONDecodeError):
        my_dict = {}
    name = input('Name: ')
    email = input('Email: ')
    password = input("password: ")
    account_num = []
    while(len(account_num) < 9):
        account_num.append(str(rand(0,9)))
    account_num = "".join(account_num)
    amount = float(input('Least amount #1000: '))
    if amount < 1000:
        print('Amount is less than #1000')

    my_new_dict = {
        'Name': name,
        'Email': email,
        'Password': password,
        'Account_Number': account_num,
        'Balance': amount,
    }
    my_dict[name.lower()] = my_new_dict
    with open(filename,'w') as file:
        json.dump(my_dict,file)
    print(f" Your password is :{my_new_dict['Password']}")
    

def login():
    global user_name
    user_name = input('Name: ')
    with open(filename, 'r') as file:
        user = json.load(file)
        if user_name.lower() in user:
            print("\t\t\t==============================================\t\t\t")
            print(f"\t\t\t\tWELCOME BACK {user_name}! \t\t\t\t")
            print("\t\t\t==============================================\t\t\t\n")
            while True:
                user_input = input("""\n\t\t\t1.Withdraw
                        2.Deposit
                        3.Transfer
                        4.Check Balance
                        5.Modify user_details
                        6.Delete Account
                        7.Quit
                \t\t\t""")
                if user_input == '1':
                    Withdraw()
                elif user_input == '2':
                    Deposit()
                elif user_input == '3':
                    Transfer()
                elif user_input == '4':
                    Check_Balance()
                elif user_input == '5':
                    Modify()
                elif user_input == '6':
                    Delete()
                    break
                elif user_input == '7':
                    break


def Withdraw():
    with open(filename,'r') as file:
        user = json.load(file)
        data = user[user_name.lower()]
        amount = float(input('Amount: '))
        if amount > data['Balance']:
            print('Insufficient Balance')
        else:
            data['Balance'] -= amount
            print('Transaction Succefull!')
            
        user[user_name.lower()] = data
    with open(filename,'w') as file:
        json.dump(user,file)
    

def Deposit():
    with open(filename, 'r') as file:
        user = json.load(file)
        data = user[user_name.lower()]
        amount = float(input('Amount: '))
        data['Balance'] += amount
        user[user_name.lower()] = data
        print('Transaction succesful!')
    with open(filename, 'w') as file:
        json.dump(user,file)


def Transfer():
    with open(filename, 'r') as file:
        try:
            user = json.load(file)
            account_name = input('Account Name: ')
            data_1 = user[account_name.lower()]
            user_data = user[user_name.lower()]
            amount = float(input('Amount: '))
            if amount < user_data['Balance']:
                data_1['Balance'] += amount
                user_data['Balance'] -= amount
                print("Transaction successful!")
            elif amount > user_data['Balance']:
                print('Insufficient Balance')
            user[user_name.lower()] = user_data
            with open(filename, 'w') as file:
                json.dump(user,file)
        except(KeyError):
            print('\nNot a valid user')


def Check_Balance():
    with open(filename, 'r') as file:
        user = json.load(file)
        data = user[user_name.lower()]
        print(f"Balance = {data['Balance']}")


def Modify():
    with open(filename,'r') as file:
        user = json.load(file)
        data = user[user_name.lower()]
        name = input("New name: ")
        if name == "":
            name = data['Name']
        email = input("New email: ")
        if email == "":
            email = data['Email']
        password = input('New password: ')
        if password == "":
            password = data['Password']
        data['Name'] = name
        data['Email'] = email
        data['Password'] = password
        print('Successful!')
        user[user_name.lower()] = data
    with open(filename,'w') as file:
        json.dump(user,file)


def Delete():
    with open(filename, 'r') as file:
        user = json.load(file)
        del user[user_name.lower()]
        print('Successful!')
    with open(filename, 'w') as file:
        json.dump(user,file)


if __name__ == '__main__':
    welcome()
