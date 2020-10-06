'''Funktion som
beräknar/tar  maximum av 3 tal'''

def main():
    max_value = calc_max(60, 9, 8)
    print(max_value)

    integers = [1, 2, 3]

    summation = calculate_sum(integers)
    print(summation)

    summation2 = calculate_sum([3, 5, 7])
    print(summation2)

    integers = [3, 5, 9]

def calc_max(a, b, c):
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    elif c > a and c > b:
        return c



def calculate_sum(integers):
    summa = 0
    for tal in integers:
        summa += tal
    return summa



def multiply(integers):
    product = 1
    for tal in integers:
        product *= tal
    return product

if __name__ == '__main__':
    main()