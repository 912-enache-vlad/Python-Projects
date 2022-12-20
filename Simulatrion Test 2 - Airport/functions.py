

def add_flight(flights, code, duration, departure_city, destination_city):
    '''
    The function add a given flight to the flights list
    :param flights: the flights list
    :param code: the code of the given flights
    :param duration: the duration of the given flights
    :param departure_city: the departure_city of the given flights
    :param destination_city: the destination_city of the given flights
    :return: the flights list modified
    '''

    new_flight = {"code": code,"duration": duration, "departure_city": departure_city, "destination_city": destination_city}
    flights.append(new_flight)
    return flights

def test_add_flight():
    flights = []
    flights_modified = []
    flight1 = {"code": "0B3002", "duration": 45, "departure_city": "Cluj-Napoca", "destination_city": "London"}
    flights.append(flight1)
    flights_modified.append(flight1)
    flight2 = {"code": "0B3003", "duration": 35, "departure_city": "Bucharest", "destination_city": "London"}
    flights.append(flight2)
    flights_modified.append(flight2)
    new_flight = {"code": "0B3004", "duration": 76, "departure_city": "Iasi", "destination_city": "London"}
    flights_modified.append(new_flight)

    assert flights_modified == add_flight(flights, new_flight["code"], new_flight["duration"], new_flight["departure_city"], new_flight["destination_city"])\


def modify_flight(flights, code, new_duration):

    for i in range(len(flights)):
        if flights[i]["code"] == code:
            flights[i]["duration"] = new_duration
            return flights

    return flights

def reroute_flights(flights, initial_destination_city, new_destination_city):

    for i in range(len(flights)):
        if flights[i]["destination_city"] == initial_destination_city:
            flights[i]["destination_city"] = new_destination_city

    return flights

def flight_to_str(flight):
    return f" -= flight with code {flight['code']} have the duration {flight['duration']}, the departure city {flight['departure_city']} and the destination city {flight['destination_city']}\n"

def show_flights(flights, departure_city):

    which_flights = []
    show_str = ""

    # finding the flights with the departure city
    for i in range(len(flights)):
        if flights[i]['departure_city'] == departure_city:
            which_flights.append(flights[i])

    # sorting
    for i in range(len(which_flights) - 1) :
        for j in range(i+1, len(which_flights)):
            if which_flights[i]["duration"] > which_flights[j]["duration"]:
                which_flights[i], which_flights[j] = which_flights[j], which_flights[i]

    #building the string
    for i in range(len(which_flights)):
        show_str += flight_to_str(which_flights[i])

    return show_str
