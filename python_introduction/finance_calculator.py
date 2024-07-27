Monthly_Income = int(input("enter yoyr monthly income:"))
Monthly_Expenses = int(input("Enter your total monthly expenses:"))

monthly_savings = Monthly_Income - Monthly_Expenses                 #caclculating monthly savings
annual_interest = .05
projected_savings =  monthly_savings * 12 + (monthly_savings * 12 * 0.05)  

print ("the monthly savings will be :",monthly_savings,"$")
print("the projected annual savings will be :",projected_savings,"$")