# python3

def max_pairwise_product(numbers):
    max_product = 0
    first = max(numbers)
    numbers.remove(first)
    second = max(numbers)
    max_product = first * second
    return max_product



if __name__ == '__main__':
    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    print(max_pairwise_product(input_numbers))
