from django.test import TestCase
from .models import Cuve
from station.models import Station
from django.contrib.auth.models import User

class CuveModelTestCase(TestCase):
    def setUp(self):
        # Create a User instance for id_users in Station
        user = User.objects.create(
            username="test_user",
            password="test_password",  # You should set a secure password
            # Add other fields as needed
        )

        # Create a Station instance
        station = Station.objects.create(
            libelle="Your Station Name",
            location="Your Station Location",
            id_users=user,
            Nmbr_cuves=3,  # Adjust these values as needed
            Nmbr_pompes=2,
            Nmbr_pompistes=5,
        )

        # Use the created Station instance when creating a Cuve
        self.cuve = Cuve.objects.create(
            Nb_pmp_alimente=2,
            charge=100.00,
            stocke=50.00,
            Qt_min=10.00,
            id_station=station,  # Associate the Cuve with the Station
        )

    def test_cuve_str(self):
        expected_str = f"Cuve {self.cuve.id} at Your Station Name"
        self.assertEqual(str(self.cuve), expected_str)
