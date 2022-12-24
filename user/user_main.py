import user_functions


def menu():
    print( """
    Press 1 to see 10 most viewed video clips.
    Press 2 to see most popular videos of specific genre.
    Press 3 to see videos from an artist.
    Press 4 to see relative songs with a song.
    Press 5 to see artist with best avg rating. 
    Press 6 to add a rating to song.
    Press -1 to exit.
    """)
    choice = int(input("type a number : "))
    return choice

def main():
    print("==== hello dear user ====")
    user_functions.open_db()
    while (1):
        choice = menu()
        if choice == 1: user_functions.query1()
        elif choice == 2: user_functions.query2()
        elif choice == 3: user_functions.query3()
        elif choice == 4: user_functions.query4()
        elif choice == 5: user_functions.query5()
        elif choice == 6: user_functions.query6(2,1)
        elif choice == -1: break
    user_functions.close_db()
    
if __name__ == '__main__':
    main()
