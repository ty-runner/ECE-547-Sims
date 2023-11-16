import simpy

class NetworkNode:
    def __init__(self, env, name, transmission_rate, processing_time):
        self.env = env
        self.name = name
        self.transmission_rate = transmission_rate
        self.processing_time = processing_time
        self.queue = simpy.Store(env)

    def transmit_frame(self, frame):
        start_time = self.env.now
        transmission_time = len(frame) / self.transmission_rate
        yield self.env.timeout(transmission_time)
        end_time = self.env.now
        total_time = end_time - start_time
        print(f"{self.name} transmitted frame in {total_time} time units")

    def process_frame(self, frame):
        start_time = self.env.now
        processing_delay = self.processing_time
        yield self.env.timeout(processing_delay)
        end_time = self.env.now
        total_time = end_time - start_time
        print(f"{self.name} processed frame in {total_time} time units")

    def propagate_frame(self, frame):
        start_time = self.env.now
        propagation_delay = 1  # Assuming 1 time unit for simplicity
        yield self.env.timeout(propagation_delay)
        end_time = self.env.now
        total_time = end_time - start_time
        print(f"{self.name} propagated frame in {total_time} time units")

def network_node(env, node, frame):
    yield env.process(node.transmit_frame(frame))
    yield env.process(node.propagate_frame(frame))
    yield env.process(node.process_frame(frame))

def main():
    env = simpy.Environment()

    transmission_rate = 10  # frames per time unit
    processing_time = 2  # time units
    node_A = NetworkNode(env, 'A', transmission_rate, processing_time)
    node_B = NetworkNode(env, 'B', transmission_rate, processing_time)

    frame = "Hello, World!"  # Example frame

    env.process(network_node(env, node_A, frame))
    env.process(network_node(env, node_B, frame))

    env.run(until=30)  # Run the simulation for 30 time units

if __name__ == '__main__':
    main()
