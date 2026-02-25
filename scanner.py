from network_functions import get_local_ip, get_subnet_mask

local_ip = get_local_ip()
if local_ip is None:
    print("Could not determine local IP address.")
else:    
    print("Local IP Address:", local_ip)

subnet = get_subnet_mask(local_ip)
if subnet is None:
    print("Could not determine subnet mask.")
else:
    print("Subnet Mask:", subnet)