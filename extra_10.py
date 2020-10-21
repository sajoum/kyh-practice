def main():
    for n in range(2000, 3201):
        if n % 7 == 0 and n % 5 != 0:
            print(n, ", ",
                  end="")  # Prints the number on a single comma-separated line. , end = "" prevents a line feed


if __name__ == '__main__':
    main()