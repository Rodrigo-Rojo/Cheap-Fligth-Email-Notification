import smtplib
from flight_search import FlightSearch


class NotificationManager:
    def __init__(self, flight_search):
        self.sms = ""
        self.flight_search = flight_search

    def sent_sms(self):
        text_sms = ""
        for text in self.flight_search.get_flight_str():
            text_sms += text
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user="email@gmail.com", password="password")
            connection.sendmail(
                from_addr="email@gmail.com",
                to_addrs="email@hotmail.com",
                msg=f"Subject: Flight Deals\n\n"
                    f"{text_sms}"

            )
        print("Email Sent")