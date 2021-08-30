from Models import ShipmentHaulLine
from Models import ShipmentMilkRun
from Models import ODPair

import pandas as pd


def create_od_pairs():
    od_pair_shipments = []
    df = pd.read_excel(r'C:\Users\93855\Downloads\initial\EDD_assignment.xlsx', sheet_name='OD Pairs',
                       usecols=['Origin', 'Destination', 'Duration'])
    for x in range(0, len(df)):
        shipment = ODPair.ODPair(9000 + x, df['Origin'][x], df['Destination'][x])
        od_pair_shipments.append(shipment)
    return od_pair_shipments


def create_shipments_haul_line():
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
    shipments_data_milk_run = []
    df = pd.read_excel(r'C:\Users\93855\Downloads\initial\EDD_assignment.xlsx', sheet_name='MilkRun',
                       usecols=['hub', 'milk_run',
                                'std', 'sta', 'travel_time', 'breaches'])
    for x in range(0, len(df)):
        shipment = ShipmentMilkRun.ShipmentMilkRun(df['hub'][x], df['milk_run'][x], df['travel_time'][x], df['std'][x],
                                                   df['sta'][x], df['breaches'][x])
        shipments_data_milk_run.append(shipment)
    return shipments_data_milk_run


def get_shipment_with_awb(awb, shipments):
    for shipment in shipments:
        if shipment.awb == awb:
            return shipment


def find_destination_hub_and_leg_travel_time(milk_run_shipments, destination):
    for shipment in milk_run_shipments:
        for dest in shipment.milk_run.split('-'):
            if dest == destination:
                return shipment.hub, shipment.travel_time
    return 'not found', 0


def find_previous_hub_and_travel_time(haul_line_shipments, destination_hub):
    for shipment in haul_line_shipments:
        for destination in shipment.to.split('-'):
            if destination == destination_hub:
                return shipment.frm, shipment.leg_travel_time
