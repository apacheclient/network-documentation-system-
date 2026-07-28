# Port and Cable Mapping

## Purpose
This document tracks how devices are physically connected.

## Core Switch (SW-01) – 48 Port

| Port   | Connected To              | Cable Type | Notes                  |
|--------|---------------------------|------------|------------------------|
| Gi1/0/1| Edge Router (RT-01)       | Cat6       | Uplink to router       |
| Gi1/0/2| Firewall (FW-01)          | Cat6       |                        |
| Gi1/0/3| Access Switch 1 (SW-02)   | Cat6       | Downlink               |
| Gi1/0/4| Access Switch 2 (SW-03)   | Cat6       | Downlink               |
| Gi1/0/5| File Server (SRV-01)      | Cat6       |                        |
| Gi1/0/6| AP-01 (Lobby)             | Cat6       | PoE                    |
| Gi1/0/7| AP-02 (Office)            | Cat6       | PoE                    |

## Access Switch 1 (SW-02) – 24 Port

| Port Range    | Purpose                     |
|---------------|-----------------------------|
| Ports 1–20    | User workstations           |
| Ports 21–22   | Printers                    |
| Port 24       | Uplink to Core Switch       |

## Cabling Standards
- Horizontal cabling: Cat6
- Patch cables: Cat6
- Backbone between closets: Cat6 (future fiber recommended)
- All cables labeled on both ends