print("Hello welcome to the ATM!")
correct_pin = 1234
pin_entered = float(input("Enter Your Pin: "))
new_balance = 5000
while True:
    if pin_entered == correct_pin:
        print("Access Granted!")
        main_menu = int(input("""=====Welcome To ATM=====
        1. Check Balance
        2. Deposit Money
        3. Withdraw money
        4. Exit
        Your Option: """))

        while True: 
            if main_menu == 1:
                balance = 5000
                print(new_balance)
                break
            elif main_menu == 2:
                deposit_amount = float(input("Enter the amount you want to deposit: "))
                new_balance = deposit_amount + new_balance
                print(f"Your new balance is {new_balance}.")
                break
            elif main_menu == 3:
                withdraw_amount = float(input("Enter the amount you want to withdraw: ")) 
                if withdraw_amount > new_balance:
                        print("The amount You Entered exceeds the money you currently have in your account")
                        withdraw_amount = float(input("Enter the amount you want to withdraw: ")) 
                elif withdraw_amount <= new_balance:
                        new_balance = new_balance - withdraw_amount
                        print(f"Your new balance is {new_balance}.")
                        break
                elif main_menu == 4:
                    print("Thank you for using the ATM")
                    break
    elif main_menu == 4:
        break
        
 
                
                

    elif  pin_entered != correct_pin:
        print("Access Denied!")
        break

    else:
        print("The Pin is atleast four digits.`")
        break
