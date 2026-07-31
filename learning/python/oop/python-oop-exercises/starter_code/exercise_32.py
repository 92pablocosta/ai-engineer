class EmailChannel:
    def send(self, message):
        pass


class LogChannel:
    def send(self, message):
        pass


class NotificationService:
    def send_all(self, message, channels):
        pass


# TODO: send Welcome to both channels and handle an empty message.
