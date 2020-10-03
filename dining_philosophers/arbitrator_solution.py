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
