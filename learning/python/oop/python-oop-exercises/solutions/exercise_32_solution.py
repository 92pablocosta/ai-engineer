class EmailChannel:
    def send(self, message):
        return f"email: {message}"


class LogChannel:
    def send(self, message):
        return f"log: {message}"


class NotificationService:
    def send_all(self, message, channels):
        if not message:
            raise ValueError("message cannot be empty")
        return [channel.send(message) for channel in channels]


service = NotificationService()
for result in service.send_all("Welcome", [EmailChannel(), LogChannel()]):
    print(result)
try:
    service.send_all("", [EmailChannel()])
except ValueError:
    # Each channel's informal contract is send(message).
    print("empty message: ValueError")
