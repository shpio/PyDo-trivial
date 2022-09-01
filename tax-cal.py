income = float(input("Enter the annual income: "))
# relief is a PIT - 18% from income

if income <= 85528:
    tax = round(income / 100 * 18 - 556.02,0)
    if tax <= 0:   
        print("The tax is: 0.0 thalers")
    else:
        print("The tax is:", tax, "thalers")

if income > 85528:
    surplus = income - 85528
# tax for income above 85528 is sum of 14839.2 and 32% of surplus
    tax = round(14839.02 + (surplus / 100 * 32),0)
    if tax <= 0:
        print("The tax is: 0.0 thalers")
    else:        
        print("The tax is:", tax, "thalers" )
