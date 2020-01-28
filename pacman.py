from pymongo import MongoClient
# pprint library is used to make the output look more pretty
from pprint import pprint
# connect to MongoDB, change the << MONGODB URL >> to reflect your own connection string
client = MongoClient()
db=client["euroleaguebasket"]
# Issue the serverStatus command and print the results
player = db.jugadores

print("What do you want do?\n1.-Insert Data \n2.-Search by name\n3.-Search by team\n")
number = input()
if int(number) == 1:
    print("Player name")
    name=input()
    print("Team name")
    team=input()
    probar={"player":name,"team":team}
    insertplayer=player.insert_one(probar)
elif int(number) == 2:
    print("Put player name")
    name = input()
    query = {"player": name}
    result = player.find(query);
    for x in result:
        print(x)
elif int(number) == 3:
    print("Put player team")
    name = input()
    query = {"team": name}
    result = player.find(query);
    for x in result:
        print(x)