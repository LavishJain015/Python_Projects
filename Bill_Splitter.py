print("Hello, Welcome To Bill Splitter.")
total_bill = float(input("Please, Enter The Total Bill : "))
number_of_people = int(input("Please Enter The Number Of People: "))
final_bill = total_bill
bill_splitted = final_bill/number_of_people
print(f"Each Person Has To Pay {bill_splitted}")
tip_wish = (input("Do You Wish To Add Tip (Y/N) : "))

while True:
    if tip_wish == "Y":
        tip = float(input("Please Enter The Amount You Want To Tip: "))
        new_and_final_bill = bill_splitted + tip
        print(f"We Are Very Pleased And We Appreciate It That You Tipped. Each Person Has To Pay {new_and_final_bill} ")
        break
    elif tip_wish == "N":
        print(f"Each Person Has To Pay {bill_splitted}")
        break
    else:
        print("Please Enter In Capital Letters: ")
        tip_wish = (input("Do You Wish To Add Tip (Y/N) : "))

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
    feedback_wish = input("Do You Want To Give Feedback, (Y/N): ")
