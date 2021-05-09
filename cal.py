def addition(num1,num2):
    return num1 + num2
def subraction(num1,num2):
    return num1 - num2
def division(num1,num2):
    return num1 / num2
def multiplication(num1,num2):
    return num1 * num2


while True:
    num1 = float(input("Enter first number:"))
    choice = input("Enter operation:")
    num2 = float(input("Enter second number:"))
    
    if choice in ('+','-','*','/'):
        # num1 = float(input("Enter first number:"))

        if choice == '+':
            print(num1,"+",num2,"=", addition(num1,num2))
        elif choice == '-':
            print(num1,"-",num2,"=", subraction(num1,num2))
        elif choice == '/':
            print(num1,"/",num2,"=", division(num1,num2))
        elif choice == '*':
            print(num1,"*",num2,"=", multiplication(num1,num2))