from datetime import datetime
import unittest

from calendar import *
from event import *


class CalendarTest(unittest.TestCase):
    def test_calendar_receives_a_name(self):
        name = 'John Doe'
        cal = Calendar(name)

        assert cal.name == name

    def test_calendar_hold_events(self):
        ev = Event('lunch',
            datetime(2012, 3, 19, 12, 0),
            datetime(2012, 3, 19, 14, 0))

        cal = Calendar('John')
        cal.add(ev)

        assert ev in cal.events

    def test_calendar_detect_conflicts(self):
        ev = Event('lunch',
            datetime(2012, 3, 19, 12, 0),
            datetime(2012, 3, 19, 14, 0))

        ev2 = Event('boring meeting',
            datetime(2012, 3, 19, 13, 0),
            datetime(2012, 3, 19, 14, 0))

        cal = Calendar('John')
        cal.add(ev)
        cal.add(ev2)

        assert cal.conflicts() == True

if __name__ == "__main__":
    unittest.main()
