class ShipmentHaulLine:
    def __init__(self, frm, to, origin, destination, std, sta, path, leg_travel_time):
        self.origin = origin
        self.destination = destination
        self.std = std
        self.sta = sta
        self.path = path
        self.frm = frm
        self.to = to
        self.leg_travel_time = leg_travel_time


