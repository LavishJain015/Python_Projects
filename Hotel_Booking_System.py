hotel_main_menu = int(input("""================
WELCOME TO HOTEL
================

1. View Rooms
2. Book Roms
3. Exit
Enter Your Choice: """))

standard_room_price = 1500
deluxe_room_price = 2500
suite_room_price = 4000

while True:
    if hotel_main_menu == 1:
        print("""ALL ROOMS
        Room Type                            Price Per Day
        1. Standard                          1500
        2. Deluxe                            2500
        3. Suite                             4000""")
        hotel_main_menu = int(input("""================
WELCOME TO HOTEL
================

1. View Rooms
2. Book Roms
3. Exit
Enter Your Choice: """))
    elif hotel_main_menu == 2:
        customer_name = input("Enter Your Name: ")
        customer_ID = int(input("Enter Your Id Number (For example - 12342, 7563638): "))
        type_of_room_booking = int(input("""Enter The Room Type You Are Booking
        1. Standard
        2. Deluxe
        3. Suite
        Your Option (For example - 1,3): """))
        number_of_days_booking = int(input("Enter The Number Of Days You Will Be Staying: "))

        if type_of_room_booking == 1:
            total_price = standard_room_price * number_of_days_booking
            bill = (f"""==========BILL==========
            Customer's Name: {customer_name}
            Customer's ID: {customer_ID}
            Type Of Room Booked: {type_of_room_booking}
            Number Of Days Room Booked For: {number_of_days_booking}
            Total Price: {total_price}""")
            print(bill)
            
        elif type_of_room_booking == 2:
            total_price = deluxe_room_price * number_of_days_booking
            bill = (f"""==========BILL==========
            Customer's Name: {customer_name}
            Customer's ID: {customer_ID}
            Type Of Room Booked: {type_of_room_booking}
            Number Of Days Room Booked For: {number_of_days_booking}
            Total Price: {total_price}""")
            print(bill)
            
        elif type_of_room_booking == 3:
            total_price = suite_room_price * number_of_days_booking
            total_price = deluxe_room_price * number_of_days_booking
            bill = (f"""==========BILL==========
            Customer's Name: {customer_name}
            Customer's ID: {customer_ID}
            Type Of Room Booked: {type_of_room_booking}
            Number Of Days Room Booked For: {number_of_days_booking}
            Total Price: {total_price}""")
            print(bill)
            
    elif hotel_main_menu == 3:
        break
    else: print("Invalid Value!")
    hotel_main_menu = int(input("""================
    WELCOME TO HOTEL
    ================
            
    1. View Rooms
    2. Book Roms
    3. Exit
    Enter Your Choice: """))

    

            




