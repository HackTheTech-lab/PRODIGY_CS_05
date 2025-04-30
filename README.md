# 🛠️ Educational Packet Sniffer Tool

A lightweight, Python‑based packet sniffer for educational and testing purposes. It captures and analyzes network packets in real‑time, displaying key details such as source/destination IPs, protocols, ports, and a hex dump of payload data.

---

## ⚙️ Features

- **Cross‑platform support**: Works on Linux and Windows (with Npcap/WinPcap).
- **Protocol layers**: IP, TCP, UDP, and raw payload inspection.
- **BPF filters**: Apply Berkeley Packet Filter expressions (e.g., `"tcp port 80"`).
- **Packet count**: Limit the number of packets to capture.
- **Extensible callback**: Easy to hook in custom parsing, logging, or visualization.

---

## 📋 Prerequisites

- **Python 3.6+**
- **Scapy** library
- **Elevated privileges** (root/Administrator) to capture raw packets.

### Linux Dependencies
```bash
# Debian/Ubuntu
sudo apt update && sudo apt install -y python3-pip libpcap-dev

# Fedora/RHEL
sudo dnf install -y python3-pip libpcap-devel

# Arch
sudo pacman -Syu python-pip libpcap
```

### Windows Dependency
- Install **Npcap** in WinPcap-compatible mode: https://nmap.org/npcap/

---

## 🚀 Installation

1. Clone this repository (or copy `pkt_sniffer.py` to your machine).

2. Install Scapy:
```bash
pip3 install --user scapy
# or system-wide:
sudo pip3 install scapy
```

3. Make the script executable (Linux/macOS):
```bash
chmod +x pkt_sniffer.py
```

---

## 💡 Usage

### Basic Command
```bash
sudo python3 pkt_sniffer.py [-i INTERFACE] [-n COUNT] [-f FILTER]
```

### Options

| Flag              | Description                                                  |
|------------------|--------------------------------------------------------------|
| `-i, --interface` | Network interface name (e.g., `eth0`, `wlan0`, `Wi-Fi`)     |
| `-n, --number`    | Number of packets to capture (0 = infinite)                 |
| `-f, --filter`    | BPF filter string (e.g., `"tcp port 80"`, `"udp"`)         |

### Examples

- **Capture 50 HTTP packets on Linux**:
```bash
sudo ./pkt_sniffer.py -i eth0 -n 50 -f "tcp port 80"
```

- **Continuous capture on Wi‑Fi (Windows)**:
```powershell
# Run in Administrator PowerShell/CMD
python pkt_sniffer.py -i "Wi-Fi"
```

- **Capture all IP traffic**:
```bash
sudo ./pkt_sniffer.py -f "ip"
```

---

## 🔧 Customization & Extensions

- **Filter**: Use BPF to narrow traffic: `sniff(filter="udp port 53", ...)`
- **Logging**: Modify `packet_callback()` to write JSON/CSV summaries to file.
- **Protocol plugins**: Leverage Scapy’s layers (DNS, HTTP, etc.) for deep parsing.
- **GUI/Dashboard**: Integrate with Flask or Electron for real-time visualization.

---

## ⚖️ Ethical Guidelines

1. **Authorization**: Only sniff on networks where you have explicit permission (lab, home).
2. **Privacy**: Avoid capturing or storing sensitive personal data.
3. **Educational use**: Use as a learning tool or for sanctioned security testing only.

---

![Packet Sniffer](https://img.shields.io/badge/Built%20with-Python-blue?style=flat-square) ![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Linux-green?style=flat-square) ![Status](https://img.shields.io/badge/Status-Active-brightgreen?style=flat-square)

