import ShipmentsUtility


class ODPair:
    def __init__(self, awb, origin, destination_):
        self.awb = awb
        self.origin = origin
        self.destination = destination_

    def get_estimated_delivery_time(self):
        path = []
        haul_line_shipments = ShipmentsUtility.create_shipments_haul_line()
        milk_run_shipments = ShipmentsUtility.create_shipments_milk_run()
        estimated_delivery_time = 0

        path.append(self.destination)

        destination_hub, travel_time = ShipmentsUtility.find_destination_hub_and_leg_travel_time(milk_run_shipments,
                                                                                                 self.destination)
        estimated_delivery_time += travel_time  # 0.83

        path.append(destination_hub)

        while destination_hub != self.origin:
            destination_hub, travel_time = ShipmentsUtility.find_previous_hub_and_travel_time(haul_line_shipments,
                                                                                              destination_hub)
            estimated_delivery_time += travel_time
            path.append(destination_hub)

        path.reverse()

        if path[0] == self.origin:
            for hub in path[0:-1]:
                print(hub, end=" -> ")
            print(path[-1])
            print("Total Estimated Delivery Time is:", int(estimated_delivery_time.__round__(0)), "hours and",
                  int(((estimated_delivery_time * 100 % 100) / 100 * 60).__round__(2)), "minutes")
        else:
            print("path not available")
