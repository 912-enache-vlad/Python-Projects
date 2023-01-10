from domain import Taxi_Station


class TaxiStationTextRepo:
    def __init__(self):
        self.__file = "stations.txt"
        self.__stations = []
        self.load_file()

    def __len__(self):
        return len(self.__stations)

    def load_file(self):
        with open(self.__file, "r") as fin:
            for line in fin:
                tokens = line.split(",")
                id = tokens[0].strip()
                name = tokens[1].strip()
                number = tokens[2].strip()
                x = tokens[3].strip()
                y = tokens[4].strip()
                station = Taxi_Station(id, name, number, x, y)
                self.__stations.append(station)

    def save_file(self):
        with open(self.__file, "w") as fout:
            for station in self.__stations:
                fout.write(str(station))
                fout.write("\n")

    def display_all_addresses(self):
        string = ""
        for station in self.__stations:
            string += str(station) + "\n"
        return string

    def add_address(self, new_address:Taxi_Station):
        self.__stations.append(new_address)
        self.save_file()

    def existing_id(self, new_id):
        for station in self.__stations:
            if new_id == station.id:
                return True
        return False

    def determine_addresses(self, x, y, d):
        """
        The function determine the addresses that have the distance from x,y at most d
        :param x: The x coordonate
        :param y: The y coordonate
        :param d: The d coordonate
        :return: string with all the addresses
        """
        string = ""
        for station in self.__stations:
            if ((station.x - x)**2 + (station.y - y)**2)**1/2 <= d:
                string += str(station)

        return string

    # def test_determine_addresses(self):

    def best_address(self):
        sumX = 0
        sumY = 0
        for station in self.__stations:
            sumX += station.x
            sumY += station.y

        newX = sumX // len(self.__stations)
        newY = sumY // len(self.__stations)

        return newX, newY

if __name__ == "__main__":
    taxi_stations = TaxiStationTextRepo()

    station_address = Taxi_Station(11, "Titulescu", 10, 11, 13)
    taxi_stations.add_address(station_address)
    print(taxi_stations.display_all_addresses())
