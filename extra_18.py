def sum(list):
    result = 0
    for i in list:
        result += i
    return result


def multiply(list):
    product = 1
    for i in list:
        product *= i
    return product


def main():
    print(sum([1, 2, 3, 4]))
    print(multiply([1, 2, 3, 4]))


if __name__ == '__main__':
    main()



