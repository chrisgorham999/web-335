/*
    Title: gorham-assignment5.2projections.js
    Author: Chris Gorham
    Date: 12 Apr 2023
    Description: WEB335 Assignment 5.2 Queries
    Sources Used: 
    WEB335 mongosh Guide
    WEB335 MongoDB Query Guide 
    MongoDB Write Srcripts Documentation, url: https://www.mongodb.com/docs/mongodb-shell/write-scripts/
 */

    // Query One
    // assigns user data to the variable user
    user = {"firstName": "Chris", "lastName": "Gorham", "employeeId": "9999", "email": "chris.gorham@outlook.com", "dateCreated": new Date()}
    // inserts the data from the variable user into the database as a new document
    db.users.insertOne(user)
    // to verify it made it to the database, we use the findOne using the firstName 
    db.users.findOne({"firstName": "Chris"})

    // Query Two
    // The first thing we have to do is lookup Mozart's Object ID so that we can update his email. We'll use the find() function.
    db.users.findOne({"lastName": "Mozart"})
    // We will use the updateOne function to update the email address
    db.users.updateOne({"_id": ObjectId("643756cc608ec1b2ca8b77c9")}, {$set:{"email": "mozart@me.com"}})
    // We will double check to make sure it was updated by using the same findOne from earlier
    db.users.findOne({"lastName": "Mozart"})

    // Query Three
    // finds all users and then uses projections to only display the firstName, lastName, and email fields.
    db.users.find({},{"firstName": 1, "lastName": 1, "email": 1})