# Network Documentation & Inventory System

A practical network documentation and inventory project designed for entry-level IT roles.

This project demonstrates real-world skills used by Help Desk, Tech Specialist, and Junior Network technicians, including:

- Network documentation
- Device inventory management
- IP addressing standards
- Port and cable mapping
- Basic troubleshooting processes
- Lightweight automation scripts

## Project Structure

network-documentation-system/
├── docs/
│   ├── 01-network-overview.md
│   ├── 02-ip-addressing-plan.md
│   ├── 03-device-naming-standards.md
│   ├── 04-port-and-cable-mapping.md
│   └── 05-troubleshooting-notes.md
├── inventory/
│   ├── devices.csv
│   └── inventory_report.txt          ← created by the export script
├── scripts/
│   ├── view_inventory.py
│   ├── search_device.py
│   └── export_report.py
├── diagrams/
├── requirements.txt
└── README.md

## Features

- Complete small-office network documentation
- Structured device inventory (routers, switches, access points, firewall, server)
- IP addressing plan
- Device naming standards
- Port and cable mapping
- Troubleshooting guide
- Python scripts to view, search, and export inventory data

## How to Use the Scripts

```bash
# View all devices
python scripts/view_inventory.py

# Search for a device
python scripts/search_device.py

# Generate a summary report
python scripts/export_report.py

# Skills Demonstrated 
Network fundamentals (routers, switches, access points, firewalls)
IP addressing and subnetting concepts
Network documentation best practices
Inventory tracking
Basic Python automation
Professional project organization