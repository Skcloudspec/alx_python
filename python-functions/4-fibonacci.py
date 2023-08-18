#!/usr/bin/env python3
def fibonacci_sequence(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    else:
        fibonacci_list = [0, 1]
        for i in range(2, n):
            fibonacci_list.append(fibonacci_list[i-1] + fibonacci_list[i-2])
        return fibonacci_list
