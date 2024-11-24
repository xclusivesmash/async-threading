#!/usr/bin/env python3
"""
module: generators
description: implementing threading through generators.
"""


def countdown(number):
    while number > 0:
        yield number
        number = number - 1
    return None

c1 = countdown(10)
c2 = countdown(20)
print(next(c1))
print(next(c2))
print(next(c1))
print(next(c2))
