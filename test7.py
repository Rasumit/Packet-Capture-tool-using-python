import scapy.all as scapy
from scapy.layers import http

def sniffing(interface):
    scapy.sniff(iface=interface, store=False, prn=process_packet, filter='tcp')

def process_packet(packet):
    print(packet.show())
    #if packet.haslayer(http.HTTPRequest):
        #print(packet[http.HTTPRequest].Host)
        #print(packet)


sniffing('Wi-Fi')