from Utilities.ShipmentsUtility import get_shipment_with_awb

curr_awb = int(input("Your Shipment/AWB Number is?? \n -->> "))

curr_shipment = get_shipment_with_awb(curr_awb)

if curr_shipment is not None:
    print("(Origin)", curr_shipment.origin, "-> (Destination)", curr_shipment.destination)
    path, edd = curr_shipment.get_estimated_delivery_time()
    print(path + "\n" + edd)
else:
    print("Please check your AWB Number")
