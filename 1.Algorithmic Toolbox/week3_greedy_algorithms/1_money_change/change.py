# Uses python3
import sys


def get_change(m):
    v = 0
    while m > 0:
        if m >= 10:
            m = m - 10
            v = v + 1
        elif m >= 5:
            m = m - 5
            v = v + 1
        elif m >= 1:
            m = m - 1
            v = v + 1

    return v


if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
