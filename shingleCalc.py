# Author Darrell Pawson
# AppName shingleCalc.py
# This application is designed to help people who dont know how to calculate
# the square footage of a roof and determine how many bundles of shingls and how many rolls of felt will be needed.  Although this script is close it is still for estimation purposes only.

from decimal import *

print "\nThis app is for estimation purposes only."

squarefeet = None
# This loop will ask for user input on the square footage of the house. If no input or no integer input is detected it will display an error and restart the loop.
while True:
    try:
        squarefeet = int(raw_input("\nPlease enter the estimated square feet of your home: "))
        break
    except ValueError:
        print "\nSorry, you must enter a value for this, please try again."

print "\nWhat is your roof pitch?"
print "1) 4 in 12"
print "2) 5 in 12"
print "3) 6 in 12"
print "4) 7 in 12"
print "5) 8 in 12"
print "6) 9 in 12"
print "7) 10 in 12"
print "8) 11 in 12"
print "9) 12 in 12"

pitch = None
# This loop will ask the user for the pitch of the roof based on the options provided above.  Again, if no input or no integer input is detected it will restart the loop.
while True:
    try:
        pitch = int(raw_input("\nPlease enter 1 - 9 based on the pitch of the customers roof: "))
        if pitch in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
            break
    except ValueError:
        print("\nSorry, that was an invalid selection. Please try again.")

if pitch == 1:
    calcsquare = squarefeet * round(1.06, 2)
    square = calcsquare / 100.0
    shinglesNeeded = round(square * 3.0)
    shingles = round(shinglesNeeded, 2)
    fifteenFelt = round(calcsquare / 432) + 1
    thirtyFelt = round(calcsquare / 216) + 1
    print "\nThe actual square footage of the roof is", calcsquare, "and you will need", shingles, "bundles of shingles. \nYou will also need", fifteenFelt, "rolls of #15 felt or", thirtyFelt, "rolls of #30 felt."
elif pitch == 2:
    calcsquare = squarefeet * round(1.08, 2)
    square = round(calcsquare / 100.0)
    shinglesNeeded = round(square * 3.0)
    shingles = round(shinglesNeeded, 2 )
    fifteenFelt = round(calcsquare / 432) + 1
    thirtyFelt = round(calcsquare / 216) + 1
    print "\nThe actual square footage of the roof is", calcsquare, "and you will need", shingles, "bundles of shingles. \nYou will also need", fifteenFelt, "rolls of #15 felt or", thirtyFelt, "rolls of #30 felt."
elif pitch == 3:
    calcsquare = squarefeet * round(1.12, 2)
    square = round(calcsquare / 100.0)
    shinglesNeeded = round(square * 3.0)
    shingles = round(shinglesNeeded, 2 )
    fifteenFelt = round(calcsquare / 432) + 1
    thirtyFelt = round(calcsquare / 216) + 1
    print "\nThe actual square footage of the roof is", calcsquare, "and you will need", shingles, "bundles of shingles. \nYou will also need", fifteenFelt, "rolls of #15 felt or", thirtyFelt, "rolls of #30 felt."
elif pitch == 4:
    calcsquare = squarefeet * round(1.16, 2)
    square = round(calcsquare / 100.0)
    shinglesNeeded = round(square * 3.0)
    shingles = round(shinglesNeeded, 2 )
    fifteenFelt = round(calcsquare / 432) + 1
    thirtyFelt = round(calcsquare / 216) + 1
    print "\nThe actual square footage of the roof is", calcsquare, "and you will need", shingles, "bundles of shingles. \nYou will also need", fifteenFelt, "rolls of #15 felt or", thirtyFelt, "rolls of #30 felt."
elif pitch == 5:
    calcsquare = squarefeet * round(1.20, 2)
    square = round(calcsquare / 100.0)
    shinglesNeeded = round(square * 3.0)
    shingles = round(shinglesNeeded, 2 )
    fifteenFelt = round(calcsquare / 432) + 1
    thirtyFelt = round(calcsquare / 216) + 1
    print "\nThe actual square footage of the roof is", calcsquare, "and you will need", shingles, "bundles of shingles. \nYou will also need", fifteenFelt, "rolls of #15 felt or", thirtyFelt, "rolls of #30 felt."
elif pitch == 6:
    calcsquare = squarefeet * round(1.25, 2)
    square = round(calcsquare / 100.0)
    shinglesNeeded = round(square * 3.0)
    shingles = round(shinglesNeeded, 2 )
    fifteenFelt = round(calcsquare / 432) + 1
    thirtyFelt = round(calcsquare / 216) + 1
    print "\nThe actual square footage of the roof is", calcsquare, "and you will need", shingles, "bundles of shingles. \nYou will also need", fifteenFelt, "rolls of #15 felt or", thirtyFelt, "rolls of #30 felt."
elif pitch == 7:
    calcsquare = squarefeet * round(1.30, 2)
    square = round(calcsquare / 100.0)
    shinglesNeeded = round(square * 3.0)
    shingles = round(shinglesNeeded, 2 )
    fifteenFelt = round(calcsquare / 432) + 1
    thirtyFelt = round(calcsquare / 216) + 1
    print "\nThe actual square footage of the roof is", calcsquare, "and you will need", shingles, "bundles of shingles. \nYou will also need", fifteenFelt, "rolls of #15 felt or", thirtyFelt, "rolls of #30 felt."
elif pitch == 8:
    calcsquare = squarefeet * round(1.36, 2)
    square = round(calcsquare / 100.0)
    shinglesNeeded = round(square * 3.0)
    shingles = round(shinglesNeeded, 2 )
    fifteenFelt = round(calcsquare / 432) + 1
    thirtyFelt = round(calcsquare / 216) + 1
    print "\nThe actual square footage of the roof is", calcsquare, "and you will need", shingles, "bundles of shingles. \nYou will also need", fifteenFelt, "rolls of #15 felt or", thirtyFelt, "rolls of #30 felt."
elif pitch == 9:
    calcsquare = squarefeet * round(1.42, 2)
    square = round(calcsquare / 100.0)
    shinglesNeeded = round(square * 3.0)
    shingles = round(shinglesNeeded, 2 )
    fifteenFelt = round(calcsquare / 432) + 1
    thirtyFelt = round(calcsquare / 216) + 1
    print "\nThe actual square footage of the roof is", calcsquare, "and you will need", shingles, "bundles of shingles. \nYou will also need", fifteenFelt, "rolls of #15 felt or", thirtyFelt, "rolls of #30 felt."
else:
    exit()
