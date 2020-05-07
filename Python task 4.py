import random
import sys
import os

                
username1 = 'emialex'
password1 = 'podolski'
email1 = 'aerigi@gmail.com'
fullname1 = 'CHIWENDU EPE'


username2 = 'zizu'
password2 = 'you'
email2 = 'zizu@gmail.com'
fullname2 = 'MOSES SIMON'


staff = open('staff.txt', 'w')
staff.write('STAFF1\n')
staff.write(f'Username: {username1}\n')
staff.write(f'Password: {password1}\n')
staff.write(f'Email: {email1}\n')
staff.write(f'Fullname: {fullname1}\n\n')

staff.write('STAFF2\n')
staff.write(f'Username: {username2}\n')
staff.write(f'Password: {password2}\n')
staff.write(f'Email: {email2}\n')
staff.write(f'Fullname: {fullname2}\n\n')

staff.close
                                              
start = True
while start:
    print('''    WEMA BANK    ''')
 
    choice = int(input('(1)To login\n(2)To close app\n--> '))
    print()
    
    
    if choice == 1:
        check1 = True
        while check1:
            staff = open('staff.txt','r')
            for line in staff:
                new_username = str(input('Please input Username: ')).lower()                        
           
                if new_username == 'emialex' or new_username == 'zizu':
                    check1 = False
                    break                                            
                else:
                    print('Invalid username, please input valid username\n')
                    check1 = True
                
                                                   
        
        check2 = True
        while check2:
            staff = open('staff.txt','r')
            for line in staff:
                new_password = str(input('Please input your password: ')).lower()                        
            
                if new_username ==  'emialex':
                    if new_password == 'podolski': 
                        print()
                        print(f'Login Successful\nWelcome {fullname1}')
                        print()
                        check2 = False
                        break
                    else:
                        print('Password incorrect,please input valid password\n')
                        check2 = True
                        
                elif new_username == 'zizu':
                    if new_password == 'you':
                        print()
                        print(f'Login Successful\nWelcome {fullname2}')
                        print()
                        check2 = False
                        break                                            
                    else:
                        print('Password incorrect,please input valid password\n')
                        check2 = True
                    
                           
    else:
        sys.exit()
        

    session = open('session.txt', 'w+')                
    choices = True
    while choices:    
        user_choice = int(input('(1) to create new bank account\n(2) to check account details\n(3) to log out\n--> '))
        print()
        
        
        if user_choice == 1:
            print()
            ac_name = str(input('Please suggest an account name? ')).upper()
            ac_balance = str(input('What is your Opening Balance? '))
            ac_type = str(input('What is your preferred account type? '))
            ac_email = str(input('Input your mail address: '))
        
            session.write(f'1. Staff selected (1) and gave some details:\nAccount Name: {ac_name}\nAccount balance: {ac_balance}\nAccount Type: {ac_type}\nAccount_Email: {ac_email}\n\n')
            session.close()    
            counts = True
            while counts:
                x = random.uniform (1,10)
                a = str(x)
                dot = (a.index('.'))
                generated_num = (a[dot+1:-5])
                count = len(generated_num)
                if count == 10:
                    counts = False
                    break
                else:
                    counts = True        
            else:
                counts = True
                        
                        
            customer =  open('customer.txt','w')
            customer.write(f'\nAccount Name: {ac_name}\nOpening Balance: {ac_balance} Naira\nAccount Type: {ac_type}\nAccount Email: {ac_email}\nAccount Number: {generated_num}\n\n') 
            customer.close()      
            customer = open('customer.txt','r')
            print(customer.read())
            choices = True           
            print()
            
            session = open('session.txt', 'a+')
            session.write('2. Staff sees generated account number for the first time,    including the details staff earlier inputed\n')
            session.close()
            
            with open('customer.txt') as f:
                with open('session.txt', 'a+') as f1:
                    for line in f:
                        f1.write (line)
                        session.close()
            
            
        elif user_choice == 2:
            print()
            acct_check = True
            while acct_check:
                acct = (input('What is your account number? '))    
                if acct == generated_num:
                    customer = open('customer.txt','r')
                    print(f'\nHere are your detail:\n{customer.read()}')           
                    acct_check = False
                    break
                else:
                    print('Please input correct account number\n')
                    session = open('session.txt', 'a+')
                    session.write('Staff gave wrong account number\n')
            
                    acct_check = True
         
            choices = True
            print()
            session = open('session.txt', 'a+')
            session.write('\n4. Staff used option 2 to check full account details\n')
            session.close()
            with open('customer.txt') as s:
                with open('session.txt', 'a+') as s1:
                    for line in s:
                        s1.write (line)
                        session.close()       
                    
        elif user_choice == 3:
            os.remove('session.txt')
            choices = False
            print()
        start = True
        print()                    
                             
else:
    start = True