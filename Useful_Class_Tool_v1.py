Student_1 = int(input("Student 1, Enter Your Marks: "))

while True:
    if Student_1 <40:
        print("You Got D grade")
        break
    elif Student_1 <60:
        print("You Got C Grade")
        break
    elif Student_1 <80:
        print("You Got B Grade")
        break
    elif Student_1 <=100:
        print("You Got A Grade")
        break
    else:
        print("Enter Number between 1 to 100")

print("Now Student 2, Come here")
Student_2 = int(input("Student 2, Enter Your Marks: "))
      
while True:
    if Student_2 <40:
        print("You Got D grade")
        break
    elif Student_2 <60:
        print("You Got C Grade")
        break
    elif Student_2 <80:
        print("You Got B Grade")
        break
    elif Student_2 <=100:
        print("You Got A Grade")
        break
    else:
        print("Enter Number between 1 to 100")

print("Now Student 3, Come here")
Student_3 = int(input("Student 3, Enter Your Marks: "))

while True:
    if Student_3 <40:
        print("You Got D grade")
        break
    elif Student_3 <60:
        print("You Got C Grade")
        break
    elif Student_3 <80:
        print("You Got B Grade")
        break
    elif Student_3 <=100:
        print("You Got A Grade")
        break
    else:
        print("Enter Number between 1 to 100")

print("Now Student 4, Come Here")
Student_4 = int(input("Student 4, Enter Your Marks: "))

while True:
    if Student_4 <40:
        print("You Got D grade")
        break
    elif Student_4 <60:
        print("You Got C Grade")
        break
    elif Student_4 <80:
        print("You Got B Grade")
        break
    elif Student_4 <=100:
        print("You Got A Grade")
        break
    else:
        print("Enter Number between 1 to 100")

print("Now Student 5, Come Here")
Student_5 = int(input("Student 5, Enter Your Marks: "))

while True:
    if Student_5 <40:
        print("You Got D grade")
        break
    elif Student_5 <60:
        print("You Got C Grade")
        break
    elif Student_5 <80:
        print("You Got B Grade")
        break
    elif Student_5 <=100:
        print("You Got A Grade")
        break
    else:
        print("Enter Number between 1 to 100")
        break

average = Student_1+Student_2+Student_3+Student_4+Student_5
print(f"Your Class Average Marks is {average/5}")
print("Thank You For Using this app")

feedback = int(input("Enter Your Feedback, Rate This App from 1-5 Stars: "))

while True:
    if feedback <3:
        print("Sorry For Your Experience 🥺, We Will Improve Our App")
        break
    elif feedback <=5:
        print("Thank You!, We Appreciate It 😊😀")
        break
    else:
        print("Enter Between 1-5")
        break