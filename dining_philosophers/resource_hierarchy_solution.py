import threading


def philosopher(left, right):
    if id(left) < id(right):
        first, second = left, right
    else:
        first, second = right, left

    while True:
        with first:
            with second:
                print('Philosopher with number {} is eating.'.format(threading.currentThread().name))


fork_number = 5
forks = [threading.Lock() for n in range(fork_number)]
philosophers = [
    threading.Thread(target=philosopher, args=(forks[n], forks[(n + 1) % fork_number])) for n in range(fork_number)
]
[x.start() for x in philosophers]
