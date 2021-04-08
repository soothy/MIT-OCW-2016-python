
def check_user_input(prompt):
  while True:
      try:
        value=float(input(prompt))
      except ValueError:
          print("Invalid")
      if value < 0:
          print("Please key in a positive number")
      else:
          break
  return value


annual_salary=check_user_input("Annual salary: ")
portion_saved = check_user_input("portion of salary saved per month: ")
total_cost = check_user_input("cost of dream home: ")
semi_annual_raise = check_user_input("semi annual raise: ")

current_savings=0
portion_down_payment = float(0.25 * total_cost)
monthly_savings = float(annual_salary * portion_saved)/12
current_savings = (current_savings * (0.04 / 12)) + monthly_savings + current_savings
i=1

while True:
    if i%6  == 0:
        monthly_savings = monthly_savings * (1 + semi_annual_raise)

    current_savings = (current_savings * (0.04 / 12)) + monthly_savings + current_savings
    i += 1
    if ((portion_down_payment/current_savings) <1 ):
        break

print("Months needed to save",i)

