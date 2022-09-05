from turtle import heading


class man:
    def __init__(self,name,hieght,weight,colour):
        self.name=name
        self.hieght=hieght
        self.colour=colour 
    def print_name(self):
        print("my name is",self.name )
    def print_hieght(self):
        print(self.name,"hieght is",self.hieght )
    def print_colour(self):
        print(self.name,"colour is",self.colour )
    def print_weight(self):
        print(self.name,"weight is",self.weight )
ram=man("ram",5.7,56,"white")
ram.colour="black"
ram.print_colour()
        
