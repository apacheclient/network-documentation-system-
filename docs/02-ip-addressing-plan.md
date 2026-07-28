# IP Addressing Plan

## Network Range
- Private Network: 192.168.1.0/24
- Subnet Mask: 255.255.255.0
- Usable Hosts: 192.168.1.1 – 192.168.1.254

## Address Allocation

| Range              | Purpose                        |
|--------------------|--------------------------------|
| 192.168.1.1 – 9    | Network Infrastructure         |
| 192.168.1.10 – 19  | Wireless Access Points         |
| 192.168.1.20 – 49  | Servers                        |
| 192.168.1.50 – 199 | DHCP for Workstations / Laptops|
| 192.168.1.200 – 254| Reserved / Static Devices      |

## Assigned Infrastructure IPs

| Device          | Hostname            | IP Address     |
|-----------------|---------------------|----------------|
| Edge Router     | edge-router-01      | 192.168.1.1    |
| Core Switch     | core-switch-01      | 192.168.1.2    |
| Access Switch 1 | access-switch-01    | 192.168.1.3    |
| Access Switch 2 | access-switch-02    | 192.168.1.4    |
| Firewall        | firewall-01         | 192.168.1.254  |
| AP Lobby        | wifi-ap-lobby       | 192.168.1.10   |
| AP Office       | wifi-ap-office      | 192.168.1.11   |
| File Server     | file-server-01      | 192.168.1.20   |

## Notes
- DHCP is planned for the .50 – .199 range
- All network devices use static IPs
- .254 is reserved for the firewall