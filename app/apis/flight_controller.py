from flask_restx import Resource, Namespace, reqparse
from services.flight_service import get_cheapest_return_flights

ns = Namespace('flight', description='flight related requests.')

# flight request parser
flight_get_request_parser = reqparse.RequestParser()
flight_get_request_parser.add_argument('departureDate', required=True,
                                       type=str, location="args")
flight_get_request_parser.add_argument('returnDate', required=True,
                                       type=str, location="args")
flight_get_request_parser.add_argument('destination', required=True,
                                       type=str, location="args")


@ns.route('')
class flight(Resource):
    @ns.doc('Returns a list of cheapest return flights given departure date, return date and destination city.')
    @ns.expect(flight_get_request_parser)
    def get(self):
        args = flight_get_request_parser.parse_args()
        print(f"Args: {args}")
        try:
            response = get_cheapest_return_flights(args)
            return response,  200, {'Content-Type': 'application/json'}
        except Exception as err:
            return {"error": str(err)}, 400, {'Content-Type': 'application/json'}
