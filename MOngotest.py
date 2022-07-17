import pymongo
client = pymongo.MongoClient("mongodb+srv://JBC007:Jagjeet123@stark.jpadz.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

d = {
    "name": "jagjeet",
    "email" :"jagjeet.chawda@gmail.com",
    "surname": "Chawda"
}

db1 = client['MOngotest']
coll = db1['test']
coll.insert_one(d )
