import random

CHANCE_OF_CONCESSIONS = 0.5

def moviegoer_behavior(env, moviegoer, theater, wait_times):
    # moviegoer arrives at the theater
    arrival_time = env.now

    # moviegoer gets in line to buy a ticket
    with theater.cashier.request() as request:
        yield request
        yield env.process(theater.buy_ticket(moviegoer))

    # moviegoer waits in line to have the ticket checked
    with theater.ushers.request() as request:
        yield request
        yield env.process(theater.check_ticket(moviegoer))

    # moviegoer decides to buy concessions
    if random.random() < CHANCE_OF_CONCESSIONS:
        # moviegoer gets in line to buy concessions
        with theater.servers.request() as request:
            yield request
            yield env.process(theater.sell_food(moviegoer))

    # moviegoer goes to the theater
    wait_time = env.now - arrival_time
    wait_times.append(wait_time)