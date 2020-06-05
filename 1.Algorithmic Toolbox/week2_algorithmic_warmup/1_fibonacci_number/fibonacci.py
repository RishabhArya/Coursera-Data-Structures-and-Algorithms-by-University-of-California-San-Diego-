# Uses python3
import math

def calc_fib(n):
    # {[(√5 + 1)/2] ^ n} / √5
    val = (math.sqrt(5) + 1) / 2
    fib = round((val**n)/math.sqrt(5))
    fib = round(fib)
    return fib


if __name__ == '__main__':
    n = int(input())
    print(calc_fib(n))
