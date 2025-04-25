# initiate a class
class employee:
    #special method/magic/dunder - constructor
    def __init__(self):
        self.name="BHavesh"
        self.id="123"
        self.designation="DA"

    def travel(self,destination):
        print(f'The empolyee tarveling through {destination}')


E1=employee()
# print(E1.name)
# E1.travel("Jaypur")

E1.name="Khaple"
print(E1.name)