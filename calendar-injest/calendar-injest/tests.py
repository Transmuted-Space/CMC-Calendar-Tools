import unittest
from calendar_injest import CalendarInjest


class Tests(unittest.TestCase):
    def setUp(self):
        self.test_instance = CalendarInjest()


    def test_injest_calendar(self):
        self.test_instance.injest_calendar()


if __name__ == '__main__':
    unittest.main()
