number1 = float(input())
number2 = float(input())
number3 = float(input())

if number1 < (number2 + number3) and number2 < (number1 + number3) and number3 < (number1 + number2):
    print("You can draw a triangle")
else:
    print("You cant draw a triangle")