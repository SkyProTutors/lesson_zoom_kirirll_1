class Animal:
    def __init__(self, specie, age):
        self.__specie = specie
        self.__age = age

    @property
    def specie(self):
        return self.__specie

    @specie.setter
    def specie(self, new_specie):
        if type(new_specie) is str and len(new_specie) <= 7:
            self.__specie = new_specie
        else:
            raise Exception("Неверный формат/слишком много символов")

    @property
    def age(self):
        return self.__age

    def eat(self):
        return f"{self.specie}, кушает 2 раза в день"


# if __name__ == '__main__':
#     an = Animal("Cat", 7)
#     print(an.specie)
#     print(an.age)
#     an.specie = "Dog"
#     print(an.eat())

