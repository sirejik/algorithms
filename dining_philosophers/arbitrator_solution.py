"""
Problem statement: Five silent philosophers sit at a round table with bowls of spaghetti. A single chopstick is placed
between each pair of adjacent philosophers. Each philosopher must alternately think and eat. However, a philosopher can
eat spaghetti only when they have both left as well as right pair of chopsticks. Each of chopsticks can be held by one
and only one philosopher and so a philosopher can use them only if it is not being used by another philosopher. After an
individual philosopher finishes eating, they need to put down both the chopsticks in their original positions so that
the chopsticks become available to the others at the table. A philosopher can only take the chopsticks on their right
and the one on their left as they become available and they cannot start eating before getting both the chopsticks.
Eating is not limited by the remaining amounts of spaghetti or stomach space; an infinite supply and an infinite demand
are assumed.

Problem: The problem is how to design a discipline of behavior such that no philosopher will starve; i.e., each can
forever continue to alternate between eating and thinking, assuming that no philosopher can know when others may want to
eat or think.

Solution: In order to pick up the forks, a philosopher must ask permission from the waiter. The waiter gives permission
to only one philosopher at a time until the philosopher has picked up both of their forks. Putting down a fork is always
allowed.
"""
import threading


class Waiter:
    @staticmethod
    def acquire_forks(fork1, fork2):
        if not fork1.locked() and not fork2.locked():
            fork1.acquire()
            fork2.acquire()
            return True
        else:
            return False

    @staticmethod
    def release_forks(fork1, fork2):
        fork1.release()
        fork2.release()


def philosopher(left, right):
    while True:
        with waiter_counter:
            result = Waiter.acquire_forks(left, right)

        if result:
            print('Philosopher with number {} is eating.'.format(threading.currentThread().name))

            with waiter_counter:
                Waiter.release_forks(left, right)


fork_number = 5
forks = [threading.Lock() for n in range(fork_number)]
waiter_counter = threading.Lock()
philosophers = [
    threading.Thread(target=philosopher, args=(forks[n], forks[(n + 1) % fork_number])) for n in range(fork_number)
]
[x.start() for x in philosophers]
