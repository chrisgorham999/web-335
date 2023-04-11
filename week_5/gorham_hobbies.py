#======================================
# Title: gorham_hobbies.py 
# Author: Chris Gorham
# Date: 11 Apr 2023
# Description: This is the code for the Python Conditionals, Lists, and Loops Exercise (Exercise 5.3)
# Sources Used:  
#=====================================

#creates a list of hobbies
hobbies_list = ["running", "guitar", "movies", "music", "woodworking"]

#iterates over the list of hobbies and prints each one
for x in hobbies_list:
    print(x)

#creates a list of days
days_list = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

#iterates over the list of days and prints a message for each day through an if, elif, else statement
for x in days_list:
        if x == "Saturday":
            print("Today is Saturday and it is an off day - time to enjoy some hobbies.")
        elif x == "Sunday":
            print("Today is Sunday and it is an off day - time to enjoy some hobbies.")
        elif x == "Monday":
            print("Today is Monday and it is a work day.")
        elif x == "Tuesday":
            print("Today is Tuesday and it is a work day.")
        elif x == "Wednesday":
            print("Today is Wednesday and it is a work day.")
        elif x == "Thursday":
            print("Today is Thursday and it is a work day.")
        elif x == "Friday":
            print("Today is Friday and it is a work day.")
        else:
            print("No days left.")