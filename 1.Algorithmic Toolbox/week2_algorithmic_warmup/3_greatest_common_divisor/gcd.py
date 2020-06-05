# Uses python3
import sys


def gcd_euclidean(a, b):
    if a == 0:
        return b
    return gcd_euclidean(b % a, a)


if __name__ == "__main__":
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(gcd_euclidean(a, b))
