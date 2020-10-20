"""
Problem statement: Some threads may read and some may write, with the constraint that no thread may access the shared
resource for either reading or writing while another thread is in the act of writing to it.

Problem: No thread shall be allowed to starve; that is, the operation of obtaining a lock on the shared data will always
terminate in a bounded amount of time.
"""
import threading

from time import sleep


def reader():
    global text
    global reader_count

    while True:
        with service:
            with reader_counter:
                reader_count += 1
                if reader_count == 1:
                    text_counter.acquire()

        print('Reading text by thread with name {}.'.format(threading.currentThread().name))
        sleep(1)

        with reader_counter:
            reader_count -= 1
            if reader_count == 0:
                text_counter.release()


def writer():
    global text

    while True:
        with service:
            text_counter.acquire()

        print('Writing text by thread with name {}.'.format(threading.currentThread().name))
        sleep(1)

        text_counter.release()


def philosopher(left, right):
    if id(left) < id(right):
        first, second = left, right
    else:
        first, second = right, left

    while True:
        with first:
            with second:
                print('Philosopher with number {} is eating.'.format(threading.currentThread()))


reader_number = 5
writer_number = 2

service = threading.Lock()
text_counter = threading.Lock()
reader_counter = threading.Lock()
reader_count = 0

text = ''

threads = [threading.Thread(target=reader) for _ in range(reader_number)] + \
          [threading.Thread(target=writer) for _ in range(writer_number)]
[x.start() for x in threads]
