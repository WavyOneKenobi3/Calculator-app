# Calculator
def add(a, b):
    return a + b
        
def sub(a, b):
    return a - b
        
def divide(a, b):
    if b == 0:
        return "Error: Division by zero is not allowed"
    return a / b
        
def multi(a, b):
    return a * b

def signal(num1, num2):
    try:                        #put all of this into a their functions
        num1 = int(input("First number? "))
        num2 = int(input("Second number? "))
        sign = input("Select +, -, /, or *: ")
        if sign == "+":
            print(f"{num1} {sign} {num2} = {add(num1, num2)}")
        elif sign == "-":
            print(f"{num1} {sign} {num2} = {sub(num1, num2)}")
        elif sign == "*":
            print(f"{num1} {sign} {num2} = {multi(num1, num2)}")
        elif sign == "/":
            print(f"{num1} {sign} {num2} = {divide(num1, num2)}")
        else:
            print("Invalid operator! Please select +, -, /, or *.")
    except ValueError:
        print("Invalid input! Please enter a number.")
        
def Calc():
    while True:
        signal() #change this
        pervious_num = 0
        next_input = input("Do you want to continue? Yes or No: ").lower()
        if next_input == "yes":
            
            signal(num1 = )
        elif next_input == "no":
            break
            print("Goodbye!")
        else:
            print("Invalid response! Exiting.")
            break

Calc()