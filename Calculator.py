def add(x,y):
    return x + y

def subtract(x,y):
    return x - y

def Multiply(x,y):
    return x * y

def Divide(x,y):
    if y == 0:
        return "Error: Division by Zero"
    return x / y

while True:
    print("\nOptions:")
    print("Enter 'add' for addition")
    print("Enter 'subtract' for Subtraction")
    print("Enter 'multiply' for Multiplication")
    print("Enter 'divide' for division")
    print("Enter 'exit' to end the program")

    choice = input("Enter your choice:")

    if choice == 'exit':
        break

    if choice not in('add','subtract','multiply','divide'):
        print("Invalid input. Please choose a valid operation.")
        continue

    num1 = float(input("Enter first Number:"))
    num2 =  float(input("Enter second number:"))

    if choice == 'add':
        result =  add(num1,num2)
        operation = "addition"
    elif choice == 'subtract':
        result = subtract(num1,num2)
        operation = "subtraction"
    elif choice == 'multiply':
        result = Multiply(num1,num2)
        operation = "Multiplication"
    elif choice == "divide":
        result = Divide(num1,num2)
        operation = "Division"

    print(f"The result of operation is: {result}")