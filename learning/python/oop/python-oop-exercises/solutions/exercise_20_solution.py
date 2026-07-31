class Alarm:
    def ring(self):
        return "alarm"


class LoudAlarm(Alarm):
    def ring(self):
        return "LOUD ALARM"


class LoggedAlarm(Alarm):
    def ring(self):
        return f"{Alarm.ring(self)}\nlogged"  # Call the known parent explicitly.


print(LoudAlarm().ring())
print(LoggedAlarm().ring())
