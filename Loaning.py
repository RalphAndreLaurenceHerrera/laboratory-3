'''You are tasked with developing a Python program for a bank to help determine whether a customer is eligible for a loan based on their salary and loan amount requested.
The customer is eligible for a loan if:
    Their monthly salary is greater than or equal to 30,000.00.
    The loan amount they request is less than or equal to 10 times their monthly salary.
If customer is eligible, ask how many months to pay and add a 10% interest increase
If the customer is not eligible, display a message explaining why they are not approved (either low salary or too high loan request)'''

Sal = float(input("Please enter your monthly salary : ₱"))
LoanAmt = float(input("Please enter the amount of loan you want : ₱"))

if (Sal >= 30000):   
    if (LoanAmt <= Sal *10):
        print("You are eligible for a loan!")
        Months = int(input("Please enter the number of months that you want to repay the loan : "))
        AllRepay = LoanAmt * 1.10
        MnthlyRepay = AllRepay / Months
        print("Total loan amount with the interest: ₱{:.2f}" .format(AllRepay))
        print("Monthly payment: ₱{:.2f} For" .format(MnthlyRepay) , str(Months) , "Months" )
    else: 
        print("You are not eligible for a loan! Cause: Your loan request is too high.")
else:
    print("You are not eligible for a loan! Cause: Your monthly salary is too low.")