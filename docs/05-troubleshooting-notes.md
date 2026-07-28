# Troubleshooting Notes

## Common Network Issues

### 1. User has no network connection
**Check in order:**
1. Is the network cable properly plugged in?
2. Are the link lights on the network card and switch port on?
3. Does the device have a valid IP address? (`ipconfig`)
4. Can it ping the gateway? (`ping 192.168.1.1`)
5. Can it ping an external address? (`ping 8.8.8.8`)

### 2. Slow network speed
- Check if the port is running at 100 Mbps instead of 1 Gbps
- Look for high CPU on the switch
- Check for duplex mismatches
- Test with a known good cable

### 3. Wireless issues
- Confirm the access point is online
- Check if the user is connected to the correct SSID
- Move closer to the AP and retest
- Restart the wireless adapter

### 4. Cannot reach a specific server
- Ping the server IP
- Confirm the server is online
- Check firewall rules
- Verify the correct DNS name is being used

## Useful Commands

| Command                  | Purpose                              |
|--------------------------|--------------------------------------|
| `ipconfig /all`          | Show detailed IP information         |
| `ping <ip>`              | Test basic connectivity              |
| `tracert <ip>`           | Show the path to a destination       |
| `nslookup <name>`        | Test DNS resolution                  |
| `arp -a`                 | Show ARP table                       |