# TabNine::sem
import rpyc

conn = rpyc.connect("localhost", 5555)

print("-------------------OPERATION--------------------")
print("1. Find Square Root")
print("2. To print square")
print("3. To Exit")
print("----------------X----------X--------------------")
choice = int(input("Enter the choice:"))
while(choice > 0 and choice < 3):
    if(choice == 1):
        num = int(input("Enter the number-"))
        x = conn.root.squareroot(num)
        print(f"square root({num})={x}")
        print()
    

    if(choice == 2):
        num = int(input("Enter the number-"))
        z = conn.root.square(num)
        print(f"{num}^2 = {z}")
        print()

    choice = int(input("Enter the choice:"))
