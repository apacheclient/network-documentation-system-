# Network Overview

## Purpose
This document provides a high-level overview of the small office network.

## Network Summary
- Network Type: Small Office / Single Site
- Primary Function: Support daily business operations, file sharing, and internet access
- Internet Connection: Single ISP handoff to edge router
- Core Switching: One core switch + two access switches
- Wireless: Two access points covering lobby and main office area
- Security: Dedicated firewall at the network edge

## High-Level Design
Internet
   ↓
Edge Router (RT-01)
   ↓
Firewall (FW-01)
   ↓
Core Switch (SW-01)
   ├── Access Switch 1 (SW-02) → Cubicles
   ├── Access Switch 2 (SW-03) → Floor 2
   ├── Access Point 1 (AP-01) → Lobby
   ├── Access Point 2 (AP-02) → Open Office
   └── File Server (SRV-01)

## Key Design Notes
- Hierarchical design (Core → Access)
- All critical devices are located in the Main Closet
- Wireless is provided by dedicated access points (not router Wi-Fi)
- Management IPs are assigned from a dedicated range