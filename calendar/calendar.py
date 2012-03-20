class Calendar(object):
    def __init__(self, name):
        self.name = name
        self.events = {}

    def add(self, event):
        year = event.start.year
        month = event.start.month
        day = event.start.day

        if year not in self.events:
            self.events[year] = {}

        if month not in self.events[year]:
            self.events[year][month] = {}

        if day not in self.events[year][month]:
            self.events[year][month][day] = []

        self.events[year][month][day].append(event)

    def conflicts(self):
        for year in self.events.values():
            for month in year.values():
                for day in month.values():
                    for event in day:
                        for other_event in day:
                            if (event != other_event and
                                event.conflicts(other_event)):
                                return True
