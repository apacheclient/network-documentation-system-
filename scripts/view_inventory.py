import csv
from pathlib import Path

# Path to the inventory file
inventory_file = Path(__file__).parent.parent / "inventory" / "devices.csv"

def view_inventory():
    print("\n=== Network Device Inventory ===\n")

    with open(inventory_file, newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        # Print header
        print(f"{'ID':<8} {'Hostname':<20} {'Type':<14} {'IP Address':<16} {'Location'}")
        print("-" * 80)

        for device in reader:
            print(f"{device['device_id']:<8} {device['hostname']:<20} {device['device_type']:<14} {device['ip_address']:<16} {device['location']}")

    print()

if __name__ == "__main__":
    view_inventory()