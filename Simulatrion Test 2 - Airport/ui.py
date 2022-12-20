
from functions import *

def start():
    #having 6 flights hard coded
    flights = []
    flight1 = {"code": "0B3002", "duration": 45, "departure_city": "Cluj-Napoca", "destination_city": "London"}
    flights.append(flight1)
    flight2 = {"code": "0B3003", "duration": 35, "departure_city": "Bucharest", "destination_city": "London"}
    flights.append(flight2)
    flight3 = {"code": "0B3004", "duration": 76, "departure_city": "Iasi", "destination_city": "London"}
    flights.append(flight3)
    flight4 = {"code": "0B3005", "duration": 89, "departure_city": "Cluj-Napoca", "destination_city": "Berlin"}
    flights.append(flight4)
    flight5 = {"code": "0B3006", "duration": 57, "departure_city": "Bacau", "destination_city": "Vienna"}
    flights.append(flight5)
    flight6 = {"code": "0B3007", "duration": 68, "departure_city": "Madrid", "destination_city": "Berlin"}
    flights.append(flight6)

    while True:
        option = input("""
        
        1 - add a flight
        2 - modify the duration of a given flight
        3 - reroute a destination city with a new one
        4 - show all flight having a given departure city sorted increasing by their duration
        
        """)
        if option == '1':
            # getting the input
            print("Regarding the flight introduce the following:")
            code = input("code = ")
            duration = int(input("duration = "))
            departure_city = input("departure_city = ")
            destination_city = input("destination city = ")

            #validating the input
            if len(code) < 3 or len(departure_city) < 3 or len(destination_city) < 3 or duration < 20:
                print("Invalid input.")
                continue

            # calling the add flight function
            flights = add_flight(flights, code, duration, departure_city, destination_city)

        elif option == '2':
            # getting the input
            code = input("Enter the code of the flight:")
            new_duration = int(input("Enter the new duration:"))

            # calling the modify_flight function
            flights = modify_flight(flights, code, new_duration)
        elif option == '3':
            # getting the input
            initial_destination_city = input("Enter the initial_destination_city: ")
            new_destination_city = input("Enter the new_destination_city: ")

            # validating the input
            if len(initial_destination_city) < 3 or len(new_destination_city) < 3:
                print("Invalid input.")
                continue

            # calling the reroute_flights functions
            flights = reroute_flights(flights, initial_destination_city, new_destination_city)

        elif option == '4':
            # calling the show_flights functions
            departure_city = input("Enter the departure city:")
            print(show_flights(flights, departure_city))

test_add_flight()
start()
