from Utilities import ShipmentsUtility


class ODPair:
    def __init__(self, awb, origin, destination_):
        self.awb = awb
        self.origin = origin
        self.destination = destination_

    def get_estimated_delivery_time(self):
        hubs = []
        path = ""
        estimated_delivery_time = 0

        hubs.append(self.destination)
        destination_hub, travel_time = ShipmentsUtility.find_destination_hub_and_leg_travel_time(self.destination)
        estimated_delivery_time += travel_time
        hubs.append(destination_hub)

        while destination_hub != self.origin:
            destination_hub, travel_time = ShipmentsUtility.find_previous_hub_and_travel_time(destination_hub)
            estimated_delivery_time += travel_time
            hubs.append(destination_hub)

        hubs.reverse()

        if hubs[0] == self.origin:
            for hub in hubs[0:-1]:
                path = path+hub + " -> "
            path = path + hubs[-1] + " "
            edd = "Total Estimated Delivery Duration is: " + str(int(estimated_delivery_time.__round__(0))) + " hours and "\
                  + str(int(((estimated_delivery_time * 100 % 100) / 100 * 60).__round__(2))) + " minutes"
        else:
            path = "path not available"
            edd = "Can't be determined"
        return path, edd
