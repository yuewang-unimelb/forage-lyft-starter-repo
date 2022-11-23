import unittest
from tire.octoprime_tire import OctoprimeTire

class TestOctoprimeTires(unittest.TestCase):
    def test_needs_service_true(self):
        tire_wear = [0.0, 1.0, 1.0, 1.0]
        tires = OctoprimeTire(tire_wear)
        self.assertTrue(tires.needs_service())

    def test_needs_service_false(self):
        tire_wear = [0.0, 1.0, 1.0, 0.9]
        tires = OctoprimeTire(tire_wear)
        self.assertFalse(tires.needs_service())