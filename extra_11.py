def main():
    n = input("Enter a number: ")
    d = {}
    for i in range (1,int(n)+1):
       #kan också skrivas som i*i
        d[i] = i*2
    print (d)

if __name__ == '__main__':
    main()