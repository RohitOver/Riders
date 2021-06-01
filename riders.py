import json

def Input_to_rider(filename):
	f = open (filename, "r")
	input = f.read()
	f.close()
	st = 0  #find index of "{"
	for i in range(len(input)):
		if(input[i] == "{"):
			st = i
			break
	identifier = input[1:st-4]
	input = input[st:]
	rider = json.loads(input)  #rider is a dictionary
	return (identifier,rider)

class riders:

	def __init__(self):
		self.riderlist = {}

	def Display_keys(self):
		print("\nAll keys in riders :")
		for key in self.riderlist:
			print(key)

	def Show_value(self):
		print("\nEnter key to get value :")
		key = input()
		print("\nRider info for key",key,"is :")
		for i in self.riderlist[key]:
			print(i,"->",self.riderlist[key][i])

	def Auto_populate(self,filename):
		identifier,new_rider = Input_to_rider(filename)
		if identifier in self.riderlist.keys():
			print("Rider's info already exists")
		else:
			self.riderlist[identifier] = new_rider

directory = []  #directory can be appended externally(later)
directory.append("rider_1.txt")
directory.append("rider_2.txt")

db = riders()  #db is object of type riders
for s in directory:
	db.Auto_populate(s)

while(1):
	print("\n-Press 1 to display all keys")
	print("-Press 2 to get rider details for particular key")
	print("-Press any other char. to exit")
	user = input("-")
	if(user == '1'):
		db.Display_keys()
	elif(user == '2'):
		db.Show_value()
	else:
		break



