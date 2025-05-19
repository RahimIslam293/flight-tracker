class FlightData:
    #This class is responsible for structuring the flight data.

    def __init__(self, price,origin_airport,destination_airport, out_date,return_date):
        self.price = price
        self.origin_airport = origin_airport
        self.destination_airport = destination_airport
        self.out_date = out_date
        self.return_date = return_date


def find_cheapest_flight(flight_data):
    if flight_data is None or flight_data["meta"]["count"] == 0:
        return FlightData("N/A","N/A", "N/A","N/A","N/A")

    first_flight = flight_data["data"][0]
    cheapest_price = float(flight_data["data"][0]["price"]["grandTotal"])
    origin = first_flight["itineraries"][0]["segments"][0]["departure"]["iataCode"]
    destination = first_flight["itineraries"][0]["segments"][0]["arrival"]["iataCode"]
    out_date = first_flight["itineraries"][0]["segments"][0]["departure"]["at"].split("T")[0]
    return_date = first_flight["itineraries"][1]["segments"][0]["departure"]["at"].split("T")[0]
    for flights in flight_data["data"]:
        price = float(flights["price"]["grandTotal"])
        if price < cheapest_price:
            cheapest_price = price
            origin = flights["itineraries"][0]["segments"][0]["departure"]["iataCode"]
            destination = flights["itineraries"][0]["segments"][0]["arrival"]["iataCode"]
            out_date = flights["itineraries"][0]["segments"][0]["departure"]["at"].split("T")[0]
            return_date = flights["itineraries"][1]["segments"][0]["departure"]["at"].split("T")[0]
    cheapest_flight = FlightData(cheapest_price,origin,destination,out_date,return_date)
    print(f"Cheapest Flight from {cheapest_flight.origin_airport} to {cheapest_flight.destination_airport} is ${cheapest_flight.price}\n"
          f"Departure Date: {cheapest_flight.out_date} Return Date: {cheapest_flight.return_date} ")
    return cheapest_flight

    print(cheapest_price)
    return cheapest_price

