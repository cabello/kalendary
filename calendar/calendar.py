class Calendar(object):
    def __init__(self, name):
        self.name = name
        self.events = []

    def add(self, event):
        self.events.append(event)

    def conflicts(self):
        for event in self.events:
            for other_event in self.events:
                if (event != other_event and
                    event.conflicts(other_event)):
                    return True
