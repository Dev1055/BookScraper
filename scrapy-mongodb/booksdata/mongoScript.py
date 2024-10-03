from pymongo import MongoClient
import datetime 
import urllib 

mongo_uri = "mongodb+srv://Dev1055:" + urllib.parse.quote("Dev@mongodb1055") + "@cluster0.fdqneml.mongodb.net/"

client = MongoClient(mongo_uri)
 
db = client.scrapy
posts = db.test_collection

post = {
    "author": "Mike",
    "text": "My first blog post!",
    "tags": ["mongodb", "python", "pymongo"],
    "date": datetime.datetime.now(tz=datetime.timezone.utc),
}

post_id = posts.insert_one(post).inserted_id