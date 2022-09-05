print("do you want to read or write in file")
ch=input()
if ch=="read":
    my_file=open("a.txt","r")
    my_line=my_file.readlines()
    for i in my_line:
        print(i,end=" ")
elif ch=="write":
    my_file=open("a.txt","w")
    while True:
        print("enter the data")
        data=input()
        my_file.write(data)
        my_file.write("\n")
        print("do you want to continue")
        ch=input()
        if ch=="yes":
            continue
        else:
            break
else:
    print("invalid input")
my_file.close()