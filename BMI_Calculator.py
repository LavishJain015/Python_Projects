print("Welcome! To The BMI Calculator.")

weight = float(input("Now To Begin With, Enter Your Weight in KG: "))
height = float(input("Next, Enter Your Height in Metres: "))

print("Calculating...")

bmi = weight/(height*height)

while True:
    if bmi <=18.5:
        print(f"Your BMI Is {bmi}, You Are Underweight.")
        break
    elif bmi <= 24.9:
        print(f"Your BMI is {bmi}, Your Weight Is Normal.")
        break
    elif bmi <= 29.9:
        print(f"Your BMI is {bmi}, You Are Overweight.")
        break
    elif bmi >= 30.0:
        print(f"Your BMI is {bmi}, You Are Obese.")
        break
    else:
        print("Please Enter Your Weight And Height in Numbers")
        break