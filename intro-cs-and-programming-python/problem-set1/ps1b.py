# Write a program to calculate how many months it will take you to save up enough money for a down
# payment. You will want your main variables to be floats, so you should cast user inputs to floats.
# Implement raise every 6 months;
total_cost = float(input("Enter total cost of dream house: "));
annual_salary = float(input('Enter your annual salary: '));
portion_saved = float(input("Percent of salary to save as decimal (IE 0.1): "));
semi_annual_raise = float(input("Enter semi annual raise amount: "));

portion_down_payment = 0.25;
current_savings = 0;

r = 0.04;

downpayment = total_cost * portion_down_payment;
months_to_save = 0;

while (downpayment - current_savings > 0):
  current_savings += ((annual_salary / 12) * portion_saved) + (current_savings * r)/12;
  months_to_save += 1;
  if months_to_save % 6 == 0:
    annual_salary += (annual_salary * semi_annual_raise);

print("Number of months:", months_to_save);