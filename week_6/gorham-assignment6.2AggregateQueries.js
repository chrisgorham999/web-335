/*
    Title: gorham-assignment6.2AggregateQueries.js
    Author: Chris Gorham
    Date: 17 Apr 2023
    Description: WEB335 Assignment 6.2 Aggregate Queries
    Sources Used: 
    WEB335 mongosh Guide
    WEB335 MongoDB Query Guide 
    MongoDB Write Scripts Documentation, url: https://www.mongodb.com/docs/mongodb-shell/write-scripts/
 */

    // Query One
    // pulls all documents from the houses collection
    db.houses.find()

    // Query Two
    // pulls all documents in the students collection
    db.students.find()

    // Query Three
    // assigns student data to the variable student
    student = {"firstName": "Chris", "lastName": "Gorham", "studentId": "s9999", "houseId": "h1009"}
    // inserts the data from the variable user into the database as a new document
    db.students.insertOne(student)
    // to verify it made it to the database, we use the findOne using the firstName 
    db.students.findOne({"lastName": "Gorham"}) 

    // Query Four
    // We already had the _id from the previous query so now we just need to do the delete one command
    db.students.deleteOne({"_id": ObjectId("643dd74bb8cb7f49e518a70e")})
    // To prove this was deleted we can run the same findOne we used previously and it will return a null value
    db.students.findOne({"lastName": "Gorham"}) 

    // Query Five
    // this query aggregates students by house id in the houses collection
    db.houses.aggregate([ {$lookup: { from: "students", localField: "houseId", foreignField: "houseId", as: "students_in_house"}}])

    // Query Six
    // this query aggregates students that match the Gryffindor founder name
    db.houses.aggregate([ {$match: { "founder": "Godric Gryffindor"}}, { $lookup: { from: "students", localField: "houseId", foreignField: "houseId", as: "students_in_house"}}])

    // Query Seven
    // this query aggregates students that match a house that has the mascot of an Eagle
    db.houses.aggregate([ {$match: { "mascot": "Eagle"}}, { $lookup: { from: "students", localField: "houseId", foreignField: "houseId", as: "students_in_house"}}])
