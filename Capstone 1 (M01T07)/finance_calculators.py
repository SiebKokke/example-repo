import math 


#give the user a choice between investment and bond calculation
print('''
      Investment - to calculate the amount of interest you'll earn on 
      your investment.
      Bond       - to calculate the amount you'll have to pay on a home 
      loan.
      ''')


#user inputs their choice of investment or bond
choice = input('Enter either "invstment" or "bond" from the menu above to proceed: ').lower()
print(choice)


#if the user enters an invalid input
if choice != "investment" or "bond": 
    print('You have entered an invalid input. Please enter either "investment" or "bond".')


#if the user chooses investment, they should enter these parameters
if choice == "investment":
    
    amount_invested = int(input("Enter the amount of money you are deposititng: "))
    interest_rate = int(input("choose your interest rate: "))
    years = int(input("enter the number of years you are investing for: "))
    interest = input("choose between simple or compound interest: ").lower()
    
    r = (interest_rate/100)

    if interest == "simple":
        simple_interest = amount_invested * (1 + r * years)
        print("The future value of your investment with simple interest is", int(simple_interest))
    
    elif interest == "compound":
        compound_interest = amount_invested * math.pow((1 + r), years)
        print("The future value of your investment with compound interest is", int(compound_interest))


#if the user chooses bond, they should enter these parameters
elif choice == "bond":
   
    present_value = int(input("enter the present value of the house: "))
    bond_interest_rate = int(input("enter the interest rate: "))
    months = int(input("enter the number of months you plan to take to repay the bond: "))
    
    i = ((bond_interest_rate/100)/12)

    bond_repayment = ((i * present_value) / (1 - (1 + i)**(-months)))
    print("The amount you will need to pay each month is", int(bond_repayment))
