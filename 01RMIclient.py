import Pyro4
import os
import datetime
user = Pyro4.Proxy("PYRONAME:RMI.calculator")
name = input("What is your name? -> ").strip()

now = datetime.datetime.now()
print('date: '+now.strftime('%d-%m-%y')+'Time: '+now.strftime('%H:%M:%S'))

print(user.get_usid(name))


print("Enter number of desired calculations:\n" + '1. ADD\n'+'2. SUB\n' +'3.MUL\n'+'4. DIV\n'+'5. Table')
c = int(input("Enter choice: "))
while(c>0 and c <6):

    if(c == 1):
        a = int(input("Enter a: "))
        b = int(input("Enter b: "))
        print(user.add(a, b))
    elif(c==2):
        a = int(input("Enter a: "))
        b = int(input("Enter b: "))
        print(user.sub(a, b))
    elif(c==3):
        a = int(input("Enter a: "))
        b = int(input("Enter b: "))
        print(user.multiply(a, b))
    elif(c==4):
        a = int(input("Enter a: "))
        b = int(input("Enter b: "))
        print(user.divide(a, b))
    elif(c==5):
        a = int(input("Enter Number-"))
        print(user.table(a))
    else:
        print("Exiting")
        

    print("Enter number of desired calculations:\n" + '1. ADD\n'+'2. SUB\n' +'3. MUL\n'+'4. DIV\n')
    c = int(input("Enter choice: "))
