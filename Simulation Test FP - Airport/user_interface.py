
from operations import *


def start():
    flights = []
    #have at least 5 flights hard coded
    flight1 = {"code":"0B3002", "duration": 45, "departure_city": "Cluj-Napoca", "destination_city": "London"}
    flights.append(flight1)
    flight2 = {"code": "0B7902", "duration": 60, "departure_city": "Bucharest", "destination_city": "Berlin"}
    flights.append(flight2)
    flight3 = {"code": "0B3102", "duration": 80, "departure_city": "London", "destination_city": "Bucharest"}
    flights.append(flight3)
    flight4 = {"code": "4B3002", "duration": 95, "departure_city": "Cluj-Napoca", "destination_city": "Viena"}
    flights.append(flight4)
    flight5 = {"code": "0B3322", "duration": 68, "departure_city": "Bucharest", "destination_city": "London"}
    flights.append(flight5)
    flight6 = {"code": "0B4502", "duration": 75, "departure_city": "Cluj-Napoca", "destination_city": "Paris"}
    flights.append(flight6)

    while True:
        option = input("""
        
        1 - add a flight
        2 - modify the duration of a given flight
        3 - change the destination city of all flights having the initial destination city to the new destination city
        4 - show all flights with a given departure city (sorted increasing by their duration)
        
        """)
        if option == '1':
            #getting the input from the user
            print("Enter the following regarding the flight:")
            code = input("code = ")
            try:
                duration = int(input("duration = "))
            except ValueError:
                print("You have not entered a number fot the duration. Please try again.")
                continue
            departure_city = input("departure_city = ")
            destination_city = input("destination_city = ")
            #validating the user input
            if len(code) < 3 or len(destination_city) < 3 or len(departure_city) < 3 or duration < 20:
                print("You enter a too short code, destination_city, departure_city or a duration less than 20 min. Please try again.")
                continue
            flights = add_flight(flights, code, duration, departure_city, destination_city)
        # --------------------------------------------
        elif option == '2':
            code = input("code = ")
            found = False
            for i in range(len(flights)):
                if flights[i]["code"] == code:
                    found = True
                    break
            if found == False:
                print("Invalid code.")
                continue
            try:
                duration = int(input("duration"))
            except ValueError:
                print("You have not entered a number fot the duration. Please try again.")
                continue
            flights = modify_flight(flights, code, duration)
        # --------------------------------------------
        elif option == '3':
            destination_city = input("Enter the initial destination city:")
            new_destination_city = input("Enter the new destination city:")
            if len(destination_city) < 3 or len(new_destination_city) < 3:
                print("At least one of the destination cities are too small. Please try again.")
                continue
            reroute_flights(flights, destination_city, new_destination_city)
        # --------------------------------------------
        elif option == '4':
            departure_city = input("Enter the departure city:")
            print(show_flights_with_given_departure_city(flights, departure_city))



test_add_flight()
start()