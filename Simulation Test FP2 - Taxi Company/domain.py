
class Taxi_Station:
    def __init__(self, id, name, number, x, y):
        self.__id = id
        self.__name = name
        self.__number = number
        self.__x = x
        self.__y = y

    #====for id====
    @property
    def id(self):
        return self.__id

    #====for name=====
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        self.__name = new_name

    #====for number====
    @property
    def number(self):
        return self.__number

    @number.setter
    def number(self, new_number):
        self.__number = new_number

    #====for x====
    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, new_x):
        self.__x = new_x

    # ====for y====
    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, new_y):
        self.__y = new_y

    def __str__(self):
        return f"{self.id}, {self.name}, {self.number}, {self.x}, {self.y}"

