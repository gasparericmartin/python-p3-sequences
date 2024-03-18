#!/usr/bin/env python3

def print_fibonacci(length):
    fib_list = []

    if length == 0:
        print(fib_list)
    elif length == 1:
        fib_list.append(0)
        print(fib_list)
    else:
        fib_list.extend([0,1])
        for x in range(length - 2):
            fib_list.append(fib_list[len(fib_list) -2] + fib_list[len(fib_list) - 1])
        print(fib_list)
