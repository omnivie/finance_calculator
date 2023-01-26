# Importing math library for mathematical calculations

import math

print('''Hello! Please choose what financial calculator you would like to use:

investment - to calculate the amount of interest you will earn on your investment
mortgage - to calculate the amount you'll have to pay on a home loan
''')

# Asking user to choose what calculation they would like to make an investment of a monthly
# repayment for a mortgage. Then running two While loops to ensure that user enters options
# correctly as wrong input can produce nor desired result and confuse the user

while True:
    investment_type = input("Please select investment type. investment/mortgage:  ")
    if investment_type.lower() not in ("investment", "mortgage"):
        print("Please type investment or mortgage")
    else:
        break

# using if/elif statements to collect appropriate data from the user and then carry out appropriate calculations
# printing the final result in a sentence

if investment_type.lower() == "investment":
    amount = float(input("How much are you planning to invest? "))
    rate = float(input("What is the annual interest rate? "))
    period = int(input("How many years you would like to keep the investment? "))
    while True:
        interest = input("What type of interest your would prefer? simple/compounded ")
        if interest.lower() not in  ("simple", "compounded"):
            print("Please type simple or compounded")
        else:
            break
    if interest.lower() == "simple":
        end_amount = round((amount * (1 + (rate / 100) * period)), 2)
    else:
        end_amount = round((amount * (1 + rate / 100) ** period), 2)
    print("")
    print(f"Your investment will grow to a total amount of {end_amount} in {period} years")

# if the user has chosen mortgage taking relevant inputs for mortgage calculations
elif investment_type.lower() == "mortgage":
    house_vl = float(input("What is present value of the house? "))
    mort_rt = float(input("What is the annual interest rate? "))
    term = int(input("How many months repayment term? "))
    monthly_rt = mort_rt/12/100

# Calculating monthly mortgage repayment using the following formula x = (i*P)/(1 - (1+i)^(-n)) and then printing
# the result in a sentence
    monthly_repayment = round(((monthly_rt * house_vl) / (1 - (1 + monthly_rt)**-term)), 2)
    print("")
    print(f"Your monthly repayment will be {monthly_repayment}")



