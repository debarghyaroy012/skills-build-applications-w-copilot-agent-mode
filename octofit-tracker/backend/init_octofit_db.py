from pymongo import MongoClient

# Connect to the MongoDB server
client = MongoClient("mongodb://localhost:27017/")

# Initialize the database
db = client["octofit_db"]

# Create collections
collections = ["users", "teams", "activity", "leaderboard", "workouts"]
for collection in collections:
    db.create_collection(collection)

# Set up a unique index for the users collection
db["users"].create_index("email", unique=True)

# List all collections to verify
print("Collections in octofit_db:", db.list_collection_names())

# Close the connection
client.close()
