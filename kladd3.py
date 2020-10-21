

if __name__ == '__main__':
    try:
        number = int(input("Hur många frågor? "))
        max_value = int(input("Största tal? "))
        game(number, max_value)
    except:
        print("Oj, här blev det fel!")