#!/usr/bin/env python3
"""
module: non_lock_threading
description: problems with running threads sequencially without queing.
"""
import random
import time
from threading import Thread


counter = 0
def increment_count():
    global counter
    # introduce fuzzing
    time.sleep(random.random())
    counter = counter + 1
    time.sleep(random.random())
    print(f"counter_value: {counter}")
    time.sleep(random.random())
    print("--------------------------")
    time.sleep(random.random())
    return None

for _ in range(10):
    time.sleep(random.random())
    t = Thread(target=increment_count)
    time.sleep(random.random())
    t.start()
