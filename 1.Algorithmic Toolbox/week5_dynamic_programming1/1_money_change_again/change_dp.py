# Uses python3
import sys


def get_change(V):
    coins = [1, 3, 4]
    m = len(coins)
    table = [0 for i in range(V + 1)]
    # Base case (If given value V is 0)
    table[0] = 0

    # Initialize all table values as Infinite
    for i in range(1, V + 1):
        table[i] = sys.maxsize

    # Compute minimum coins required
    # for all values from 1 to V
    for i in range(1, V + 1):
        # Go through all coins smaller than i
        for j in range(m):
            if coins[j] <= i:
                sub_res = table[i - coins[j]]
                if sub_res != sys.maxsize and sub_res + 1 < table[i]:
                    table[i] = sub_res + 1
                    print(table[i])
    print(table)
    return table[V]


if __name__ == '__main__':
    money = int(sys.stdin.read())
    print(get_change(money))
