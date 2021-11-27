#Operators are used to perform operations on variables and values.
#Arithmetic operators
a = 20
b = 10
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a//b)
print(a%b)
print(a**b)
#Comparison operator
print(a==b)
print(a<b)
print(a>b)
print(a<=b)
print(a>=b)
print(a!=b)
#Assignment Operators
a+=b
print(a)
a-=b
print(a)
a*=b
print(a)
a%=b
print(a)
a//=b
print(a)
#Bitwise Operators
a=10
b=20
print(bin(a)[2:])
print(bin(b)[2:])
print(bin(a&b)[2:])
print(bin(a|b)[2:])
print(bin(a^b)[2:])
print(bin(~a)[3:])
print(bin(a<<2)[2:])
print(bin(a>>2)[2:])
#boolean
print(True and True)
print(False and True)
print(1 == 1 and 2 == 1)
print("love" == "love")
print(1 == 1 or 2 != 1)
print(True and 1 == 1)
print(False and 0 != 0)
print(True or 1 == 1)
print("time" == "money")
print(1 != 0 and 2 == 1)
print("I Can't Believe It's Not Butter!" != "butter")
print("one" == 1)
print(not (True and False))
print(not (1 == 1 and 0 != 1))
print(not (10 == 1 or 1000 == 1000))
print(not (1 != 10 or 3 == 4))
print(not ("love" == "love" and "time" == "money"))
print(1 == 1 and (not ("one" == 1 or 1 == 0)))
print("chunky" == "bacon" and (not (3 == 4 or 3 == 3)))
print(3 == 3 and (not ("love" == "love" or "Python" == "Fun")))