# """Initialize name, age, and breed information."""
#         """Introduce the dog."""
#         """Say Woof!"""
#         """Celebrate the dog's birthday and update the age attribute."""
#         """Check the dog's mood."""
import random

class Cat:
        def __init__(self, name, age, breed, is_kitten):
                self.name = name
                self.age = age
                self.breed = breed
                self.is_kitten = is_kitten

        def introduce(self):
                """Introducing the cat."""
                if self.is_kitten == False:
                    print(f"{self.name} is a {self.breed} cat, and is {self.age} years old.")
                else:
                    print(f"{self.name} is a {self.breed} kitten, and is {self.age} years old.")

        def meow(self):
                """Cat is meowing"""
                print(f"Meow!, says {self.name}")

        def celebrate_bday(self):
                if self.is_kitten == True:
                    print(f"Hooray! It is {self.name}'s birthday!")
                    self.age == 1
                else:
                    print(f"Hooray! It is {self.name}'s birthday!")
                    self.age += 1
                print(f"{self.name} is now {self.age} years old.")

        def mood_check(self):
                """Check on the cat's mood"""
                mood = random.choice("sad", "grumpy", "sleepy")
                print(f"{self.name} is {mood}.")
                if mood == "sad":
                    self.meow()
                elif mood == "happy":
                    self.growl()
                else:
                    print("Zzzz...")

        def growl(self):
                """Cat is GRRRing"""
                print("Grrr...")
        
sesame = Cat("Sesame", 2, "Siberian", False)
miso = Cat("Miso", 0.5, "Siberian", False)

sesame.introduce()     # EXPECTED: Sesame is a 2 year old Siberian.
miso.introduce()