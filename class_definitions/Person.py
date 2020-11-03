""" Person class using property"""


class Person:
    """Person class"""
    TITLES = ("Dr", "Mr", "Mrs", "Ms")

    def __init__(self, title, name='Derek'):         # Constructor
        self.title = title
        self.name = name
        print("Starting my constructor")

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        if value not in self.TITLES:
            raise ValueError("%s is not a valid title" % value)
        self._title = value

    @property  # getter
    def name(self):
        print("Getting my name....")
        return self._name

    @name.setter
    def name(self, value):
        if value.isdigit():
            raise ValueError
        print("Setting my name....")
        self._name = value


# Driver
try:
    person = Person("Mr.", "Derek")
except ValueError as err:
    print(err)
else:
    print(person.title + " " + person.name)



