from scapy.all import ARP, Ether, srp
import json

NETWORK = input("ip= ")
INTERFACE = "wlan0"

with open("devices.json", "r") as file:
    devices = json.load(file)

known_devices = devices["devices"]

print(known_devices)

packet = Ether(dst="ff:ff:ff:ff:ff:ff") / ARP(pdst=NETWORK)

answered, _ = srp(
    packet,
    iface=INTERFACE,
    timeout=2,
    verbose=False
)

print("\nDevices found:")
print("-" * 50)

for _, response in answered:

    mac = response.hwsrc
    ip = response.psrc

    if mac not in known_devices:
        known_devices[mac] = {
            "ip": ip
        }

    print(f"IP: {ip:<16} MAC: {mac}")

with open("devices.json", "w") as file:
    json.dump(devices, file, indent=4)

print("\nDatabase in memory:")
print(known_devices)

print("-" * 50)
print(f"Total devices: {len(answered)}")
