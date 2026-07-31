class Alarm:
    def ring(self):
        return "alarm"


class LoudAlarm(Alarm):
    pass  # TODO: fully replace ring.


class LoggedAlarm(Alarm):
    pass  # TODO: extend ring without using super().


# TODO: print both overridden behaviors.
