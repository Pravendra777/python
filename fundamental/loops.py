'''
Python has two primitive loop commands:
while loops
for loops
'''
#while loop
i = 1#we can execute a set of statements as long as a condition is true
while i < 6:
  print(i)
  i += 1
#for loop
#we can execute a set of statements, once for each item in a list, tuple, set etc
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
for i in "he is my brother":
    if i!=" ":
        print(i,end="")
for x in range(6):
  print(x)
for x in range(2, 30, 3):
  print(x)
#nested for loop
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)

