import psutil 
from socket import AddressFamily
import ipaddress


res = psutil.net_if_addrs()['Wi-Fi']
for infos in res:
    if infos.family == AddressFamily.AF_INET:
        ip = infos.address
        netmask = infos.netmask
        cidr = ipaddress.IPv4Network(f"0.0.0.0/{netmask}").prefixlen
        nb_adr = 2**(32-cidr)
        print(f"{ip}/{cidr}")
        print(f"{nb_adr} adresses")