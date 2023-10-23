class Animal:
    def speak(self):
        print("animal speaking")
class Dog(Animal):
    def bark(self):
        print("dog barks")
dog =Dog()
dog.bark()
dog.bark()
class Dogchild(Dog):
    def eats(self):
        print("drinks milk")
dogmdogo=Dogchild()#this is object 2
dogmdogo.speak()
dogmdogo.eats()
dogmdogo.bark()