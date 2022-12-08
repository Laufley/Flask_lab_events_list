from models.event import Event
import datetime


event1_day = datetime.date(2022, 12, 31) #output: 2022-12-31
event2_day = datetime.date(2023, 1, 6)
event_1 = Event(event1_day, "Hogmanay Ball", 200, "Assembly Rooms", "Ceilidh to celebrate the start of 2023!!", False)
event_2 = Event(event2_day, "Dia de los Reyes Magos", 20, "home with family", "Don't forget to feed the camels", True)

all_events = [event_1, event_2]