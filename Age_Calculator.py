#Print Statement For Welcoming User.
print("Hello, Welcome To The Age Calculator  😀😀")
#Takes Input For User, Asks Them For Their Birth Year.
birth_year = int(input("Enter Your Birth Year To Calculate Your Age:  "))
current_year = int(input("Enter The Current Year in Numbers (i.e, 2026): "))
age = current_year - birth_year
print(f"Your Age Is {age}")
while True:
    if age <= 1:
        print("You Are An Infant/Baby.")
        break
    elif age <= 3:
        print("You Are A Toddler.")
        break
    elif age <= 12:
        print("You Are A Child.")
        break
    elif age <= 19:
        print("You Are A Teenager.")
        break
    elif age <= 39:
        print("You Are A Yound Adult.")
        break
    elif age<= 59:
        print("You Are A Middle Aged Adult.")
        break
    elif age >=60:
        print("You Are A Senior Citizen.")
        break
    else: print("Please Enter Your Age In Numbers (i.e, 23)")
    break

feedback_wish = input("Do You Want To Give Feedback, (Y/N): ")

while True:
    if feedback_wish == "Y":
        feedback_stars = int(input("Enter Your Feedback (1-5 Stars): "))
        while True:
              if feedback_stars <=3:
                  print("Sorry For Your Experience, This Program Was Written By A 10 Year Old.")
                  break
              elif feedback_stars >=5:
                  print("I Appreciate It, This Code Was Written By a 10 Year Old.")
                  break
              else: print("Please Enter Feedback In Numbers, (i.e, 5)")
              break
    elif feedback_wish == "N":
        print("Thank You For Reviewing This Code, This Code Was Written By A 10 Year Old.")
        break
    else: print("Please Enter In Capital Letters (Y/N)")
    break

            
    