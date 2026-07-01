print("Welcome To The Calculator 😄")
num_1 = int(input("To Begin With, Enter Your First Number: "))
num_2 = int(input("Now, Enter Your Second Number: "))
operator = input("Select The Operation You Want (add, subtract, multiply, divide): ")
Add = num_1+num_2
Subtract = num_1-num_2
Multiply = num_1*num_2
Divide = num_1/num_2
while True:
    if operator == "add":
        print(f"The Sum Of {num_1} and {num_2} is {Add}")
        break
    elif operator == "subtract":
        print(f"The Difference Of {num_1} and {num_2} Is {Subtract}")
        break
    elif operator == "multiply":
        print(f"The Product Of {num_1} and {num_2} is {Multiply}")
        break
    elif operator == "divide":
        print(f"The Quotient Of {num_1} and {num_2} is {Divide}")
        break
    else:
        print("Please Enter A Valid Operation, Options- add, subtract, multiply, divide, enter in lowercase letters only")

Feedback = int(input("Please Enter Your Feedback in stars upto 5: "))

while True:
    if Feedback <=3:
        print("Sorry For Your Experience, This Code Was written by a 10 year old")
        break
    elif Feedback <=5:
        print("We Appreciate It, This Code Was Written By a 10 Year Old")
        break
    else:
        print("Please Enter A number Between 1-5!")
        break
    