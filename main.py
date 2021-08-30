import ShipmentsUtility
from ShipmentsUtility import get_shipment_with_awb

ODPair_shipments = ShipmentsUtility.create_od_pairs()

curr_awb = int(input("Your Shipment/AWB Number is?? \n -->> "))

curr_shipment = get_shipment_with_awb(curr_awb, ODPair_shipments)

print("(Origin)", curr_shipment.origin, "-> (Destination)", curr_shipment.destination)

curr_shipment.get_estimated_delivery_time()


