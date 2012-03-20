from datetime import datetime
import unittest

from event import *


class EventTest(unittest.TestCase):

    def test_event_receives_a_name_and_two_datetimes(self):
        name = 'meeting'
        start = datetime(2012, 3, 19, 18, 0)
        end = datetime(2012, 3, 19, 19, 45)
        ev = Event(name, start, end)

        assert ev.name == name
        assert ev.start == start
        assert ev.end == end

    def new_event(self, start_hour, start_minute, end_hour, end_minute):
        name = 'meeting'
        start = datetime(2012, 3, 19, start_hour, start_minute)
        end = datetime(2012, 3, 19, end_hour, end_minute)
        return Event(name, start, end)

    def test_conflict_is_false(self):
        ev = self.new_event(18, 0, 19, 45)
        ev2 = self.new_event(12, 0, 14, 0)

        assert ev.conflicts(ev2) == False
        assert ev2.conflicts(ev) == False

    def test_conflict_other_event_is_inside_of_event(self):
        name = 'meeting'
        start = datetime(2012, 3, 19, 18, 0)
        end = datetime(2012, 3, 19, 19, 45)
        ev = Event(name, start, end)

        name2 = 'snack'
        start2 = datetime(2012, 3, 19, 18, 30)
        end2 = datetime(2012, 3, 19, 19, 0)
        ev2 = Event(name2, start2, end2)

        assert ev.conflicts(ev2) == True
        assert ev2.conflicts(ev) == True

    def test_conflict_event_is_insideof_other_event(self):
        name = 'meeting'
        start = datetime(2012, 3, 19, 18, 0)
        end = datetime(2012, 3, 19, 19, 45)
        ev = Event(name, start, end)

        name2 = 'snack'
        start2 = datetime(2012, 3, 19, 18, 30)
        end2 = datetime(2012, 3, 19, 19, 0)
        ev2 = Event(name2, start2, end2)

        assert ev.conflicts(ev2) == True
        assert ev2.conflicts(ev) == True

    def test_conflict_other_event_is_leftside_of_event(self):
        name = 'meeting'
        start = datetime(2012, 3, 19, 18, 0)
        end = datetime(2012, 3, 19, 19, 45)
        ev = Event(name, start, end)

        name2 = 'snack'
        start2 = datetime(2012, 3, 19, 17, 30)
        end2 = datetime(2012, 3, 19, 18, 15)
        ev2 = Event(name2, start2, end2)

        assert ev.conflicts(ev2) == True
        assert ev2.conflicts(ev) == True

    def test_conflict_other_event_is_rightside_of_event(self):
        name = 'meeting'
        start = datetime(2012, 3, 19, 18, 0)
        end = datetime(2012, 3, 19, 19, 45)
        ev = Event(name, start, end)

        name2 = 'snack'
        start2 = datetime(2012, 3, 19, 19, 15)
        end2 = datetime(2012, 3, 19, 20, 00)
        ev2 = Event(name2, start2, end2)

        assert ev.conflicts(ev2) == True
        assert ev2.conflicts(ev) == True

    def test_no_conflict_in_following_events(self):
        name = 'meeting'
        start = datetime(2012, 3, 19, 18, 0)
        end = datetime(2012, 3, 19, 18, 30)
        ev = Event(name, start, end)

        name2 = 'meeting 2'
        start2 = datetime(2012, 3, 19, 18, 30)
        end2 = datetime(2012, 3, 19, 19, 00)
        ev2 = Event(name2, start2, end2)

        assert ev.conflicts(ev2) == False
        assert ev2.conflicts(ev) == False

    def test_event_is_equal_if_everything_match(self):
        name = 'meeting'
        start = datetime(2012, 3, 19, 18, 0)
        end = datetime(2012, 3, 19, 18, 30)
        ev = Event(name, start, end)
        ev2 = Event(name, start, end)

        assert ev == ev2

if __name__ == "__main__":
    unittest.main()
