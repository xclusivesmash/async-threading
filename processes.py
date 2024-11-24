#!/usr/bin/env python3
"""
module: processes
description: more on processes (multi*) in Python.
"""
import time
from multiprocessing import Process


def ask_user():
    start = time.time()
    user_input = input("Please type your name: ")
    greeting = f"Hi, {user_input}"
    print(greeting)
    print(f"user_input: {time.time() - start}")
    return None

def long_calculation():
    start = time.time()
    x = [y**2 for y in range(200000)]
    print(f"long calculation: {time.time() - start}")
    return None

t1 = time.time()
ask_user()
long_calculation()
t2 = time.time()
print(f"overall thread: {t2 - t1}")


# introducing threading
tt1 = time.time()
process1 = Process(target=long_calculation)
process2 = Process(target=long_calculation)

process1.start()
process2.start()

process1.join()
process2.join()

tt2 = time.time()
print(f"processing time: {tt2 - tt1}")
