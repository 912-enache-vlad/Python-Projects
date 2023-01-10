from domain import Taxi_Station
from repository import TaxiStationTextRepo


class UI:
    def __init__(self):
        self.__repo = TaxiStationTextRepo()

    def __call__(self):


        while True:
            choice = input("""
            1 - Add an new address
            2 - Display all addresses
            3 - What addresses have distance at most <d>
            4 - Determine best address for a new station
            """)
            if choice == "1":
                try:
                    id = int(input("id: "))

                    #veryfing uniqueness
                    if self.__repo.existing_id(id) == True:
                        raise ValueError("The id already exits!")

                    #positive integer
                    if id < 0 or int(id) is not id:
                        raise ValueError("The id should be a positive integer!")

                    name = input("name: ")

                    #at least 3 characters
                    if len(name) < 3:
                        raise ValueError("The name should have at least 3 characters!")

                    number = int(input("number: "))

                    #positive integer
                    if number < 0 or int(number) is not number or number > 100:
                        raise ValueError("The number should be a positive integer of at most 100!")

                    x = int(input("x: "))
                    y = int(input("y: "))
                    # <= 100 and >= -100
                    if x > 100 or y > 100 or x < -100 or y < -100:
                        raise ValueError("x and y should be between -100 and 100!")

                    #adding the new station
                    new_station = Taxi_Station(id, name, number, x, y)
                    self.__repo.add_address(new_station)

                except ValueError as ve:
                    print(ve)

            elif choice == "2":
                print(self.__repo.display_all_addresses())

            elif choice == "3":
                try:
                    x = int(input("x:"))
                    y = int(input("y:"))
                    d = int(input("d:"))
                    print(self.__repo.determine_addresses(x, y, d))
                except ValueError as ve:
                    print(ve)

            elif choice == "4":
                newX, newY = self.__repo.best_address()
                print(f"newX = {newX}, newY = {newY}")






