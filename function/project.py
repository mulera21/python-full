#------------------simple interest calculator------------------#

def simple_interest():
    principal = float(input("Enter the principal amount: "))
    rate = float(input("Enter the annual interest rate (in %): "))
    time = float(input("Enter the time in years: "))
    
    interest = (principal * rate * time) / 100
    total_amount = principal + interest
    
    print(f"Simple Interest: {interest}")
    print(f"Total Amount after {time} years: {total_amount}")
setup = simple_interest()


#------------------simple interest calculator------------------#
def interest_calculator(principal, rate, time):
    
    interest = (principal * rate * time) / 100
    return interest



def simple_interest():
    principal = float(input("Enter the principal amount: "))
    rate = float(input("Enter the annual interest rate (in %): "))
    time = float(input("Enter the time in years: "))

    interest = interest_calculator(principal, rate, time)
    total_amount = principal + interest
    print(f"Simple Interest: {interest}")
    print(f"Total Amount after {time} years: {total_amount}")
simple_interest()