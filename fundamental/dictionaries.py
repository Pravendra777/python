#Dictionaries are used to store data values in key:value pairs.
#Dictionaries cannot have two items with the same key:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)
print(type(thisdict))
print(len(thisdict))

#Accessing Items

print(thisdict["model"])#it'll raise error if the value not present in the dictionory
print(thisdict.get("model"))#it'll return none if value is not present in the dictionory
print(thisdict.keys())#There is also a method called get() that will give you the same result:
print(thisdict.values())#The keys() method will return a list of all the keys in the dictionary.
print(thisdict.items())#he items() method will return each item in a dictionary, as tuples in a list.



#Change Values
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["year"] = 2018
print(thisdict)#the value of year will be 2018 in place of 1964

#add element in dictionory
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["color"] = "red"
print(thisdict)


#delete element
thisdict.pop("model")#delete model form the dictionory
print(thisdict)
thisdict.popitem()#it will remove the last key
print(thisdict)
del thisdict["brand"] 
print(thisdict)
del thisdict #it will remove complete dictionory

#looping
mattan = {'name': 'Mattan', 'height': 70, 'shoe size': 10.5, 'hair': 'Brown', 'eyes': 'Brown'}

chris = {'name': 'Chris', 'height': 68, 'shoe size': 10, 'hair': 'Brown', 'eyes': 'Brown'}

sarah = {'name': 'Sarah', 'height': 72, 'shoe size': 8, 'hair': 'Brown', 'eyes': 'Brown'}
people = [mattan, chris, sarah]

print(people)

for i in mattan:
    print(i,end=" ")
print()
for i in mattan.keys():
    print(i,end=" ")
print()
for i in mattan.values():
    print(i,end=" ")
print()
for i,j in mattan.items():
    print(i,j)
print()

#copy dictionory
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = thisdict.copy()
print(mydict)

for person in people:
    print(person["name"]," has ",person['height'],"hight.")



    
# formkeys
a=[1,2,3,4,5]
b=dict.fromkeys(a)
print(b)

