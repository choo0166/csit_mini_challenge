from flask_restx import Resource, Namespace, reqparse
from services.hotel_service import get_cheapest_hotels

ns = Namespace('hotel', description='hotel related requests.')

# hotel request parser
hotel_get_request_parser = reqparse.RequestParser()
hotel_get_request_parser.add_argument('checkInDate', required=True,
                                      type=str, location="args")
hotel_get_request_parser.add_argument('checkOutDate', required=True,
                                      type=str, location="args")
hotel_get_request_parser.add_argument('destination', required=True,
                                      type=str, location="args")


@ns.route('')
class hotel(Resource):
    @ns.doc('Search cheapest hotel bookings given check-in date, check-out date and destination city.')
    @ns.expect(hotel_get_request_parser)
    def get(self):
        args = hotel_get_request_parser.parse_args()
        print(f"Args: {args}")
        try:
            response = get_cheapest_hotels(args)
            return response,  200, {'Content-Type': 'application/json'}
        except Exception as err:
            return {"error": str(err)}, 400, {'Content-Type': 'application/json'}
