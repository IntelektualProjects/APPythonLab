class Person:

    # Constructor Function is the init one

    def __init__(self, name):
        self.name = name

    def talk(self):
        print(f"Hi, I am {self.name}")


person = Person("John")
print(person.name)

bob = Person("Bob Smith")
bob.talk()