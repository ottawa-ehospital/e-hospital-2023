# pip3 install pymongo
from pymongo import MongoClient
import gridfs

# Connect to the server with the hostName and portNumber.
connection = MongoClient("mongodb+srv://admin:admin@e-hospital.mgq2xgp.mongodb.net/test")

# Connect to the Database where the images will be stored.
database = connection['mldata']

# Create an object of GridFs for the above database.
fs = gridfs.GridFS(database,"pneumonia_database") # change the name to your collection

i = 0
# Retrieve all file under the collection
for grid_out in fs.find({"filename": "image.jpeg"}): # change the name to your identifiable file name
    print(f"Retrieve file in index {i}")
    i += 1
    file = grid_out.read()

    # Write data to the current directory
    f = open(f'image{i}.jpeg', 'wb')
    f.write(file)
    f.close()
