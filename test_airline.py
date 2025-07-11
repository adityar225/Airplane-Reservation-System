import unittest
from seats_utils import create_initial_seat_map, book_seats, cancel_seats

class TestAirlineBooking(unittest.TestCase):
    def setUp(self):
        # Run before every test
        self.seat_map = create_initial_seat_map()

    # test for BOOK A2 2
    def test_valid_booking(self):
        result = book_seats(self.seat_map, "A", 2, 2
        self.assertEqual(result, "SUCCESS")

    # test for BOOK A0 2
    def test_double_booking(self):
        book_seats(self.seat_map, "A", 0, 2)
        result = book_seats(self.seat_map, "A", 0, 2)

        self.assertEqual(result, "FAIL")

    # test for BOOK B1 2
    def test_valid_cancellation(self):
        book_seats(self.seat_map, "B", 1, 2)
        result = cancel_seats(self.seat_map, "B", 1, 2)

        self.assertEqual(result, "SUCCESS")

    # test for BOOK C3 2
    def test_invalid_cancellation(self):
        result = cancel_seats(self.seat_map, "C", 3, 2)
        self.assertEqual(result, "FAIL")

    # test for BOOK D7 2
    def test_out_of_bounds_booking(self):
        result = book_seats(self.seat_map, "D", 7, 2)  # seat 7 + 2 goes out of range
        self.assertEqual(result, "FAIL")

if __name__ == '__main__':
    unittest.main()
