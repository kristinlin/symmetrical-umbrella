'''
JUNGLERABBITS
Eric Li, Kristin Lin

DATASET: Scottish Parliament Events
HYPERLINK: https://data.parliament.scot/api/events
SUMMARY: Our json file is opened, parsed, and conveniently converted into a list of dictionaries. We ran the mongo function insert_many() with the list of dictionaries as the input to import our json data into our database.
'''

import pymongo, json, datetime

#connect to the database and collection; create if nonexisted
connection = pymongo.MongoClient("149.89.150.100")
db = connection['junglerabbits']                 
collection = db['events'] 

#returns True--empty; needs to insert
def check():
    found = collection.find({'ID': 1})
    if found.count() == 0:
        return True
    return False

#insert data into collection from json file
def insert(j_file):
    if check():
        j_file = open(j_file, 'r')	
        data = json.loads( j_file.read() )
        collection.insert_many(data)
        j_file.close()
    else:
        print "Database is filled already."


#==================================================================
# FORMATTING


#Prints data nice
def prettyPrint(x):
	#without id
	retStr = x['Date']+"\n"+x['Title']+"\n"+x['Sponsor']+"\n"
	print retStr.encode('utf-8')



#gets the date from the string
# 0 = year
# 1 = month
# 2 = day
def getDate(date,type):
	year = int(date[:4])
	month = int(date[5:7])
	day = int(date[8:10])

	if type == 0:
		return year
	elif type == 1:
		return month
	elif type == 2:
		return day


#==================================================================
# START OF SEARCH FUNCS


#if you wanted to get by ID for some reason
def getID(id):
	temp = collection.find({'ID':id})
	for each in temp:
		prettyPrint(each)

# find by year
def getYear(y):
    st = str(y) + "-01-01T00:00:00"
    end = str(y+1) + "-01-01T00:00:00"
    temp = collection.find({'Date': {'$gte' : st, '$lte': end}})
    for each in temp:
	prettyPrint(each)
                
#get by month
def getTimeRange(d1, d2):
    st = d1 + "T00:00:00"
    end = d2 + "T00:00:00"
    temp = collection.find({'Date': {'$gte' : st, '$lte': end}})
    for each in temp:
	prettyPrint(each)
            
def getSponser(name):
	temp = collection.find({"Sponsor":name})
	for each in temp:
		prettyPrint(each)

	name2 = name+" MSP"
	print name2
	temp2 = collection.find({"Sponsor":name2})
	for each in temp2:
		prettyPrint(each)


insert("junglerabbits.json")

print "GET BY ID - 1"
print "======================================================"
getID(1)
print "GET BY YEAR - 2016"
print "======================================================"
getYear(2016)
print "GET BY TIME RANGE - 2015-12-01 to 2015-12-14"
print "======================================================"
getTimeRange("2015-12-01", "2015-12-14")
print "GET BY SPONSOR - Jackie Baillie"
print "======================================================"
getSponser("Jackie Baillie")
