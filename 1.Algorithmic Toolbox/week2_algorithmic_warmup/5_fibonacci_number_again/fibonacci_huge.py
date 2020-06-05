# Uses python3
import sys
import math

def get_fibonacci_huge_naive(n, m):
    val = (math.sqrt(5) + 1) / 2
    fib = round((val ** n) / math.sqrt(5))
    return fib % m


if __name__ == '__main__':
    input = sys.stdin.read()
    n, m = map(int, input.split())
    print(get_fibonacci_huge_naive(n, m))
