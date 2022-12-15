import user_functions


def menu():
    print( """Press 1 to see 10 most viewed video clips.
     Press 2 to see most popular songs of specific genre.
     Press 3 to see top artist by raitings.
     Press -1 to exit.""")
    choice = int(input())
    return choice

def main():
    print("==== hello dear user ====")
    user_functions.open_db()
    while (1):
        choice = menu()
        if choice == 1: user_functions.querie1()
        elif choice == 2: user_functions.querie2()
        elif choice == 3: user_functions.queries3()
        elif choice == -1: break

if __name__ == '__main__':
    main()
