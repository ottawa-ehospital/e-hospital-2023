# pip3 install pymongo
from pymongo import MongoClient
import gridfs
import glob

# Connect to the server with the hostName and portNumber.
connection = MongoClient("mongodb+srv://admin:admin@e-hospital.mgq2xgp.mongodb.net/test")

# Connect to the Database where the images will be stored.
database = connection['mldata']

# Create an object of GridFs for the above database.
fs = gridfs.GridFS(database,"pneumonia_database") # update the collection name to the record type like "BloodTest"

# Scan all .jpeg files in the current directory
filesName = glob.glob("*.jpeg")
# file = "Image_20230215111208.jpeg"

for file in filesName: 
    # Open the image in read-only format.
    with open(file, 'rb') as f:
        contents = f.read()

    # Now store/put the image via GridFs object.
    fs.put(contents, filename="image.jpeg") # update the name to some identifiable like "X-Ray.jpeg"
