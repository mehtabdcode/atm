print()
print("WELCOME TO THE ATM\n")

pin = 1234
your_pin = int(input("Enter your pin to continue: "))
ballance = 50000

while your_pin != pin:
    print("ACCES DENIED")
    print()
    your_pin = int(input("Enter your pin to continue: "))

if your_pin == pin:
    print("ACCES GRANTED")
    print()
    choose = int(input("""Choose from the following: 

1)Press 1 to deposite money.

2)Press 2 to withdraw money.

3)Press 3 to check balance.

4)Press 4 to quit.
: """))
    while choose != 4:
        if choose == 3:
            print(f"Your ballance is {ballance}")

        elif choose == 2:
            withdrawl_amount = int(input("enter the amount you want to withdraw: "))

            while not (0 < withdrawl_amount < ballance):

                if withdrawl_amount == ballance:
                    print("Cannot withdraw all money.")
                    withdrawl_amount = int(input("enter the amount you want to withdraw: "))

                elif withdrawl_amount < 0:
                    print("The amount cannot be in negative.")
                    withdrawl_amount = int(input("enter the amount you want to withdraw: "))

                elif withdrawl_amount > ballance:
                    print("Amount too high cannot withdraw.")
                    withdrawl_amount = int(input("enter the amount you want to withdraw: "))

                else:
                    print("This is invalid")
                    withdrawl_amount = int(input("enter the amount you want to withdraw: "))

            if 0 < withdrawl_amount < ballance:
                ballance = ballance - withdrawl_amount
                print(f"{ballance} is your new ballance. ")

        elif choose == 1:
            deposite_amount = int(input("Enter the amount you want to deposite: "))

            while not (0 < deposite_amount < 200000):

                if deposite_amount < 0:
                    print("Deposite amount cannot be in negative.")
                    deposite_amount = int(input("Enter the amount you want to deposite: "))

                elif deposite_amount > 200000:
                    print("Cannot deposite more than two lakhs in one transaction.")
                    deposite_amount = int(input("Enter the amount you want to deposite: "))

                elif deposite_amount < 10:
                    print("Deposite amount cannot be less than 100.")
                    deposite_amount = int(input("Enter the amount you want to deposite: "))

                else:
                    print("INVALID AMOUNT")
                    deposite_amount = int(input("Enter the amount you want to deposite: "))

            if 10 < deposite_amount < 200000:
                ballance = ballance + deposite_amount
                print(f"{ballance} is your new ballance. ")

        print()
        choose = int(input("""Choose from the following: 

1)Press 1 to deposite money.

2)Press 2 to withdraw money.

3)Press 3 to check balance.

4)Press 4 to quit.
: """))
    if choose == 4:
        print("Thanks for using our service")