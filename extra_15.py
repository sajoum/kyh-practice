def length(name):
    counter = 0
    for x in name:
        counter +=1
    return counter

def main():
    Str = "Hello there"
    print(length(Str))

    List = [1,2,3,4,5,6,7]
    print(length(List))

    Set = {1,2,3,4,54,66}
    print(length(Set))


if __name__ == '__main__':
    main()

