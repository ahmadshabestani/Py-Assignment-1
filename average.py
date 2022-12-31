name = input()
family = input()
number1 = float(input())
number2 = float(input())
number3 = float(input())


average = (number1 + number2 + number3) / 3

if average >= 17 :
    print("Great")
elif average < 17 and average >= 12:
    print("Normal ")
elif average < 12:
    print("Faill")