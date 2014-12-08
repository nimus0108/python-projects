class Person (object):
    total_people = 0
    
    def __init__ (self, name, gender):
        Person.total_people += 1
        self.name = name
        self.gender = gender
        self.age = 0

    def celebrate_bday (self):
        self.age += 1

        print(self.name + " is now " + str(self.age) + " years old")

    def talk(self):
        print("Hello, my name is " + self.name + ".")
    
    def __str__ (self):
        return self.name + " " + str(self.age) + " " + self.gender


def main():
    katie = Person ("Katie", "girl")
    timmy = Person ("Timmy", "boy")
    david = Person ("David", "boy")

    print(timmy)
    katie.celebrate_bday()
    timmy.celebrate_bday()

    for i in range (5):
        david.celebrate_bday()

    david.talk()

    print(Person.total_people)
main()
