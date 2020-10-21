def max_of_three(a, b, c):
    if a > b and a > c:
        return a
    if b > a and b > c:
        return b
    else:
        return c

def main():
    biggest = max_of_three(2, 5, 3)
    print(biggest)

if __name__ == '__main__':
    main()



