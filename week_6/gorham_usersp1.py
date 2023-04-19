#======================================
# Title: gorham_usersp1.py 
# Author: Chris Gorham
# Date: 19 Apr 2023
# Description: This is the code for Exercise 6.3, connecting MongoDB with Python
# Sources Used:  WEB335 Python Guide
#=====================================

# imports the Mongo Client
from pymongo import MongoClient

# builds a connection string with the user name / database name / password for our database
client = MongoClient("mongodb+srv://web335_user:s3cret@bellevueuniversity.up6klva.mongodb.net/web335DBretryWrites=true&w=majority")

db = client["web335DB"]

print(client)


print("Here is a list of all documents in the users collection:")
# displays all documents in the user's collection
for user in db.users.find({}, {"firstName": 1, "lastName": 1}):
    print(user)

print("Here is a document for employeeId 1011:")
# displays a document where the employeeId is 1011
print(db.users.find_one({"employeeId": "1011"}))

print("Here is a document where the last name is Mozart:")
# displays a document where the lastName is Mozart
print(db.users.find_one({"lastName": "Mozart"}))


