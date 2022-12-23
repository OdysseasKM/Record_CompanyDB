import PySimpleGUI as sg
import user_functions_for_gui as uf

my_window_size = [500,300] #width, height
my_font = 'Helvetica 16'

def print_window(headings,results,my_col_size,title):
    headings = headings
    data = results

    layout = [
        [sg.Table(data, headings=headings,
            auto_size_columns = False,
            col_widths = my_col_size,
            justification='left',
            num_rows=10,
            key = '-TABLE-')],
        [sg.Cancel("Exit",button_color="red")]
    ]
    window = sg.Window(title, layout,layout, font=my_font, size = my_window_size,resizable = True,finalize=True)

    while True:
        event, values = window.read()
        if event == "Exit" or event == sg.WINDOW_CLOSED:
            break
    window.close()

def select_genre_window():
    genres = ["Genres", uf.return_genre()]
    
    button1 = sg.ButtonMenu("Genres", menu_def=genres)
    button2 = sg.Button("Show")
    text1 = sg.Text("Please select a genre.")
    button3 = sg.Cancel("Exit",button_color="red")

    layout = [
        [text1,button1,button2],
        [button3]
    ]

    window = sg.Window("Select Genre", layout, font=my_font, size = my_window_size,resizable = True,finalize=True)
    genre = ""
    while True:
        event, values = window.read()
        if event == "Exit" or event == sg.WINDOW_CLOSED:
            break
        elif event == 0:
            genre = values[0]
        elif event == "Show":
            if (genre!=""):
                window.close()
                return genre
    window.close()
    return 0                     

def select_song(text):
    layout = [
        [sg.Text('Enter a song name:')],
        [sg.Input(),sg.Button('OK')],
        [sg.Button('Exit')],
        [sg.Text(text)]
    ]

    window = sg.Window("Select a song",layout, font=my_font, size = my_window_size,resizable = True,finalize=True)
    
    while True:
        event, values = window.read()
        if event == "OK" or event == sg.WINDOW_CLOSED:
            break
        if event == "Exit":
            window.close()
            return False

    window.close()
    return values[0]

def select_rating():
    stars = ["1","2","3","4","5"]
    
    button1 = sg.ButtonMenu("Stars", menu_def=stars)
    button2 = sg.Button('OK')
    text1 = sg.Text("Please select a rate.")
    button3 = sg.Cancel("Exit",button_color="red")

    layout = [
        [text1,button1,button2],
        [button3]
    ]

    window = sg.Window("Select Rate", layout, font=my_font, size = my_window_size,resizable = True,finalize=True)
    rate = ""
    while True:
        event, values = window.read()
        if event == "Exit" or event == sg.WINDOW_CLOSED:
            break
        elif event == 0:
            rate = values[0]
        elif event == "OK":
            if (rate!=""):
                window.close()
                return rate
    window.close()
    return False

def d_query1():
    results = uf.query1()
    headings=['Video', 'Views']
    col_size=[20,20]
    print_window(headings,results,col_size, "Top 10 Videos.")

def d_query2():
    genre = select_genre_window()
    if (genre!=0):
        headings=['Video', 'Views']
        col_size=[20,20]
        results = uf.query2(genre)
        print_window(headings,results,col_size,genre)

def d_query3():
    results = uf.query3()
    headings=['Artist', 'Average Rating']
    col_size=[20,20]
    print_window(headings,results,col_size, "Top artists")

def d_query4(note):
    song_name = select_song(note)
    if (not song_name):return
    else:
        id = uf.find_song(song_name)
        if (not id):d_query4("The song does not exist.. please type again.")
        else : 
            results = uf.query4(id)
            headings=['Song Name',"Artist","genre",'Rating']
            col_size=[10,10,10,10]
            print_window(headings,results,col_size, "Relative Songs.")

def d_query5(note):
    song_name = select_song(note)
    if (not song_name):return
    else:
        id = uf.find_song(song_name)
        if (not id):d_query5("The song does not exist.. please type again.")
        else : 
            rate=select_rating()
            if (not rate):return
            else: uf.query5(int(id),int(rate))

def starting_window():
    query1 = "Top 10 video."
    query2 = "Most popular videos of specific genre."
    query3 = "Top aritsts."
    query4 = "Select a song and get back relative songs to this song."
    query5 = "Add a rating to song."
    query6 = "Add a rating to video."
    query7 = "Add a rating to album."
    
    layout =    [
                    [sg.Button(query1)],
                    [sg.Button(query2)],
                    [sg.Button(query3)],
                    [sg.Button(query4)],
                    [sg.Button(query5)],
                    [sg.Button(query6)],
                    [sg.Button(query7)],
                    [sg.Cancel(button_color="red")]
                ]

    window	=	sg.Window("Starting Window", layout, font=my_font, size = my_window_size, resizable=True)

    while True:
        event, values = window.read()
        if event == "Cancel":
            break
        elif event == query1:
            window.hide()
            d_query1()
            window.un_hide()
        elif event == query2:
            window.hide()
            d_query2()
            window.un_hide()
        elif event == query3:
            window.hide()
            d_query3()
            window.un_hide()
        elif event == query4:
            window.hide()
            d_query4("")
            window.un_hide()
        elif event == query5:
            window.hide()
            d_query5("")
            window.un_hide()
        # elif event == query6:
        #     window.hide()
        #     d_query6()
        #     window.un_hide()
        # elif event == query7:
        #     window.hide()
        #     d_query7()
        #     window.un_hide()

    window.close()


def main():
    uf.open_db()
    starting_window()
  

if __name__ == '__main__':
    main()



