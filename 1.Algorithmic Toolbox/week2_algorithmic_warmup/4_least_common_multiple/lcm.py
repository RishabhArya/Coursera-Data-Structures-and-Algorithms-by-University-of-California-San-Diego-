# Uses python3
import sys


def gcd(c, d):
    if c == 0:
        return d
    return gcd(d % c, c)


def lcm(q, d):
    return int((q * d) / gcd(q, d))


if __name__ == '__main__':
    numbers = sys.stdin.read()
    a, b = map(int, numbers.split())
    print(lcm(a, b))
