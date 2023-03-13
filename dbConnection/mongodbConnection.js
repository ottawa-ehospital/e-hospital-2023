const { MongoClient } = require('mongodb');

const uri = "mongodb+srv://ehuser:ehuser@e-hospital.mgq2xgp.mongodb.net/?retryWrites=true&w=majority"
const client = new MongoClient(uri);

try {
    // Connect to the MongoDB cluster
    client.connect();
    testConnection();
    // findImageById("files1", "63ec4d0bf7e2456aaff8347c");
} catch (e) {
    console.log('Cannot connect to the Mongo DB server.');
    console.error(e);
}

module.exports = {
    getDb: function () {
      return client.db("htdata");
    }
};

async function testConnection(){
    databasesList = await client.db().admin().listDatabases();
    console.log("Connected to the Mongo Database");
    // databasesList.databases.forEach(db => console.log(` - ${db.name}`));
};

// async function createNewImage(collectionName, image){
//     const result = await client.db("db1").collection(collectionName).insertOne(image);
//     console.log(`New image created with the following id: ${result.insertedId}`);
// }

// async function findImageById(collectionName, id) {
//     var mongo = require('mongodb');
//     var o_id = new mongo.ObjectId(id);

//     const result = await client.db("db1").collection(collectionName).findOne({ _id: o_id });

//     if (result) {
//         console.log(`Found an image in the collection with the id '${id}':`);
//         // console.log(result);
//     } else {
//         console.log(`No image found with the id '${id}'`);
//     }
// }