#Set items are unordered, unchangeable, and do not allow duplicate values.
thisset = {"apple", "banana", "cherry", "apple"}
print(thisset)
print(len(thisset))
print(type(thisset))
#access of set
#You cannot access items in a set by referring to an index or a key.
thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)

#add element
thisset = {"apple", "banana", "cherry"}

thisset.add("orange")

print(thisset)

thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]

thisset.update(mylist)

print(thisset)

#removing element
thisset.remove("kiwi")#remove raise error if element is not found 
print(thisset)
thisset.discard("banana")
print(thisset)#disard does not raise error if element is not found


x = thisset.pop()#pop
print(x)
print(thisset)

thisset.clear()
print(thisset)

del thisset


#join set
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)#union returns a new set which has element of both set
print(set3)

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.intersection_update(y)
print(x)#The intersection_update() method will keep only the items that are present in both sets.

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z=x.intersection(y) #intersection retruns 
print(z)

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.symmetric_difference_update(y)#The symmetric_difference_update() method will keep only the elements that are NOT present in both sets.
print(x)


x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z=x.symmetric_difference(y)#The symmetric_difference() method will return a new set, that contains only the elements that are NOT present in both sets.
print(z)






