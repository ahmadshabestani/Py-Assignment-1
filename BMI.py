weight = float(input())
height = float(input())

BMI = weight / height ** 2


if BMI < 18.5:
    print("Underweight")
elif BMI >= 18.5 and BMI <= 24.9:
    print("Normal Weight")
elif BMI >= 25 and BMI <= 29.9:
    print("Normal Weight") 
elif BMI >= 30 and BMI <= 34.9:
    print("Normal Weight")  
elif BMI >= 35 and BMI <= 39.9:
    print("Normal Weight")  