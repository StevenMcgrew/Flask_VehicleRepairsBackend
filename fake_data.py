"""
Populate vehicle_repairs database with fake data using Faker and the SQLAlchemy ORM.
"""

from faker import Faker
from faker.providers import DynamicProvider
from vehicle_repairs.models.vehicle import Vehicle
from vehicle_repairs.shared_db import db
from vehicle_repairs import create_app

VEHICLE_COUNT = 10000

vehicle_manufacturer_provider = DynamicProvider(
    provider_name="vehicle_make",
    elements=["Acura", "Alfa Romeo", "Aston Martin", "Audi", "Bentley",
            "BMW", "Bugatti", "Buick", "Cadillac", "Chevrolet", "Chrysler",
            "Citroen", "Daewoo", "Daihatsu", "Dodge", "Eagle", "Ferrari",
            "Fiat", "Ford", "Freightliner", "Geo", "GMC", "Honda", "Hummer",
            "Hyundai", "Infiniti", "Isuzu", "Jaguar", "Jeep", "Kia", "Lamborghini",
            "Land Rover", "Lexus", "Lincoln", "Lotus", "Maserati", "Maybach",
            "Mazda", "Mercedes-Benz", "Mercury", "MINI", "Mitsubishi", "Nissan",
            "Oldsmobile", "Opel", "Plymouth", "Pontiac", "Porsche", "Ram",
            "Renault", "Rolls Royce", "Rover", "Saab", "Saturn", "Scion", "Seat",
            "Skoda", "Smart", "Subaru", "Suzuki", "Toyota", "Volkswagen", "Volvo"],
)

def generate_engine_sizes():
    elements = []
    liters = 1.0
    for i in range(74):
        liters += 0.1
        elements.append(str(round(liters,1)) + 'L')
    return elements

vehicle_engine_provider = DynamicProvider(
    provider_name="engine_size",
    elements=generate_engine_sizes()
)

def truncate_tables():
    """Delete all rows from database tables"""
    Vehicle.query.delete()
    db.session.commit()

def main():
    app = create_app()
    app.app_context().push()

    truncate_tables()

    fake = Faker()
    fake.add_provider(vehicle_manufacturer_provider)
    fake.add_provider(vehicle_engine_provider)

    last_vehicle = None  # save last_vehicle
    for _ in range(VEHICLE_COUNT):
        last_vehicle = Vehicle(year=fake.year(),
                               make=fake.vehicle_make(),
                               model=fake.last_name(),
                               engine=fake.engine_size())
        db.session.add(last_vehicle)
    # insert vehicles
    db.session.commit()

# run script
main()
