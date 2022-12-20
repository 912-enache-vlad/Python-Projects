

def add_flight(flights:list, code:str, duration:int, departure_city:str, destination_city:str):
    '''
    The function adds a flight into the list of flights
    @param flights: the list of flights
    @param code: the code of the flight that will be added
    @param duration: the duration of the flight that will be added
    @param departure_city: the departure_city of the flight that will be added
    @param destination_city: the destination_city of the flight that will be added
    @return: the list of flights modified
    '''

    new_flight = {"code": code, "duration": duration, "departure_city": departure_city, "destination_city": destination_city}
    flights.append(new_flight)
    return flights

def test_add_flight():
    flights = []
    flights_modified = []
    # having 2 flights hard coded
    flight1 = {"code": "0B3002", "duration": 45, "departure_city": "Cluj-Napoca", "destination_city": "London"}
    flights.append(flight1)
    flights_modified.append(flight1)
    flight2 = {"code": "0B7902", "duration": 60, "departure_city": "Bucharest", "destination_city": "Berlin"}
    flights.append(flight2)
    flights_modified.append(flight2)
    new_flight = {"code": "0B3102", "duration": 80, "departure_city": "London", "destination_city": "Bucharest"}
    flights_modified.append(new_flight)

    assert flights_modified == add_flight(flights, new_flight["code"], new_flight["duration"], new_flight["departure_city"], new_flight["destination_city"])


def modify_fligt(flights:list, code, new_duration):
    """
    The function modifies a duration of a flight
    @param flights: the list of flights
    @param code: the code of the flight that will be modified
    @param duration: the new duration
    @return: the list of flights modified
    """
    for i in range(len(flights)):
        if flights[i]["code"] == code:
            flights[i]["duration"] = new_duration

    return flights


def test_modify_flight():

    pass


def reroute_flights(flights:list, destination_city:str, new_destination_city:str):
    """
    The function rerout some flights having a destination city with a new one
    @param flights: the list of the flights rerout
    @param destination_city: the initial destination_city
    @param new_destination_city: the new destination_city
    @return: the list of flights modified
    """
    for i in range(len(flights)):
        if flights[i]["destination_city"] == destination_city:
            flights[i]["destination_city"] = new_destination_city
    return flights

def test_reroute_fligths():
    pass


def display_flight(flight:dict):
    return f" -= flight with code {flight['code']} having the duration {flight['duration']} min, the departure city {flight['departure_city']} and the destination city {flight['destination_city']}\n"

def show_flights_with_given_departure_city(flights:list, departure_city:str):
    show_flights = []
    for i in range(len(flights)):
        if flights[i]["departure_city"] == departure_city:
            show_flights.append(flights[i])

    for i in range(len(show_flights) - 1):
        for j in range(i + 1, len(show_flights)):
            if show_flights[i]['duration'] > show_flights[j]['duration']:
                show_flights[i], show_flights[j] = show_flights[j], show_flights[i]

    show_str = ""
    for i in range(len((show_flights))):
        show_str += display_flight(show_flights[i])

    return show_str

# def test_all():
#     flights = []
#     flights_modified = []
#     # having 2 flights hard coded
#     flight1 = {"code": "0B3002", "duration": 45, "departure_city": "Cluj-Napoca", "destination_city": "London"}
#     flights.append(flight1)
#     flights_modified.append(flight1)
#     flight2 = {"code": "0B7902", "duration": 60, "departure_city": "Bucharest", "destination_city": "Berlin"}
#     flights.append(flight2)
#     flights_modified.append(flight1)
#     flight3 = {"code": "0B3102", "duration": 80, "departure_city": "London", "destination_city": "Bucharest"}
#     flights_modified.append(flight3)
#
#     test_add_flight()


# test_all()

