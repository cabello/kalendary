class Event(object):
    def __init__(self, name, start, end):
        self.name = name
        self.start = start
        self.end = end

    def conflicts(self, other_event):
        # If other_event is inside of event
        if (self.start < other_event.start and
            self.end > other_event.end):
            return True

        # If event is inside of other_event
        if (other_event.start < self.start and
            other_event.end > self.end):
            return True

        # If other_event is leftside of event
        if (other_event.end > self.start and
            other_event.end < self.end):
            return True

        # If other_event is rightside of event
        if (other_event.start > self.start and
            other_event.start < self.end):
            return True

        return False
