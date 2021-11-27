#Lists are used to store multiple items in a single variable.
people = ["Mattan", "Chris", "Sarah"]
print(people)
print(type(people))
print(len(people))
#access of element
print("fisrt element",people[0])
print("last element",people[-1])
print("reverse",people[::-1])
#add element
people.append("kamal")
people.append("Nitin")
print(people)
people[2]=[["blackcurrant", "watermelon"]]
print(people)
people.insert(2, "ama")
print(people)
people2=["nike","ken","john"]
people.extend(people2)
print(people)
#removing element
people.remove("ama")#Remove Specified Item
print(people)
people.pop(3)#remove element of a particular index
print(people)
people.clear()#remove all element of list or we can use del people also to remove all element
print(people)
