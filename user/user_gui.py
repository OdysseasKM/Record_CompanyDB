import PySimpleGUI as sg
import user.user_functions_for_gui as uf


my_window_size = [800,350] #width, height
my_font = 'Helvetica 22'

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
    window = sg.Window(title,layout,font=my_font,size = my_window_size,resizable = True,finalize=True)

    while True:
        event, values = window.read()
        if event == "Exit" or event == sg.WINDOW_CLOSED:
            break
    window.close()

def select_genre_window():
    genres = ["Genres", uf.return_genre()]
    
    button1 = sg.ButtonMenu("Genres", menu_def=genres)
    button2 = sg.Button("Show",button_color="green")
    text1 = sg.Text("Please select a genre.")
    button3 = sg.Cancel("Exit",button_color="red")

    layout = [
        [text1,button1],
        [button2,button3]
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

def select_rel(text1,title,note):
    layout = [
        [sg.Text(text1)],
        [sg.Input()],
        [sg.Button('OK',button_color = "green"),sg.Button('Exit',button_color="red")],
        [sg.Text(note)]
    ]

    window = sg.Window(title,layout, font=my_font, size = my_window_size,resizable = True,finalize=True)
    
    while True:
        event, values = window.read()
        if event == "OK":
            window.close()
            value = values[0]
            if value=="":return True
            else: return value
        if event == "Exit" or event == sg.WINDOW_CLOSED:
            window.close()
            return False
    

def select_rating():
    stars = ["Stars",["1","2","3","4","5"]]
    
    button1 = sg.ButtonMenu("Stars", menu_def=stars)
    button2 = sg.Button('OK',button_color = "green")
    text1 = sg.Text("Please select a rate:")
    text2 = sg.Text('Stars: \n1 -  Poor\n2 -  Below average\n3 -  Good\n4 -  Very good\n5 -  Excellent')
    button3 = sg.Cancel("Exit",button_color="red")

    layout = [
        [text1,button1,button2],
        [text2],
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
    col_size=[25,25]
    print_window(headings,results,col_size, "Top Videos.")

def d_query7():
    results = uf.query5()
    headings=['Song', 'Artist', 'Avg Rating']
    col_size=[20,15,15]
    print_window(headings,results,col_size, "Top Songs.")

def d_query8():
    results = uf.query6()
    headings=['Album', 'Artist', 'Avg Rating']
    col_size=[20,15,15]
    print_window(headings,results,col_size, "Top Albums.")

def d_query2():
    genre = select_genre_window()
    if (genre!=0):
        headings=['Video', 'Views']
        col_size=[30,20]
        results = uf.query2(genre)
        print_window(headings,results,col_size,genre)

def d_query3():
    results = uf.query3()
    headings=['Artist', 'Average Rating']
    col_size=[30,20]
    print_window(headings,results,col_size, "Top artists")

def d_query4(note):
    text = "Type the name of the song:"
    title = "Select a song."
    name = select_rel(text,title,note)
    if (not name):return
    else:
        id = uf.find_song(name)
        if (not id):d_query4("The song does not exist.. please type again.")
        else : 
            results = uf.query4(id)
            headings=['Song Name',"Artist","genre",'Rating']
            col_size=[15,15,10,10]
            print_window(headings,results,col_size, "Relative Songs.")

def d_query5(note):
    text = "Type the name of the song:"
    title = "Select a song."
    name = select_rel(text,title,note)
    if (not name):return
    else:
        id = uf.find_song(name)
        if (not id):d_query5("The song does not exist.. please type again.")
        else : 
            rate=select_rating()
            if (not rate):return
            else: 
                uf.add_rating_for_song(int(id),int(rate))
                note = "You have submit rate (" + rate + "/5) in \n" + name
                uf.commit_db()
                d_query5(note)

def d_query6(note):
    text = "Type the name of the video:"
    title = "Select a video."
    name = select_rel(text,title,note)
    if (not name):return
    else:
        id = uf.find_video(name)
        if (not id):d_query6("The video does not exist.. please type again.")
        else : 
            rate=select_rating()
            if (not rate):return
            else: 
                uf.add_rating_for_video(int(id),int(rate))
                note = "You have submit rate (" + rate + "/5) in \n" + name
                uf.commit_db()
                d_query6(note)

def user_window():
    query1 = "Most viewed videos"
    query3 = "Top aritsts"
    query7 = "Top songs"
    query8 = "Top albums"
    query2 = "Most popular videos of specific genre"
    query4 = "Select a song and get back relative songs to this song"
    text1 = sg.Text("Rate a:")
    query5 = ["Rate a:",["song","video"]]


    layout =    [
                    [sg.Button(query3)],
                    [sg.Button(query7)],
                    [sg.Button(query8)],
                    [sg.Button(query1)],
                    [sg.Button(query2)],
                    [sg.Button(query4)],
                    [text1,sg.ButtonMenu("       ",menu_def=query5)],
                    [sg.Cancel(button_color="red")]
                ]

    window = sg.Window("Starting Window", layout, font=my_font, size = my_window_size, resizable=True)

    while True:
        event, values = window.read()
        if event == "Cancel":
            break
        elif event == query1:
            window.hide()
            d_query1()
            window.un_hide()
        elif event == query7:
            window.hide()
            d_query7()
            window.un_hide()
        elif event == query8:
            window.hide()
            d_query8()
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
        elif event == 0:
            window.hide()
            if values[0] == "song": d_query5("")
            elif values[0] == "video": d_query6("") 
            window.un_hide()
    uf.close_db()
    window.close()

def main():
    uf.open_db()
    user_window()
  

# if __name__ == '__main__':
#     main()



