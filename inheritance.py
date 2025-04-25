class animal:
    def __init__(self,name):
        self.name = name
    
    def speak(self):
        print(f"{self.name} creates sound")
    
    def idli(self):
        print("this is single idli")


    
    

animal1 =animal("Dog")
animal1.speak()
animal1.idli()

class dog(animal):
    def speak(self):
        print(f"{self.name} barks")
    
    def idli(self):
        print(f"{self.name} eats idli")
        


Dog = dog("Dog")
Dog.speak()
Dog.idli()

    
