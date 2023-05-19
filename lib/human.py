class Human:

    species = "Homo sapiens"

    def __init__(self, name):
        self.name = name
        self._age = 20

    def get_age(self):
        print("Retrieving age")
        return self._age

    def set_age(self, age):
        if (type(age) in (int, float)) and (0 <= age <= 120):
            print(f"setting the age to {age}")
            self._age = age
        else:
            print("age must be a number between 0 and 120")

    age = property(get_age, set_age)


markoff = Human("Markoff")
markoff.age = 99
# markoff.age = False
print(markoff.age)
