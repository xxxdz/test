class Animal:
    def __init__(self, name):
        self.name = name
    def speak(self):
        print('Hello ' + self.name)
class Dog(Animal):
    def __init__(self, age:str,name:str):
        super().__init__(name)
        self.age=age
    def speak(self):
        print(f'I am Dog{self.name}')
class Cat(Animal):
    def __init__(self, age:str,name:str):
        super().__init__(name)
        self.age=age
    def speak(self):
        super().speak()
        print(f'I am Cat{self.name}')
    def __str__(self):
        return f'I am Cat{self.name}'
def speak(animal:Animal,animal2):
    animal.speak()
    print(animal.name)
    animal=animal2
    animal.speak()
    print(animal.name)
    print(animal.age)
if __name__ == '__main__':
    speak(animal=Animal("ani"),animal2=Dog(20,"dog"))
