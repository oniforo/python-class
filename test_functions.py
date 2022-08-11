import unittest
import functions

class TestFunctions(unittest.TestCase):

    def test_calc_area(self):
        self.assertEqual(functions.calc_area(10, 4), 40)
        self.assertEqual(functions.calc_area(-10, 4), -40)
        self.assertEqual(functions.calc_area(-10.5, -4), 42)
        self.assertEqual(functions.calc_area(10, 0), 0)


    def test_calc_average(self):
        self.assertEqual(functions.calc_average(10, 4), 7)
        self.assertEqual(functions.calc_average(-10, 4), -3)
        self.assertEqual(functions.calc_average(-10.5, -4), -7.25)
        self.assertEqual(functions.calc_average(10, 0), 5)


    def test_seconds_to_hours(self):
        self.assertEqual(functions.seconds_to_hours(0), (0, 0, 0))
        self.assertEqual(functions.seconds_to_hours(3600), (1, 0, 0))
        self.assertEqual(functions.seconds_to_hours(4200), (1, 10, 0))
        self.assertEqual(functions.seconds_to_hours(4250), (1, 10, 50))


    def test_format_hours(self):
        self.assertEqual(
            functions.format_hours(5, 10, 10), 
            "5 hours 10 minutes and 10 seconds")
        self.assertEqual(
            functions.format_hours(0, 10, 10), 
            "10 minutes and 10 seconds")
        self.assertEqual(
            functions.format_hours(0, 0, 10), 
            "10 seconds")


    def test_time_in_days(self):
        self.assertEqual(functions.time_in_days(1, 0, 0), 365)
        self.assertEqual(functions.time_in_days(1, 10, 0), 665)
        self.assertEqual(functions.time_in_days(1, 10, 20), 685)


    def test_calc_weighted_average(self):
        self.assertEqual(
            functions.calc_weighted_average((2, 3, 4)), 
            0)
        self.assertEqual(
            functions.calc_weighted_average((2, 3, 4), (1, 1, 1)), 
            0)
        self.assertEqual(
            functions.calc_weighted_average((2, 3, 4), (5, 3, 2)), 
            0)


    def test_squared_average(self):
        self.assertEqual(functions.squared_average(), 0)
        self.assertEqual(functions.squared_average(), 0)
        self.assertEqual(functions.squared_average(), 0)


    def test_customer_cost(self):
        self.assertEqual(functions.customer_cost(), 0)
        self.assertEqual(functions.customer_cost(), 0)
        self.assertEqual(functions.customer_cost(), 0)


if __name__ == "__main__":
    unittest.main()