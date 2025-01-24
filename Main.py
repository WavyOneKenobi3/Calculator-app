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

operator = {
    "+" : add,
    "-" : sub, 
    "*" : multi, 
    "/": divide
 }

def calculator():
    num1 = int(input("First number? "))

    for symbol in operator:
        print(symbol)
    should_continue = True  #set a flag

    while should_continue:
        sign = input("Select an Operator. ")
        num2 = int(input("Second number? "))
        calc_funciton = operator[sign]
        answer = calc_funciton(num1, num2)
        print(f"{num1} {sign} {num2} = {answer}")
        
        ask_continue = input("do you want to continue with the same number? Yes or No if you want to start over? Type End to end program  ").lower()
        if ask_continue == "yes":
            num1 = answer
        elif ask_continue == "no":
            calculator()
        elif ask_continue == "end":
            should_continue == False
            break


calculator()