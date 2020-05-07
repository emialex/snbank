# snbank
A txt file is created which stores the details of two staffs
There is a login or close app option for users to choose
If close app is chosen the program ends. If the login option
is chosen, the user inputs login details(username  and password).
If login details are incorrect, user is asked to repeat.
If login is successful, user is shown more options for creating;
create bank account, check bank account details and finally log out.


If create account is chosen, user is asked to input some details and 
a ten digit account number is generated and stored in customer.txt 
file and is displayed for user to see. After this, the program
goes back to the option of creating bank account, check bank account
details and log out option

If check bank account details is chosen, user is asked to input the
account number previously generated. After user inputs the account 
number, all the user details is displayed to the user. After this, 
the program goes back to the option of creating bank account, check
bank account details and log out option.

If log out is chosen, the user is signed out and taken to login and 
close app option


Meanwhile, when user successfully login, a session.txt file is created
to store user sessions. Once user log out, the stored session is deleted.
