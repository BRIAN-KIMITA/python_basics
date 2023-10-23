class fruits:
    def __init__(self,type,price,color):
        self.type=type
        self.price = price
        self.color =color
    def show(self):
        print(f"i like eating {self.type} and it costs {self.price} color being {self.color}")
        #creating objects
myobj= fruits("banana","20 ksh","yellow")

myobj2= fruits("mangoes","50 ksh","red")
myobj.show()
myobj2.show()