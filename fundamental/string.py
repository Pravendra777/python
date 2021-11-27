# Strings are text surrounded by quotes
# Both single (') or double (") or triple (""") quotes are used
# examples: "dinosaurs", '2112', "I'm lovin' it!"
print("Hello")
print('Hello')

kanye_quote = "my greatest pain in live is that I will never be able to see myself perform live"
print(kanye_quote) 

kanye_quote = """My greatest pain in life  
is that I will never be able
to see myself perform live.""" #use of triple quote
print(kanye_quote)

str1="he is my brother.\nhe is fat.\nhe is 19 years old."#new line using \n
print(str1)

hamilton_quote = "Well, the word got around, they said, \"This kid's insane, man\""
print(hamilton_quote)

#slicing
a = " Hola,Mundo!! "
print(a[0])
print(a[::-1])
print(a[:])
print(a[-8:-1])
#built-in methods
print(a.upper())
print(a.lower())
print(a.strip())
print(a.strip().split(","))
print(a.replace("Mundo", "buenos dias"))
txt = "Mi casa, su casa."
x = txt.rfind("casa")
print(x)
#formating
age=32
sen="he is {} years old."
print(sen.format(age))
print("he is {} brother".format("my"))


