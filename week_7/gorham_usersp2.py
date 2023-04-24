#======================================
# Title: gorham_usersp2.py 
# Author: Chris Gorham
# Date: 24 Apr 2023
# Description: This is the code for Exercise 7.3, connecting MongoDB with Python part 2
# Sources Used:  WEB335 Python Guide
#=====================================

# imports the Mongo Client
from pymongo import MongoClient
import datetime

# builds a connection string with the user name / database name / password for our database
client = MongoClient("mongodb+srv://web335_user:s3cret@bellevueuniversity.up6klva.mongodb.net/web335DB?retryWrites=true&w=majority")

db = client["web335DB"]

print(client)


#creates a new user document by assigning the fields to a variable
new = {
    "firstName": "Megan",
    "lastName": "Gorham",
    "employeeId": "9233",
    "email": "megangorham@outlook.com",
    "dateCreated": datetime.datetime.utcnow()
}

#inserts the document into the users collection
new_user_id = db.users.insert_one(new).inserted_id
print(new_user_id)

#prove the insert worked
print(db.users.find_one({"employeeId": "9233"}))

#creates an update query to change the user's email address
db.users.update_one(
    {"employeeId": "9233"},
    {
        "$set": {
            "email":"newemail@newemail.com"
        }
    }
)

#prove the email was updated
print(db.users.find_one({"employeeId": "9233"}))


#builds a query to remove a user document
result = db.users.delete_one({
    "employeeId": "9233"
})

#display the result of the query
print(result)

#prove the delete worked
print(db.users.find_one({"employeeId": "9233"}))
