#define variables
FirstNumber = input("Enter first number: ")
Operator = input("Enter the operator ( +, -, *, /, %) : ")
SecondNumber = input("Enter second number: ")

# FirstNumber and SecondNumber are yet strings and not integers so lets turn it into int for arithematics to work
FirstNumber = int(FirstNumber)
SecondNumber = int(SecondNumber)

# let's add if , else conditions
if Operator == "+":
    print(FirstNumber + SecondNumber)
elif Operator == "-":
    print(FirstNumber - SecondNumber)
elif Operator == "*":
    print(FirstNumber * SecondNumber)
elif Operator == "/":
    print(FirstNumber / SecondNumber)
elif Operator == "%":
    print(FirstNumber % SecondNumber)

else:
    print("Invalid Operation")
