''''Must start with a lowercase letter.
Can have letters, numbers, and underscores (but no spaces).
Should use underscores (instead of spaces). E.g. your_name.  '''


name = "Mattan Griffel"
orphan_fee = 200
teddy_bear_fee = 121.80

total = orphan_fee + teddy_bear_fee

print(name, "the total will be", total)
print(id(teddy_bear_fee)) # return the unique id of the object, thhe id is the object's memory address .