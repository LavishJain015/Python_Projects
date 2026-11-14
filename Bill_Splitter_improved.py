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
        tip_splitted = tip / number_of_people
        new_and_final_bill = bill_splitted + tip_splitted
        print(f"We Are Very Pleased And We Appreciate It That You Tipped. Each Person Has To Pay {new_and_final_bill} ")
        break
    elif tip_wish == "N":
        print(f"Each Person Has To Pay {bill_splitted}")
        break
    else:
        print("Please Enter In Capital Letters: ")
        tip_wish = (input("Do You Wish To Add Tip (Y/N) : "))




