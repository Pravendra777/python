answer = input("Do you want to hear a joke? ")
if answer.lower() == "yes":
    print("I'm against picketing, but I don't know how to show it.")
elif answer.lower() == "no":
    print("Fine.")
else:
    print("I don't understand.")

#nested if else
x = 41

if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")