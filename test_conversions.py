import unittest
import conversions
import conversions_refactored as converts

class ConversionTestCase(unittest.TestCase):
    

    def test_for_CelsiusTOFahrenheit(self):
        self.assertEqual(conversions.convertCelsiusTOFahrenheit(300), 572.0, "Should be 572.0")
    def test_for_CelsiusTOKelvin(self):
        self.assertEqual(conversions.convertCelsiusTOKelvin(300), 573.15, "Should be 573.15")
        
    def test_for_FahrenheitToCelsius(self):
        self.assertEqual(conversions.convertFahrenheitToCelsius(300), 148.88888888888889, "Should be 148.88888888888889")
    def test_for_FahrenheitToKelvin(self):
        self.assertEqual(conversions.convertFahrenheitToKelvin(300), 422.03888888888895, "Should be 422.03888888888895")
        
    def test_for_KelvinToCelsius(self):
        self.assertEqual(conversions.convertKelvinToCelsius(300), 26.850000000000023, "Should be 26.850000000000023")
    def test_for_KelvinToFahrenheit(self):
        self.assertEqual(conversions.convertKelvinToFahrenheit(300), 80.32999999999998, "Should be 80.32999999999998")        


    # convert distance

    def test_meters_to_miles(self):
        self.assertEqual(converts.convert("Meters","Miles",10), .00621)

    def test_meters_to_yards(self):
        self.assertEqual(converts.convert("Meters","Yards",10), 10.9361)    
    
    def test_miles_to_meters(self):
        self.assertEqual(converts.convert("Miles","Meters",10), 16093.44)

    def test_miles_to_yards(self):
        self.assertEqual(converts.convert("Miles","Yards",10), 17600)
        
    def test_yards_to_miles(self):
        self.assertEqual(converts.convert("Yards","Miles",10), 0.005681)

    def test_yards_to_meters(self):
        self.assertEqual(converts.convert("Yards","Meters",10), 9.144)

    def test_itself_unit(self):
        self.assertEqual(converts.convert("Meters","Meters",15), 15)

    # def test_itself_unit(self):
    #     self.assertEqual(converts.convert("Yards","Yards",25), 15)

    # def test_itself_unit(self):
    #     self.assertEqual(converts.convert("Miles","Miles",100), 1005)

if __name__ == "__main__":
    unittest.main()