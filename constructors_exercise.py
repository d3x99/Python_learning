class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def talk(self):
        return f"hi, I am {self.first_name} {self.last_name}"

    def talk_ext(self):
        return f"{self.talk()} nice to meet you"


person1 = Person('Bartek', 'Słodyczka')
print(person1.talk())
print(person1.talk_ext())
