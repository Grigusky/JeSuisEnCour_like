# coding: utf-8


def main():
    menu = ["welcome on the migrations place", "you can do:", "\t- docker action [d]", "\t- git action [g]"]

    for m in menu:
        print(m)
    choice = input("votre choix: ")
    if choice == 'd':
        menuDocker()
        choice2 = input("votre choix: ")
        if choice2 == "ci":
            print("créer un container")
        elif choice2 == "cd":
            print()
        elif choice2 == "k":
            print()
        elif choice2 == "r":
            print()
    elif choice == 'g':
        menuGit()
        choice2 = input("votre choix: ")
        if choice2 == "c":
            print("clone")
        elif choice2 == "pl":
            print("pull")
        elif choice2 == "a":
            print("add")
        elif choice2 == "c":
            print("commit")
        elif choice2 == "ps":
            print("push")
        elif choice2 == "*":
            print("all")
    return 0


def menuDocker():
    menuDocker = [
        "vous pouvez maintenant:",
        "creer une nouveau container à partir d'une image [ci]",
        "creer une nouveau container à partir d'un dockerfile[cd]",
        "kill un container [k]",
        "rm un container [r]"
    ]
    for md in menuDocker:
        print(md)


def menuGit():
    menuGit = [
        "vous pouvez maintenant:",
        "cloner un repo git [c]",
        "pull un repo git [pl]",
        "add un fichier ou groupe de fichier [a]",
        "commit un fichier ou groupe de fichier [c]",
        "push un fichier ou groupe de fichier [ps]",
        "add commit et push d'un coup [*]"
    ]
    for mg in menuGit:
        print(mg)

if __name__ == "__main__":
    main()