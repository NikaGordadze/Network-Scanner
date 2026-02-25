from network_functions import get_local_ip, get_subnet_mask

print("Local IP Address:", get_local_ip())

subnet = get_subnet_mask(get_local_ip())
if subnet is None:
    print("Could not determine subnet mask.")
else:
    print("Subnet Mask:", subnet)