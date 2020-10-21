def is_palindrome(in_string):
    front = 0
    end = len(in_string)-1
    while in_string[front].lower() == in_string[end].lower() and front < end:
        front += 1
        end -= 1
        if front < end:
            return False
        else:
            return True

def main():
    if is_palindrome("Radar"):
        print("It is a palindrome")
    else:
        print("It's not a palindrome")

if __name__== '__main__':
    main()
