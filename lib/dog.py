#!/usr/bin/env python3

APPROVED_BREEDS = [
    "Mastiff",
    "Chihuahua",
    "Corgi",
    "Shar Pei",
    "Beagle",
    "French Bulldog",
    "Pug",
    "Pointer"
]


class Dog:
    # def __init__(self, name="Rex", breed="Mastiff"):
    #     self.name = name
    #     self.breed = breed

    # def get_name(self):
    #     return self._name

    # def set_name(self, name):
    #     if not isinstance(name, str):
    #         print("Name must be string between 1 and 25 characters.")
    #     elif len(name) < 1 or len(name) > 25:
    #         print("Name must be string between 1 and 25 characters.")
    #     else:
    #         self._name = name.title()

    # name = property(get_name, set_name)

    # def get_breed(self):
    #     return self._breed

    # def set_breed(self, dog_breed):
    #     if dog_breed in APPROVED_BREEDS:
    #         self._breed = dog_breed
    #     else:
    #         print("Breed must be in list of approved breeds.")

    # breed = property(get_breed, set_breed)

    def __init__(self, name="kali", breed="Mastiff"):
        # self.name = name
        self.name = name
        self.breed = breed

    def get_name(self):
        print("Retrieving the number of characters")
        return self._name

    def set_name(self, name,):
        if not isinstance(name, str):
            print("Name must be string between 1 and 25 characters.")

        elif len(name) < 1 or len(name) > 25:
            print("Name must be string between 1 and 25 characters.")

        else:
            self._name = name

    name = property(get_name, set_name)

    def get_breed(self):
        return self._breed

    def set_breed(self, breed):
        if breed in APPROVED_BREEDS:
            self._breed = breed
        else:
            print("Breed must be in list of approved breeds.")

    breed = property(get_breed, set_breed)
