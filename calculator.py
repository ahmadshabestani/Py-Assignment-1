import math



print("operation :  + , - , / , * , sqrt , sin , cos , tan , cot , factorial")
op = input("Enter one operation : ")

if op == "+" or op == "-" or op == "*" or op == "/":
    number1 = float(input("Enter Number 1 : "))
    number2 = float(input("Enter Number 2 : "))
else:
    number1 = float(input("Enter Number : ")) 



if op == "+":
    result = number1 + number2
elif op == "-":
    result = number1 - number2
elif op == "*":
    result = number1 * number2
elif op == "/":
        result = number1 / number2
elif op == "sqrt":
    result = math.sqrt(number1)
elif op == "sin":
    result = math.sin(number1)
elif op == "cos":
    result = math.cos(number1)
elif op == "tan":
    result = math.tan(number1)
elif op == "cot":
    result = 1 / math.tan(number1)
elif op == "factorial":
    result = math.factorial(number1)


print(result)