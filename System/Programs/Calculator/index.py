import operations
import platform
import time
import os

#Clear Screen
def ClearScreen():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")

def DoMath(num1, num2, addType):
    if addType == "1":
        return operations.add(num1, num2)
    elif addType == "2":
        return operations.subtract(num1, num2)
    elif addType == "3":
        return operations.multiply(num1, num2)
    elif addType == "4":
        return operations.divide(num1, num2)
    elif addType == "5":
        return operations.exponent(num1, num2)
    else:
        return("Not a valid option. You shouldn't be here.")

def getnumbers(num):
    if num == "1":
        print("Whats the first number?")
        while True:
            try:
                return int(input("Calculator>"))
            except:
                print("Not a number.")   
    elif num == "2":
        print("Whats the second number?")
        while True:
            try:
                return int(input("Calculator>"))
            except:
                print("Not a number.")   
    else:
        print("Doesn't support more than 2 numbers in a equation.")



def main():
    ClearScreen()
    print("Welcom to the official PythonOS calculator.")
    while True:
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exponent. Negative exponents not supported.")
        print("6. Exit")
        AddType = ""
        while True:
            print("What would you like to do?")
            AddType = input("Calculator>").lower()
            if AddType in ["1", "add"]:
                AddType = "1"
                break
            elif AddType in ["2", "subtract"]:
                AddType = "2"
                break
            elif AddType in ["3", "multiply"]:
                AddType = "3"
                break
            elif AddType in ["4", "divide"]:
                AddType = "4"
                break
            elif AddType in ["5", "exponent"]:
                AddType = "5"
                break
            elif AddType in ["6", "exit"]:
                exit()
            else:
                print("Not a valid option.")
        
        num1 = getnumbers("1")
        num2 = getnumbers("2")
        print(f"Answer:{DoMath(num1, num2, AddType)}")
        time.sleep(2)

if __name__ == "__main__":
    main()