import pymongo

#connect to the database and collection
connection = pymongo.MongoClient("149.89.150.100")
db = connection['test']			
collection = db['restaurants']		


#All restaurants in a specified borough.
def bur(place):
	temp = collection.find({'borough':place})
	for each in temp:
		print each['name'].encode('utf-8')

                
#All restaurants in a specified zip code.
def zip(z):
	temp = collection.find({'address.zipcode':str(z)})
	for each in temp:
		print each['name'].encode('utf-8')


#All restaurants in a specified zip code and with a specified grade.
def zipgrade(z,g):
	temp = collection.find({'address.zipcode':str(z),"grades.grade":g})
	for each in temp:
		print each['name'].encode('utf-8')

                
#All restaurants in a zip code with a score below a specified threshold.
def zipscore(z,s):
	temp = collection.find({'address.zipcode' : str(z),
                                "grades.score" : {'$lt' : s}})
	for each in temp:
		print each['name'].encode('utf-8')

#All restaurants on your block by using building number
def restaddr(num, street):
        temp = []
        for block in range(num-10, num+10) :
                rest = collection.find_one({'address.building':str(block),
                                            'address.street':str(street)})
                if (rest is not None):
                        temp.append(rest)
        for each in temp :
                print each['name'].encode('utf-8')



print "\nTESTING BOROUGH(M) RESTAURANTS"
print "=========================================="
bur("Manhattan")
print "\nTESTING ZIPCODE(10002) RESTAURANTS"
print "=========================================="
zip(10002)
print "\nTESTING ZIPCODE(10002) AND GRADE(A) RESTAURANTS"
print "=========================================="
zipgrade(10002,"A")
print "\nTESTING ZIPCODE(10002) AND SCORE(15) RESTAURANTS"
print "=========================================="
zipscore(10002,15)
print "\nTESTING BLOCK(123 Chambers) RESTAURANTS"
print "=========================================="
restaddr(123, "Chambrs Street")
