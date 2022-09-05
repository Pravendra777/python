#Single Inheritance in Python
print("///////////////////////////////","single Inheritance in Python","///////////////////////////////")
class parent:
    def func1(self):
        print("parent func1")
class child(parent):
    def fun2(self):
        print("child func2")
obj=child()
obj.func1()
obj.fun2()
#Multi-Level Inheritance in Python
print("///////////////////////////////","Multi-Level Inheritance in Python","///////////////////////////////")
class parent:
    def func1(self):
        print("parent func1")
class child(parent):
    def fun2(self):
        print("child func2")
class grandchild(child):
    def fun3(self):
        print("grandchild func3")
obj=grandchild()
obj.func1()
obj.fun2()
obj.fun3()
#Multiple Inheritance in Python
print("///////////////////////////////","Multiple Inheritance in Python","///////////////////////////////")
class parent:
    def func1(self):
        print("parent func1")
class child:
    def fun2(self):
        print("child func2")
class grandchild(parent,child):
    def fun3(self):
        print("grandchild func3")
obj=grandchild()
obj.func1()
obj.fun2()
obj.fun3()

print("///////////////////////////////","Hierarchical Inheritance in Python","///////////////////////////////") 
class parent:
    def func1(self):
        print("parent func1")
class child1(parent):
    def fun2(self):
        print("child1 func2")
class child2(parent):
    def fun3(self):
        print("child2 func3")
obj=child1()
obj.func1()
obj.fun2()
obj=child2()
obj.func1()
obj.fun3()
print("///////////////////////////////","Hybrid Inheritance in Python","///////////////////////////////")
 
class parent1:                            # first parent class
    def func1(self):                  
        print("Hello Parent")
 
 
class parent2:                            # second parent class
    def func2(self):                   
        print("Hello Parent")
 
class child1(parent1):                    # first child class
    def func3(self):                   
        print("Hello Child1")
 
 
class child2(child1, parent2):            # second child class
    def func4(self):                   
        print("Hello Child2")   
                               
 
# Driver Code
test1 = child1()                          # object created
test2 = child2()
 
test1.func1()                       # child1 calling parent1 method
test1.func3()                       # child1 calling its own method
 
test2.func1()                       # child2 calling parent1 method
test2.func2()                       # child2 calling parent2 method
test2.func3()                       # child2 calling child1 method
test2.func4()                       # child2 calling its own method
