print ('\n                       A Simple Calculator in Python                \n')

def add(x,y):
    return x+y
def sub(x,y):
    return x-y
def mul(x,y):
    return x*y 
def divide(x,y):
    return x/y

print ('Select operation: \n')
print (' 1.for Addition')
print (' 2.for Subtract')
print (' 3.for Multiply')
print (' 4.for Divide\n')

choice = input('Enter your choice(1,2,3,4): ')

if choice in ('1','2','3','4'): 

    first_num = int(input('\nEnter your first number: '))
    second_num = int(input('Enter your second number: '))
   

    if (choice == '1'):
        result = add(first_num,second_num)
    if (choice == '2'):
        result = sub(first_num,second_num)
    if (choice == '3'):
        result = mul(first_num,second_num)
    if (choice == '4'):
        result = divide(first_num,second_num)

    print("\nTotal:",result)
else:
    print('Invalid')