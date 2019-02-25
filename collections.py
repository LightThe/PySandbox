print("In this file i'll be developing some collections\n")

#According to W3schools, there's four collection types in python
# Lists, Tuples, Sets and Dictionaries
#The first one is the list
#works just like dynamic linked lists in C or Haskell

strList = ["Item 1", "Item2", "Well this is boring"]
#printing the whole list is easy
print("Here, have a list:\n"+str(strList))

#remember: list indexes start at ZERO
print("I can access just one item, "+str(strList[2]))

#deleting the whole list
del strList

print("now let's iterate over the list");
#starting an empty list
newList = []
#for(x=0;x<4;x++), python is cleaner
for x in range(4):
	#append adds another element to the list
	newList.append(input("Index "+str(x)+": "))
print("i think we're done:\n"+str(newList))

#Tuples are lists that can't change after creation "tuple = ("item1", "item2")"
#Sets are unindexed lists (don't have predef order or indexes) "set = {"item1", "item2")"

#Dictionaries, unordered, changeable and indexed. They have keys and values
newDict = {
	"key1": "value1",
	"name": "Clawdyo",
	"Usage": "30%",
	"randomInt": 32,
	"thisIsList": newList
}

print("I built a dictionary, it has keys and values.\nWe're printing only keys:")
for key in newDict:
	#printing newDict[key] prints the values
	print(key)

print("\nbut it can do cool pattern matching too")
#newDict.values() searches only the values
#newDict.keys() serches only the keys
for key, val in newDict.items():
	print("Key: "+str(key)+"\tValue: "+str(val))
print("\nwould you LOOK AT THIS THING")

print("\nNow let's update some stuff")
#OLHA PRA ESSE IF MARAVILHOSO
if "name" in newDict:
	print("I don't think your name is really @"+newDict["name"]+" can you tell me your name again?")
	newDict["name"] = input("Type it on... ")
	print("Okay @"+newDict["name"]+" now it's registered")
print("\nthis is it, i need to get some usecases to use the collections and remember a little more")
