from collections import defaultdict
import time
import csv

class BandwidthThrottler:
    def __init__(self, total_bandwidth):
        self.total_bandwidth = total_bandwidth
        self.destination_bandwidth = defaultdict(int)
        self.last_reset_time = time.time()
        self.bandwidth_usage = defaultdict(int)

    def throttle_bandwidth(self, destination_ip, packet_length):
        current_time = time.time()

        # Reset bandwidth counters if a second has passed
        if current_time - self.last_reset_time >= 1:
            self.destination_bandwidth = defaultdict(int)
            self.last_reset_time = current_time

        # Check if there is enough bandwidth for the current packet
        if self.destination_bandwidth[destination_ip] + packet_length <= self.total_bandwidth:
            self.destination_bandwidth[destination_ip] += packet_length
            self.bandwidth_usage[destination_ip] += packet_length
            print(self.bandwidth_usage)
            return True
        else:
            return False

# Example usage:
total_bandwidth = 2000  # Set your total bandwidth limit here
throttler = BandwidthThrottler(total_bandwidth)
#we want to throttle the total bandwidth and distribute it among the destination IPs
#we prioritize the destination IPs with the highest bandwidth usage

#to do this...
#keep count of total bandwidth usage during a session
#if a packet comes in, check if there is enough bandwidth for the packet
#if there is, add the packet to the bandwidth usage
#if there isn't, drop the packet, increase the drop count, and attempt to increase the bandwidth of the limited IPs

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
