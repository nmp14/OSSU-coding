#calc how much needed to save per month to get down payment in 3 years.
semiAnnualRaise = 0.07;
r = 0.04;
houseCost = 1000000;
downPayment = .25 * houseCost;
monthsToSave = 36;
annualSalary = float(input("Enter salary: "));


def calcSavingsIn3Years(portion_saved):
  current_savings = 0;
  currentMonths = 0;
  semi_annual_raise = 0.07;
  portion_saved = portion_saved / 10000;
  annual_salary = annualSalary;

  while (currentMonths < 36):
    current_savings += ((annual_salary / 12) * portion_saved) + (current_savings * r)/12;
    currentMonths += 1;
    if currentMonths % 6 == 0:
      annual_salary += (annual_salary * semi_annual_raise);
  return current_savings;

high = 10000;
low = 0;

if calcSavingsIn3Years(10000) < downPayment - 100:
  print('Not possible to save');
  exit(0);

steps = 0;

while (True):
  middle = int((high + low) / 2);
  middleSavings = calcSavingsIn3Years(middle);
  if (downPayment - 100 < middleSavings) and (downPayment + 100 > middleSavings):
    print('Best savings rate:', middle / 10000);
    print('Steps:', steps);
    break;

  if middleSavings < downPayment - 100:
    low = middle;
    steps += 1
  elif middleSavings > downPayment + 100:
    high = middle;
    steps += 1;
  else:
    print('Best savings rate:', middle / 10000);
    print('Steps: ', steps);
    break;