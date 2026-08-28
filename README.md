# 🛡️ AyamCheckWiFi

A lightweight network monitoring and anomaly detection tool built with **Python** and **Scapy**.

AyamCheckWiFi is designed to discover devices on a local network, keep track of known devices, and eventually detect unusual network activity.

> 🚧 **Status:** Work in Progress

## ✨ Features

### Currently Available

* 🔍 Local network device discovery
* 📡 ARP-based network scanning
* 🖥️ IP and MAC address identification
* 🐍 Built with Python and Scapy

### Planned

* 💾 Known-device database
* 🚨 New-device detection
* 🕐 Device activity history
* 📊 Network traffic monitoring
* 🔎 Anomaly detection
* 📈 Network monitoring dashboard
* 🔔 Security alerts

## 🏗️ Project Roadmap

```text
v0.1  Initial ARP Scanner             ✅
  ↓
v0.2  Device Database                 ⏳
  ↓
v0.3  New Device Detection            ⏳
  ↓
v0.4  Device History                  ⏳
  ↓
v0.5  Traffic Monitoring              ⏳
  ↓
v0.6  Anomaly Detection               ⏳
  ↓
v1.0  Network Anomaly Detector        ⏳
```

## 🧰 Technologies

* **Python 3**
* **Scapy**
* **Linux / Kali Linux**
* **Git & GitHub**

## 🚀 Getting Started

### Requirements

* Python 3
* Scapy
* A Linux environment with access to the local network interface

### Installation

Clone the repository:

```bash
git clone https://github.com/yoroki12/ayamcheckwifi.git
cd ayamcheckwifi
```

Install Scapy:

```bash
sudo apt update
sudo apt install python3-scapy
```

### Usage

Configure the network interface and local network in `scanner.py`:

```python
NETWORK = "192.168.18.0/24"
INTERFACE = "wlan0"
```

Then run:

```bash
sudo python3 scanner.py
```

Example output:

```text
Devices found:
--------------------------------------------------
IP: 192.168.18.1     MAC: xx:xx:xx:xx:xx:xx
IP: 192.168.18.11    MAC: xx:xx:xx:xx:xx:xx
IP: 192.168.18.16    MAC: xx:xx:xx:xx:xx:xx
--------------------------------------------------
Total devices: 3
```

## 🔐 How It Works

The current version uses **ARP (Address Resolution Protocol)** to discover devices on the local network.

```text
                Local Network
                     │
                     ▼
              ARP Discovery
                     │
          ┌──────────┼──────────┐
          ▼          ▼          ▼
       Device 1   Device 2   Device 3
          │          │          │
          └──────────┼──────────┘
                     ▼
              IP + MAC Address
```

Future versions will use the discovered information as a foundation for device tracking and anomaly detection.

## 🎯 Goals

The main goals of this project are to:

1. Learn practical network programming with Python.
2. Understand ARP and local network discovery.
3. Build a lightweight network monitoring system.
4. Detect unexpected devices and unusual network behavior.
5. Explore concepts used in network security and intrusion detection.

## ⚠️ Responsible Use

AyamCheckWiFi is intended for **educational purposes and authorized networks only**.

Only monitor networks and devices that you own or have explicit permission to monitor.

Do not use this project to intercept, disrupt, or access networks without authorization.

## 📌 Project Status

This project is actively being developed.

The current release focuses on basic local-network device discovery. More advanced monitoring and anomaly detection capabilities will be added incrementally.

## 📄 License

This project is currently unlicensed. A license may be added in a future release.
