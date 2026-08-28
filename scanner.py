from scapy.all import ARP, Ether, srp

NETWORK = "192.168.18.0/24"
INTERFACE = "wlan0"

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
    print(f"IP: {response.psrc:<16} MAC: {response.hwsrc}")

print("-" * 50)
print(f"Total devices: {len(answered)}")
