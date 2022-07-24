import pymongo
client = pymongo.MongoClient("mongodb+srv://mongodb:mongodb@inueron.cu9p8qi.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

d={
    "name" :"Wasim Akram",
    "Email" :"wasim.khan1042@yahoo.com"
}
db1=client["mongotest"]
coll=db1['test']
coll.insert_one(d)