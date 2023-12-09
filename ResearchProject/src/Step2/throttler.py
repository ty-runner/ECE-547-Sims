from collections import defaultdict
import time
import csv

class BandwidthThrottler:
    def __init__(self, total_bandwidth):
        self.total_bandwidth = total_bandwidth
        self.destination_bandwidth = defaultdict(int)
        self.last_reset_time = time.time()

    def throttle_bandwidth(self, destination_ip, packet_length):
        current_time = time.time()

        # Reset bandwidth counters if a second has passed
        if current_time - self.last_reset_time >= 1:
            self.destination_bandwidth = defaultdict(int)
            self.last_reset_time = current_time

        # Check if there is enough bandwidth for the current packet
        if self.destination_bandwidth[destination_ip] + packet_length <= self.total_bandwidth:
            self.destination_bandwidth[destination_ip] += packet_length
            return True
        else:
            return False

# Example usage:
total_bandwidth = 2000  # Set your total bandwidth limit here
throttler = BandwidthThrottler(total_bandwidth)

# Replace 'your_file.csv' with the actual path to your CSV file
with open('output.csv', 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    
    for packet in reader:
        timestamp = float(packet["Timestamp"])
        destination_ip = packet["Destination IP"]
        packet_length = int(packet["Length"])

        if throttler.throttle_bandwidth(destination_ip, packet_length):
            print(f"Packet allowed at {timestamp} for Destination IP {destination_ip}")
        else:
            print(f"Packet throttled at {timestamp} for Destination IP {destination_ip}")
