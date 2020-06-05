# Uses python3
# Boyer Moore Majority Vote Algoithum
import sys


def check_majority_element(ar , majority_element):
    i = 0
    count = 0
    while i < len(ar):
        if ar[i] == majority_element:
            count = count + 1
        i = i + 1
    if count > len(ar)/2:
        return 1
    if count <= len(ar)/2:
        return -1
    return 0


def get_majority_element(a, left, right):
    if left == right:
        return -1
    if left + 1 == right:
        return a[left]
    majority_element = a[0]
    count = 1
    i = 1
    while i < right:
        current_element = a[i]
        if majority_element == current_element:
            count = count + 1
        if majority_element != current_element:
            count = count - 1
        if count == 0:
            majority_element = current_element
            count = 1
        i = i + 1
    result = check_majority_element(a, majority_element)
    if result == 1:
        return 1
    return -1


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    if get_majority_element(a, 0, n) != -1:
        print(1)
    else:
        print(0)
