Educational Packet Sniffer ToolA lightweight, Python‑based packet sniffer for educational and testing purposes. It captures and analyzes network packets in real‑time, displaying key details such as source/destination IPs, protocols, ports, and a hex dump of payload data.
⚙️ FeaturesCross‑platform support: Works on Linux and Windows (with Npcap/WinPcap).
Protocol layers: IP, TCP, UDP, and raw payload inspection.
BPF filters: Apply Berkeley Packet Filter expressions (e.g., "tcp port 80").
Packet count: Limit the number of packets to capture.
Extensible callback: Easy to hook in custom parsing, logging, or visualization.
📋 PrerequisitesPython 3.6+
Scapy library
Elevated privileges (root/Administrator) to capture raw packets.
Linux dependencies (for Linux users):
# Debian/Ubuntu
sudo apt update && sudo apt install -y python3-pip libpcap-dev

# Fedora/RHEL
sudo dnf install -y python3-pip libpcap-devel

# Arch
sudo pacman -Syu python-pip libpcapWindows dependency (for Windows users):
Install Npcap in WinPcap-compatible mode: https://nmap.org/npcap/
🚀 InstallationClone this repository (or copy pkt_sniffer.py to your machine).
Install Scapy:
pip3 install --user scapy
# or system-wide:
sudo pip3 install scapyMake the script executable (Linux/macOS):
chmod +x pkt_sniffer.py💡 UsageBasic Commandsudo python3 pkt_sniffer.py [-i INTERFACE] [-n COUNT] [-f FILTER]OptionsFlagDescription-i, --interfaceNetwork interface name (e.g., eth0, wlan0, Wi-Fi)-n, --numberNumber of packets to capture (0 = infinite)-f, --filterBPF filter string (e.g., "tcp port 80", "udp")ExamplesCapture 50 HTTP packets on Linux:
sudo ./pkt_sniffer.py -i eth0 -n 50 -f "tcp port 80"Continuous capture on Wi‑Fi (Windows):
# Run in Administrator PowerShell/CMD
python pkt_sniffer.py -i "Wi-Fi"Capture all IP traffic:
sudo ./pkt_sniffer.py -f "ip"🔧 Customization & ExtensionsFilter: Use BPF to narrow traffic: sniff(filter="udp port 53", …).
Logging: Modify packet_callback() to write JSON/CSV summaries to file.
Protocol plugins: Leverage Scapy’s layers (DNS, HTTP, etc.) for deep parsing.
GUI/Dashboard: Integrate with Flask or Electron for real-time visualization.
⚖️ Ethical GuidelinesAuthorization: Only sniff on networks where you have explicit permission (lab, home).
Privacy: Avoid capturing or storing sensitive personal data.
