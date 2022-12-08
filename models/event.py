class Event():
    def __init__(self, date, name, capacity, location, description, recurring):
        self.date = date
        self.name = name
        self.capacity = capacity
        self.location = location
        self.description = description
        self.recurring = recurring
        
    def find_event(self, name, list_of_events):
        for event in list_of_events:
            if event.name == name:
                return event
            
        