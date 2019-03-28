import sqlalchemy as db
import json
from pprint import pprint


from config import username

DATABASE_URI = f'postgres+psycopg2://{username}:@localhost:5432/slack'
engine = db.create_engine(DATABASE_URI)
connection = engine.connect()
metadata = db.MetaData()

messages = db.Table ('messages', metadata, autoload=True, autoload_with=engine)

with open ('db.json', 'r') as my_data:
    #now you want to do something with this file object
    list_of_dict = json.load(my_data)


for message in list_of_dict:
    if 'comments' in message:
        del message['comments']

for message in list_of_dict:
    if 'description' not in message:
        message['description'] = "None"

query = db.insert(messages)
connection.execute(query, list_of_dict)
