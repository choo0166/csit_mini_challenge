from flask_restx import Api
from .flight_controller import ns as flight_ns
from .hotel_controller import ns as hotel_ns

api = Api(
    title='My Test Api',
    version='1.0',
    description='API for CSIT Mini-challenge.'
    # All API metadatas
)

# Add namespaces
api.add_namespace(flight_ns)
api.add_namespace(hotel_ns)