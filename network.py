#!/usr/bin/env python3
"""
Educational Packet Sniffer
Requires: scapy
Usage: sudo python3 pkt_sniffer.py [-i INTERFACE] [-n COUNT]
"""

import argparse
from scapy.all import sniff, IP, TCP, UDP, Raw

def packet_callback(pkt):
    """Called for each captured packet; prints summary info."""
    if IP in pkt:
        ip_layer = pkt[IP]
        src = ip_layer.src
        dst = ip_layer.dst
        proto = ip_layer.proto

        print(f"\n=== New Packet ===")
        print(f"Source      : {src}")
        print(f"Destination : {dst}")
        print(f"Protocol    : {proto}")

        # TCP layer
        if TCP in pkt:
            tcp_layer = pkt[TCP]
            print(f"TCP Ports   : {tcp_layer.sport} → {tcp_layer.dport}")
        # UDP layer
        elif UDP in pkt:
            udp_layer = pkt[UDP]
            print(f"UDP Ports   : {udp_layer.sport} → {udp_layer.dport}")

        # Payload (hex dump of up to 32 bytes)
        if Raw in pkt:
            data = pkt[Raw].load
            hexdump = data[:32].hex()
            ellipsis = "..." if len(data) > 32 else ""
            print(f"Payload     : {hexdump}{ellipsis}")

def start_sniff(interface: str = None, count: int = 0, bpf: str = None):
    """
    :param interface: network interface to sniff (e.g. 'eth0' or 'Wi-Fi')
    :param count: number of packets to capture (0=infinite)
    :param bpf: Berkeley Packet Filter string (e.g. 'tcp port 80')
    """
    print(f"Starting sniff on {interface or 'all interfaces'} "
          f"(count={'∞' if count == 0 else count})"
          f"{', filter='+bpf if bpf else ''}")
    sniff(prn=packet_callback,
          iface=interface,
          count=count,
          filter=bpf,
          store=False)

def main():
    parser = argparse.ArgumentParser(
        description="Educational Packet Sniffer Tool")
    parser.add_argument(
        "-i", "--interface",
        help="Network interface to listen on (default: all)")
    parser.add_argument(
        "-n", "--number", type=int, default=0,
        help="Number of packets to capture (0=infinite)")
    parser.add_argument(
        "-f", "--filter", default=None,
        help="BPF filter (e.g. 'tcp port 80', 'udp')")
    args = parser.parse_args()

    try:
        start_sniff(interface=args.interface,
                    count=args.number,
                    bpf=args.filter)
    except PermissionError:
        print("Error: This script must be run with elevated privileges (sudo/root).")

if __name__ == "__main__":
    main()
