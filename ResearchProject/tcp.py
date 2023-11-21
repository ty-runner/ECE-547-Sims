import simpy

class TCPSender:
    def __init__(self, env, cwnd=1):
        self.env = env
        self.cwnd = cwnd
        self.ack = env.event()

    def send(self):
        while True:
            yield self.env.timeout(1)  # Time unit for simulation

            # Send packets
            for _ in range(self.cwnd):
                print(f"Packet sent at time {self.env.now}")
                self.env.process(self.wait_for_ack())

            # Wait for the ACK event
            yield self.ack

            # Adjust congestion window (for simplicity, using additive increase)
            self.cwnd += 1

    def wait_for_ack(self):
        i = 0
        yield self.env.timeout(1)  # Simulating round-trip time
        print(f"ACK {i} received at time {self.env.now}")
        self.ack.succeed()
        self.ack = self.env.event()
        i += 1

class Network:
    def __init__(self, env, bandwidth=1):
        self.env = env
        self.bandwidth = bandwidth
        self.queue = simpy.Store(env)

    def transmit(self):
        while True:
            packet = yield self.queue.get()
            yield self.env.timeout(1 / self.bandwidth)
            print(f"Packet transmitted at time {self.env.now}")
            packet.succeed()

def simulate_tcp(env, sender, network):
    env.process(sender.send())
    env.process(network.transmit())
    env.run(until=30)  # Run the simulation for 10 time units

# Example usage
env = simpy.Environment()
sender = TCPSender(env)
network = Network(env)

# Connect the sender and the network
sender.ack = network.queue.put(env.event())

simulate_tcp(env, sender, network)
