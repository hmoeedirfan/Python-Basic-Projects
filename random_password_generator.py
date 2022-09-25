import random

# Creating variable of storing digits that are use in creating password
password = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()'

# Creating variable for storing length of password
password_length = int(input('Enter the password length: '))

# Creating variable for creating random password
random_password = "".join(random.sample(password,password_length))

# Printing random_password var
print(f'Your password is:{random_password}')