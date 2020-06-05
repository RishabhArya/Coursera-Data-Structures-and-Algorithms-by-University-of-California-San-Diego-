# python3
def SumOfDigits(firstNumber, secondNumber):
    return firstNumber + secondNumber


if __name__ == '__main__':
    x, y = map(int, input().split())
    print(SumOfDigits(x, y))
