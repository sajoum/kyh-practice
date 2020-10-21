'''Bygg ett program där användaren ser denna meny:

1. Lista TODO
2. Lägg till uppgift
3. Ta bort uppgift
4. Avbryt programmet

Programmet ska spara en fil "TODO.txt" som läses in i början, och innehåller en lista med saker att göra.
Listan kan manipuleras med alternativ 2 och 3.

När programmet avslutas sparas listan till TODO.txt (skrivs över).'''

from pathlib import Path

def mainmenu(todo_list):
        While True:\
        print("""
    1) Lista TODO
    2) Lägg till uppgift
    3) Ta bort uppgift
    4) Avbryt programmet
    """)
    if answer == 1:
        print_list(todo_list)
    if answer == 2:
        new_item = input("Vad vill du lägga till? ")
        todo_list.append(new_item)
    if answer == 3:
        print_list(todo_list)
        item_number = safe_input number("Vad har du gjort? ")
        if 0 < item_number <= len(todo_list):
            print()
            print(f"You have deleted task {todo_list[item_number - 1]}")
            del todo_list[item_number - 1]
        else:
            print(f"There is no task with than number")
        if answer == 4:
            return todo_list


        def print_list(todo_list):
            for i in range(len(todo_list)):
                print(f"{i + 1}. {todo_list[i]}")


        def safe_input_number(prompt):
            while True:
                try:
                    answer = input(prompt)
                    num = int(answer)
                    return num
                except ValueError:
                    print(f"{answer} är inte ett heltal!")

        if __name__ == '__main__':
            p = Path('TODO.txt')
            if not p.exists():
                p.write_text('')
            todo_list = p.read_text(encoding='utf8').splitlines()
            new_list = mainmenu(todo_list)
            p.write_text('\n'.join(new_list))