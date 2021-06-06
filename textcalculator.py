import time

print("Welcome to Calculator.py.\nThis is a calculator made by Rhytham Gupta !!!!!!")
perm = input("Do you wish to switch on calculator?(Y/N): ")

if perm == "Y":
    time.sleep(1)
    print("Opening Calculator.......")
    time.sleep(1)
    print("Opened")
    time.sleep(1)

    choice = input("Which operation you want to perform?(+, -, *, /,cb,sq)(please enter the sign): ")
    if choice.lower() == "+":
        num1 = int(input("What is the first number(Enter in digit form)?: "))
        num2 = int(input("What is the second number(Enter in digit form)?: "))
        print(f"Doing {num1} + {num2}.....")
        time.sleep(1)
        print(num1 +num2)
    elif choice.lower() == "cb":
        num1 = int(input("What is the first number(Enter in digit form)?"))
        print(f"Doing {num1}*{num1}*{num1}.....")
        time.sleep(1)
        print(num1*num1*num1)
    elif choice.lower() == "-":
        num1 = int(input("What is the first number(Enter in digit form)?"))
        num2 = int(input("What is the second number(Enter in digit form)?"))
        print(f"Doing {num1} - {num2}.....")
        time.sleep(1)
        print(num1 - num2)
    elif choice.lower() == "*":
        num1 = int(input("What is the first number(Enter in digit form)?"))
        num2 = int(input("What is the second number(Enter in digit form)?"))
        print(f"Doing {num1}*{num2}.....")
        time.sleep(1)
        print(num1*num2)
    elif choice.lower() == "/":
        num1 = int(input("What is the first number(Enter in digit form)?"))
        num2 = int(input("What is the second number(Enter in digit form)?"))
        print(f"Doing {num1}/{num2}.....")
        time.sleep(1)
        print(num1/num2)
    elif choice.lower() == "sq":
        num1 = int(input("What is the first number(Enter in digit form)?"))
        print(f"Doing {num1}*{num1}.....")
        time.sleep(1)
        print(num1*num1)
        
    else:
        print("Invalid!")


elif perm == "N":
    time.sleep(2)
    print("Ok, See You! Bye!, Have a good Day")
        
else:
    print("Invalid!")


    

