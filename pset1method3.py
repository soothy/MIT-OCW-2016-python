hi=10000
lo=1
down_payment=250000
annual_salary = float(input("key in annual salary: "))
semi_annual_raise=0.7
current_savings=0
guess=(hi+lo)//2
monthly_salary=annual_salary/12
month=1
tolerance= 100
c=0


def calsavings(current_savings,monthly_salary,guess,month):
    while month !=36:
        monthly_savings = monthly_salary *(guess/10000)
        current_savings +=monthly_savings
        month+=1
    return current_savings

current_savings = calsavings(current_savings,monthly_salary,guess,month)

while True:
    if ((current_savings - down_payment) > tolerance):
        hi = guess-1
        c+=1
        guess=(hi+lo)//2
        current_savings = calsavings(0,monthly_salary,guess,1)
        print("guess is too high... ")
    elif ((down_payment-current_savings) >tolerance):
        lo=guess-1
        c+=1
        guess=(hi+lo)//2
        current_savings = calsavings(0,monthly_salary,guess,1)
        print("guess is too low... ")
    elif ((current_savings - down_payment)<tolerance):
         print("The correct guess is ",guess/100, "%, the amount saved was $",current_savings)
         break
print (c)




