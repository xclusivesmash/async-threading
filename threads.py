#!/usr/bin/env python3
"""
module: threads
description: more on threading in Python.
"""
import time
from threading import Thread


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
thread1 = Thread(target=long_calculation)
thread2 = Thread(target=ask_user)

thread1.start()
thread2.start()

thread1.join()
thread2.join()

tt2 = time.time()
print(f"Threading time: {tt2 - tt1}")
