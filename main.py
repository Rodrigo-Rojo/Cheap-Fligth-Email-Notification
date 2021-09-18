from data_manager import DataManager
import time
from flight_search import FlightSearch
from notification_manager import NotificationManager
flight_search = FlightSearch()
data_manager = DataManager(flight_search)
notification_manager = NotificationManager(flight_search)
sent = False
while not sent:
    try:
        data_manager.create_data()
        notification_manager.sent_sms()
    except Exception as e:
        print(e)
        time.sleep(5)
    else:
        sent = True
