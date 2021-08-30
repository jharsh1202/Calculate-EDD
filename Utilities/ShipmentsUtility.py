import pandas as pd

from Models import ODPair
from Models import ShipmentHaulLine
from Models import ShipmentMilkRun


def create_od_pairs():
    """
    This method loads the sample ODPairs, and assigns AWB number to each shipment starting from 9000.
    :return: This method returns the collection of ODPair objects loaded from ODPair Sample sheet of EDD_assignment.xlsx
    """
    od_pair_shipments = []
    df = pd.read_excel(r'C:\Users\93855\Downloads\initial\EDD_assignment.xlsx', sheet_name='OD Pairs',
                       usecols=['Origin', 'Destination', 'Duration'])
    for x in range(0, len(df)):
        shipment = ODPair.ODPair(9000 + x, df['Origin'][x], df['Destination'][x])
        od_pair_shipments.append(shipment)
    return od_pair_shipments


def create_shipments_haul_line():
    """
    This method loads the shipments data from haul line sheet of EDD_assignment.xlsx.
    :return: This method returns the collection of Haul Line objects loaded from Haul Line sheet of
    EDD_assignment.xlsx
    """
    shipments_data_line_haul = []
    df = pd.read_excel(r'C:\Users\93855\Downloads\initial\EDD_assignment.xlsx',
                       usecols=['run_name', 'from', 'to', 'std', 'sta',
                                'origin', 'destination_',
                                'leg_travel_time'])
    for x in range(0, len(df)):
        shipment = ShipmentHaulLine.ShipmentHaulLine(df['from'][x], df['to'][x], df['origin'][x],
                                                     df['destination_'][x],
                                                     df['std'][x], df['sta'][x], df['run_name'][x],
                                                     df['leg_travel_time'][x])
        shipments_data_line_haul.append(shipment)
    return shipments_data_line_haul


def create_shipments_milk_run():
    """
        This method loads the shipments data from milk run sheet of EDD_assignment.xlsx
        :return: This method returns the collection of Milk Run objects loaded from milk run sheet of
        EDD_assignment.xlsx
        """
    shipments_data_milk_run = []
    df = pd.read_excel(r'C:\Users\93855\Downloads\initial\EDD_assignment.xlsx', sheet_name='MilkRun',
                       usecols=['hub', 'milk_run',
                                'std', 'sta', 'travel_time', 'breaches'])
    for x in range(0, len(df)):
        shipment = ShipmentMilkRun.ShipmentMilkRun(df['hub'][x], df['milk_run'][x], df['travel_time'][x], df['std'][x],
                                                   df['sta'][x], df['breaches'][x])
        shipments_data_milk_run.append(shipment)
    return shipments_data_milk_run


def get_shipment_with_awb(awb):
    """
    This methods finds the shipment with a given AWB Number
    :param awb: Air way bill Number that needs to be searched.
    :return: This method return the shipment which has awb number equal to awb no. in the argument of this function.
    """
    from Database import ShipmentsData
    shipments = ShipmentsData.od_pair_shipments
    for shipment in shipments:
        if shipment.awb == awb:
            return shipment


def find_destination_hub_and_leg_travel_time(destination):
    """
    This method finds the destination hub for a particular shipment and also the time it takes to reach from DC to
    Destination
    :param destination: The destination to which the shipment has to reach.
    :return:
    """
    milk_run_shipments = create_shipments_milk_run()
    for shipment in milk_run_shipments:
        for dest in shipment.milk_run.split('-'):
            if dest == destination:
                return shipment.hub, shipment.travel_time
    return 'not found', 0


def find_previous_hub_and_travel_time(destination_hub):
    haul_line_shipments = create_shipments_haul_line()
    for shipment in haul_line_shipments:
        for destination in shipment.to.split('-'):
            if destination == destination_hub:
                return shipment.frm, shipment.leg_travel_time
