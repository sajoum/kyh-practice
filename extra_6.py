"Write a program that begins by reading the denomination of a banknote from the user."
"Then your program should display the name of the individual that appears on the banknote of the entered amount."
"An appropriate error message should be displayed if no such note exists."

def main():
    notes = {
        "1" : "George Washington",
        "2" : "Thomas Jefferson",
        "5" : "Abraham Lincoln",
        "10" : "Alexander Hamilton",
        "20" : "Andrew Jackson",
        "50" : "Ulysses S. Grant",
        "100" :  "Benjamin Franklin",
    }
    value = input("Enter banknote value: ")
    if value not in notes:
        print("Sorry, that is not a valid note")
    else:
        print("On that you will find a picture of", notes[value])

if __name__ == "__main__":
    main()

