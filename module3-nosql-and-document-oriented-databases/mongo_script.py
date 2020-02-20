import os
from dotenv import load_dotenv
import pymongo

load_dotenv()

MONGO_USER = os.getenv('MONGO_USER')
MONGO_PASS = os.getenv('MONGO_PASS')
MONGO_SERVER = os.getenv('MONGO_SERVER')


client = pymongo.MongoClient(f"mongodb+srv://{MONGO_USER}:{MONGO_PASS}@{MONGO_SERVER}/test?retryWrites=true&w=majority")
print('CLIENT:', client)

# create new database
db = client.test
print('DB:', db)

# within database, we create collections
collection = db.titanic
# print(db.list_collection_names())
# print(collection.count_documents())


def write_rows():
    with open('DS-Unit-3-Sprint-2-SQL-and-Databases/module2-sql-for-analysis/titanic.csv') as titanic:
        csvReader = csv.reader(titanic)
        next(csvReader)
        counter = 1
        for row in csvReader:
            passenger = {
                'survived': row[0],
                'pclass': int(row[1]), 
                'name': row[2], 
                'sex': row[3],
                'age': float(row[4]),
                'sib_spouse_count': int(row[5]),
                'parent_child_count': int(row[6]),
                'fare': float(row[7])
            }
            collection.insert_one(passenger)
            counter += 1


'''
print(db.list_collection_names())
print(collection.count_documents())

print("----------------")
db = client.another_test_database
print("DB:", type(db), db)
print("----------------")
print("COLLECTIONS:")
print(db.list_collection_names())
print("----------------")
collection = db.pokemon
print("COLLECTION:", type(collection), collection)
print("----------------")
print("COLLECTIONS:")
print(db.list_collection_names())
print("----------------")
print("SELECT ALL PIKACHUS:")
print(collection.count_documents({}))
print(collection.count_documents({"name": "Pikachu"}))
'''

'''
How was working with MongoDB different from working with PostgreSQL? What was 
easier, and what was harder?

MongoDB is not "relational" like PostgreSQL, but rather stored in documents, or 
"JSON-like" data.

It seems to me to be easier to mentally visualize relational tables, however, 
it also seems a bit easier/more flexible to access MongoDB data.
'''
