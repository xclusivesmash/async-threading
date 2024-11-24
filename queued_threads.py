#!/usr/bin/env python3
"""
module: queued_threads
description: using the queue module to do task sequentially in threading
'time.sleep(random.random())' introduces fuzzing
"""
import time
import random
import queue
from threading import Thread


counter = 0 # global variable
job_queue = queue.Queue() # stores jobs to be performed
counter_queue = queue.Queue() # stores amount by which to increase counter

def increment_manager():
    global counter
    while True:
        time.sleep(random.random())
        increment = counter_queue.get() # waits until value is available and locks.
        time.sleep(random.random())
        old_counter = counter
        counter = old_counter + increment
        time.sleep(random.random())
        job_queue.put((f"counter_value: {counter}", "---------------------"))
        time.sleep(random.random())
        counter_queue.task_done()

Thread(target=increment_manager, daemon=True).start()
time.sleep(random.random())

def printer_manager():
    while True:
        for line in job_queue.get():
            print(line)
            time.sleep(random.random())
        job_queue.task_done()

Thread(target=printer_manager, daemon=True).start()
time.sleep(random.random())

def increment_counter():
    counter_queue.put(1)
    time.sleep(random.random())

workers = [Thread(target=increment_counter) for _ in range(10)]

for thread in workers:
    thread.start()
    time.sleep(random.random())

for thread in workers:
    thread.join()
    time.sleep(random.random())

counter_queue.join()
time.sleep(random.random())
job_queue.join()

