class Car (object):
    def __init__(self,color) :
        self.color=color

    def showcolor(self):
        print("Yout car color is",self.color)

audi = Car("red")
print(audi.color)
audi.showcolor()