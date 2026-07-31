class Notification:
    def send(self):
        return "Notification sent"


class EmailNotification(Notification):
    def send(self):
        return "Email sent"  # Inheritance makes this an override.


print(EmailNotification().send())
