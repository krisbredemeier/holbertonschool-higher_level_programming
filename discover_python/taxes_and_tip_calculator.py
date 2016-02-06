import os
#clear the screen
os.system('clear')

"""This is a tip calculator for meals
written by Kris Bredemeier"""

#opeing line
print("Welcome to the taxs and tip calculator!")

#accounts for price of meal
meal = float(raw_input("What is the price before tax? "))

#accounts for tax
tax = float(raw_input("What are the taxes? (in %) "))

#converts tax to decimal
tax = tax / 100

#accoutns for meal, tax included
meal = meal + meal * tax

#accounts for tip
tip = float(raw_input("What do you want to tip? (in %) "))

#converts tip to decimal
tip = tip / 100

#accounts for meal and tip
total = meal + meal * tip

#prints total
print "The price you need to pay is: " +str(total)

#returns screen to terminal
raw_input('Press enter to quit...')

#clear the screen
os.system('clear')

