from .db import database
from utils.date_formatter import format_date
from werkzeug.exceptions import BadRequest


def get_cheapest_hotels(args):
    """
    Returns a list of cheapest hotel bookings,
    given the check-in date, check-out date and
    destination city.

    :param argparse.namespace args: Dictionary of arguments.
    :return: List of records.
    :rtype: list[dict]
    """
    dest_city = args['destination']
    checkin_date, checkout_date = args['checkInDate'], args['checkOutDate']
    checkin_dt = format_date(checkin_date)
    checkout_dt = format_date(checkout_date)

    if checkin_dt > checkout_dt:
        raise BadRequest(
            "Invalid date arguments. The check-in date cannot be later than check-out date.")

    pipeline = [
        {"$match": {"city": dest_city}},
        {"$match": {"date": checkin_dt}},
        {"$project": {
            "_id": 0,
            "City": "$city",
            "Hotel": "$hotelName",
            "Price": {"$min": "$price"},
            "Check In Date": checkin_date,
            "Check Out Date": checkout_date
        }},
        {"$sort": {"Price": 1}}
    ]
    result = list(database.hotels.aggregate(pipeline))

    response = []
    min_price = None
    for doc in result:
        price = doc["Price"]
        if min_price is None:
            min_price = price

        if price > min_price:
            break
        response.append(doc)

    return response
