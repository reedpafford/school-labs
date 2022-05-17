class Employee:
    def __init__(self,name,ID,department,title):
        self.__name=name
        self.__IDNumber=ID
        self.__department=department
        self.__title=title

    def getID(self):
            return self.__IDNumber

    def display(self):
        print('Name: {}'.format(self.__name))
        print('ID Number: {}'.format(self.__IDNumber))
        print('Department: {}'.format(self.__department))
        print('Title: {}'.format(self.__title))
