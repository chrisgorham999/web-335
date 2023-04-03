/*
    Title: gorham-assignment4mongodbshell.js
    Author: Chris Gorham
    Date: 3 Apr 2023
    Description: WEB335 Assignment 4 Queries
    Sources Used: 
    WEB335 mongosh Guide
    WEB335 MongoDB Query Guide 
    MongoDB Write Srcripts Documentation, url: https://www.mongodb.com/docs/mongodb-shell/write-scripts/
 */

    // displays all documents in the user's collection
    db.users.find()

    // searches the users for an email that matches the input (jbach@me.com)
    db.users.find({"email": "jbach@me.com"})

    // searches the users for a user with the last name that matches the input (Mozart)
    db.users.find({"lastName": "Mozart"})

    // searches the users for a user with the first name that matches the input (Richard)
    db.users.find({"firstName": "Richard"})

    // searches the users for a user with the employeeId that matches the input (1010)
    db.users.find({"employeeId": "1010"})
