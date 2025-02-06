print("✧･ﾟ: * Simple Calculator ✧･ﾟ:*")

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

operation = input("choose an operation (add, subtract, multiply, divide): ").lower()

if operation == 'add':
    result = num1 + num2
elif operation == 'subtract':
    result = num1 - num2
elif operation == 'multiply':
    result = num1 * num2
elif operation == 'divide':
    if num2 != 0:
        result = num1 /num2
    else:
        result = "Error! Denominator is zero."
else:
    result = "Invalid operation!"

print(f"The result is: {result}")
print("✧･ﾟ: Way to go! Let's solve more! ✧･ﾟ:")
