import pymongo

connection = pymongo.MongoClient("149.89.150.100")

db = connection['test']			
collection = db['restaurants']		


def bur(place):
	print "All the places in "+place
	temp = collection.find({'borough':place})

	for each in temp:
		print each['name']

def zip(z):
	temp = collection.find({'address.zipcode':str(z)})

	for each in temp:
		print each['name']

def zipgrade(z,g):
	temp = collection.find({'address.zipcode':str(z),"grades.grade":g})
	for each in temp:
		print each['name']

def zipscore(z,s):
	temp = collection.find({'address.zipcode':str(z),"grades.score":{'$lt' : s}})
	for each in temp:
		print each['name']



#bur("Brooklyn")
#zip(10002)
#zipgrade(10002,"A")
zipscore(10002,15)