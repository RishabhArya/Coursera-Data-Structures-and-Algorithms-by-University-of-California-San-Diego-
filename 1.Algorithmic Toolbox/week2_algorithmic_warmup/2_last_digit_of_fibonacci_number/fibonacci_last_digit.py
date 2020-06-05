# Uses python3


def fib(f, n):
    f[0] = 0
    f[1] = 1
    for i in range(2, n + 1):
        f[i] = (f[i - 1] + f[i - 2]) % 10

    return f


def findLastDigit(n):
    f = [0] * 61
    f = fib(f, 60)
    return f[n % 60]


if __name__ == '__main__':
    n = int(input())
    print(findLastDigit(n))
