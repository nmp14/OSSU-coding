####################
## EXAMPLE: while loops 
## Try expanding this code to show a sad face if you go right
## twice and flip the table any more times than that. 
## Hint: use a counter
####################
countRight = 0;
n = input("You are in the Lost Forest\n****************\n****************\n :)\n****************\n****************\nGo left or right? ")
while n == "right" or n == "Right":
  countRight += 1;
  if countRight > 2:
    n = input("You are in the Lost Forest\n****************\n******       ***\n  (╯°□°）╯︵ ┻━┻\n****************\n****************\nGo left or right? ")
  elif countRight == 2:
    n = input("You are in the Lost Forest\n****************\n******       ***\n  😞  \n****************\n****************\nGo left or right? ")
  else:
    n = input("You are in the Lost Forest\n****************\n******       ***\n  \n****************\n****************\nGo left or right? ")

print("\nYou got out of the Lost Forest!\n\o/")