import unittest

from python.geocode import geocode

class TestGeocode(unittest.TestCase):
    def setUp(self):
        pass

    def test_get_coord(self):
        coords = geocode.code('2200 Kraft Drive Blacksburg VA')
        self.assertTrue(isinstance(coords, dict))
        self.assertTrue('latitude' in coords)
        self.assertTrue('longitude' in coords)

    def test_throw_exception(self):
        with self.assertRaises(geocode.GeocodeException) as context:
            geocode.code("")

        self.assertEqual('No valid address was given', context.exception.args[0])

        with self.assertRaises(geocode.GeocodeException) as context:
            geocode.code(1)

        self.assertEqual('No valid address was given', context.exception.args[0])

        with self.assertRaises(geocode.GeocodeException) as context:
            geocode.code('zzzz')

        self.assertEqual('Sorry no results found', context.exception.args[0])


if __name__ == '__main__':
    unittest.main()