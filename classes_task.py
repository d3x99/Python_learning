class Person:
    def __init__(self, name):
        self.name = name

    def talk(self):
        print(f"Hi i'm {self.name}")



person = Person('Bartek')
person.talk()

person2 = Person('Bob')
person2.talk()


