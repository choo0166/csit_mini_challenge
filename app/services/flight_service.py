from .db import database
from utils.date_formatter import format_date
from werkzeug.exceptions import BadRequest


def get_cheapest_return_flights(args):
    """
    Returns a list of cheapest return flights,
    given the destination city, departure date
    and return date.

    :param argparse.namespace args: Dictionary of arguments.
    :return: List of records.
    :rtype: list[dict]
    """
    dest_city = args['destination']
    departure_date, return_date = args['departureDate'], args['returnDate']
    departure_dt = format_date(departure_date)
    return_dt = format_date(return_date)

    if departure_dt > return_dt:
        raise BadRequest(
            "Invalid date arguments. The departure date cannot be later than return date.")

    pipeline = [
        {"$match": {"srccountry": "Singapore"}},
        {"$match": {"destcity": args['destination']}},
        {"$match": {"date": departure_dt}},
        {"$match": {"stop": 0}},
        {"$lookup": {
            "from": "flights",
            "let": {"ddestcity": "$destcity", "dsrccountry": "$srccountry"},
            "pipeline": [
                {"$match": {
                    "$expr": {
                        "$and": [
                            {"$eq": ["$srccity", "$$ddestcity"]},
                            {"$eq": ["$destcountry",
                                     "$$dsrccountry"]},
                            {"$eq": ["$date", return_dt]}
                        ]
                    }
                }},
                {"$sort": {"price": 1}},
                {"$project": {"_id": 0}}
            ],
            "as": "returnFlights"
        }}
    ]
    result = list(database.flights.aggregate(pipeline))

    response = []
    for dflight in result:
        record = {
            "City": dest_city,
            "Departure Date": departure_date,
            "Departure Airline": dflight.get("airlinename", "NA"),
            "Departure Price": dflight.get("price", "NA"),
        }
        min_price = None
        for rflight in dflight["returnFlights"]:
            price = rflight["price"]
            if min_price is None:
                min_price = price

            if price > min_price:
                break

            new = record.copy()
            new["Return Date"] = return_date
            new["Return Airline"] = rflight.get("airlinename", "NA")
            new["Return Price"] = price

            response.append(new)

    return response
