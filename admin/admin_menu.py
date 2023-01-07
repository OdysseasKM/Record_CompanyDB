import PySimpleGUI as sg
import admin_functions as adm
import sqlite3
import datetime

my_window_size = [800,350] #width, height
my_font = 'Helvetica 22'


def admin_window():

    add_list = ["Insert", ["Artist", "Release", "Studio", "Format", "Individual"]]
    delete_list = ["Delete", ["Artist", "Release"]]
    inspect_list = ["Inspect", ["Bands", "Solo Artists", "Studio", "Contributor", "Individual", "Albums", "Singles", "Videos"]]

    layout =    [
                    [sg.Text("Insert  "),sg.ButtonMenu("       ", menu_def=add_list)],
                    [sg.Text("Delete "),sg.ButtonMenu("       ", menu_def=delete_list)],
                    [sg.Text("Inspect"),sg.ButtonMenu("       ", menu_def=inspect_list)],
                    [sg.Button("Annual Revenue")],
                    [sg.Button("Studios With the most recordings")],
                    [sg.Button("Most Profitable Artists")],
                    [sg.Cancel(button_color="red")]
                ]
    window	=	sg.Window("Data	Entry Form", layout, font=my_font,size=my_window_size)
    event, values=window.read()	
    window.close()

    if event == "Cancel":
        window.close()

    elif event == 0:
 
        if values[0] == "Artist":
            add_artist_window()
            admin_window()

        elif values[0] == "Release":
            add_release_window()
            admin_window()

        elif values[0] == "Studio":
            add_studio_window()
            admin_window()

        elif values[0] == "Format":
            add_format_window()
            admin_window()

        elif values[0] == "Individual":
            add_individual_window()
            admin_window()
            

    elif event == 1:
        if values[1] == "Artist":
            name = delete_artist_window()
            adm.delete_artist(name)
            admin_window()

        elif values[1] == "Release":
            idn = delete_release_window()
            adm.delete_release(idn)
            admin_window()

    elif event==2:
 
        if values[2] == "Bands":
            results=adm.find_all("Artist")
            headings=['Nickname', 'Country']
            print_window(headings, results, [25,25])
            admin_window()

        if values[2] == "Solo Artists":
            results=adm.find_all("Artist")
            headings=['Nickname', 'Country']
            print_window(headings, results, [25,25])
            admin_window()

        elif values[2] == "Studio":
            results=adm.find_all("Studio")
            headings=['Studio_id', 'Town']
            print_window(headings, results, [25,25])
            admin_window()

        elif values[2] == "Contributor":
            results=adm.find_all("Contributor")
            headings=['Ssn', 'First Name', 'Last Name', 'Role']
            print_window(headings, results, [10,15,15,10])
            admin_window()

        elif values[2] == "Albums":
            results=adm.find_all("Albums")
            headings=['Release_title', 'Artist']
            print_window(headings, results, [25,25])
            admin_window()

        elif values[2] == "Singles":
            results=adm.find_all("Singles")
            headings=['Release_title', 'Artist']
            print_window(headings, results, [25,25])
            admin_window()

        elif values[2] == "Videos":
            results=adm.find_all("Videos")
            headings=['Release_title', 'Artist']
            print_window(headings, results, [25,25])
            admin_window()

    elif event == 'Annual Revenue':
        year=year_window()
        results=adm.annual_revenue(year)
        print(results)
        # headings=['revenue']
        # print_window(headings, results, [25])
        # admin_window()

    elif event == 'Studios With the most recordings':
        results=adm.studios()
        headings=['Studio_id', 'Recordings']
        print_window(headings, results, [25,25])
        admin_window()

    elif event == 'Most Profitable Artists':
        results=adm.artist_profit()
        headings=['Artist', 'Profit']
        print_window(headings, results, [25,25])
        admin_window()
        

def add_artist_window():

    layout =    [
                    [sg.Text('Please Enter the following information', font=my_font)],[sg.VPush()],
                    [sg.Text('Artist Nickname',size=(12,1),font=my_font), sg.InputText(font=my_font)], [sg.VPush()],	
                    [sg.Text('Artist Country',size=(12,1),font=my_font), sg.InputText(font=my_font)], [sg.VPush()],
                    [sg.Submit(key="-SUMBIT-",button_color="green",font=my_font),sg.VPush(),sg.Cancel(button_color="red",font=my_font)]
                ]
    window = sg.Window("Add Artist Window", layout, font=my_font, size = my_window_size, resizable=True, modal=True)
    event, values = window.read()

    if event == "Cancel":
        window.close()	
    if	event	==	"-SUMBIT-":
        adm.add_artist(values[0], values[1])
        window.close()

def add_format_window():

    layout =    [
                    [sg.Text('Please Enter the following information', font=my_font)],[sg.VPush()],
                    [sg.Text('Release Id',size=(12,1),font=my_font), sg.InputText(font=my_font)], [sg.VPush()],	
                    [sg.Text('Price',size=(12,1),font=my_font), sg.InputText(font=my_font)], [sg.VPush()],
                    [sg.Text('Please Choose the Format', font=my_font)],[sg.VPush()],
                    [sg.CB("Vinyl", key="Vinyl")],
                    [sg.CB("CD", key="CD")],
                    [sg.CB("Digital", key="Digital")],
                    [sg.Submit(key="-SUMBIT-",button_color="green",font=my_font) , sg.VPush(),sg.Cancel(button_color="red",font=my_font)]
                ]

    window = sg.Window("Add Format Window", layout, font=my_font, size = my_window_size, resizable=True, modal=True)
    event, values = window.read()

    if event == "Cancel":
        window.close()	
    if	event	==	"-SUMBIT-":
        if values["Vinyl"]==True:
            adm.add_format(values[0], 1, cost=values[1])
        elif values["CD"]==True:
            adm.add_format(values[0], 2, cost=values[1])
        elif values["Digital"]==True:
            adm.add_format(values[0], 3)
        window.close()


def add_studio_window():

    layout =    [
                    [sg.Text('Please Enter the following information', font=my_font)],[sg.VPush()],
                    [sg.Text('Street Name',size=(12,1),font=my_font), sg.InputText(font=my_font)], [sg.VPush()],
                    [sg.Text('Number',size=(12,1),font=my_font), sg.InputText(font=my_font)], [sg.VPush()],
                    [sg.Text('Town',size=(12,1),font=my_font), sg.InputText(font=my_font)], [sg.VPush()],
                    [sg.Text('Country',size=(12,1),font=my_font), sg.InputText(font=my_font)], [sg.VPush()],
                    [sg.Submit(key="-SUMBIT-",button_color="green",font=my_font),sg.VPush(),sg.Cancel(button_color="red",font=my_font)]
                ]
    window = sg.Window("Add Artist Window", layout, font=my_font, size = my_window_size, resizable=True, modal=True)
    event,values = window.read()	

    if event == "Cancel":
        window.close()
    if	event	==	"-SUMBIT-":
        adm.add_studio(values[0], values[1], values[2], values[3])
        
        window.close()
    

def add_contributor_window(release_name):

    layout =    [
                    [sg.Text('Please Enter the following information',font=my_font)],[sg.VPush()],
                    [sg.Text('Ssn',size=(12,1),font=my_font), sg.InputText(font=my_font)], [sg.VPush()],
                    [sg.Text('First Name',size=(12,1),font=my_font), sg.InputText(font=my_font)], [sg.VPush()],
                    [sg.Text('Last Name',size=(12,1),font=my_font), sg.InputText(font=my_font)], [sg.VPush()],
                    [sg.Text('Role',size=(12,1),font=my_font), sg.InputText(font=my_font)], [sg.VPush()],
                    [sg.Submit(key="-SUMBIT-",font=my_font,button_color="green"),sg.VPush(),sg.Cancel(button_color="red",font=my_font)]
                ]
    window = sg.Window("Add Contributor Window", layout, font=my_font, size = my_window_size, resizable=True, modal=True)
    event,values = window.read()	

    if event == "Cancel":
        window.close()
    if	event	==	"-SUMBIT-":
        adm.add_contributor(release_name, values[0], values[1], values[2], values[3])
        
        window.close()
        add_contributor_window(release_name)

def add_individual_window():

    layout =    [
                    [sg.Text("Please Enter the following information",font=my_font)],[sg.VPush()],
                    [sg.Text("Artist Nickname",font=my_font), sg.InputText(font=my_font)], [sg.VPush()],
                    [sg.Submit(key="-SUMBIT-",font=my_font,button_color="green"),sg.VPush(),sg.Cancel(button_color="red",font=my_font)]
                ]
    window = sg.Window("Add Individual Window", layout, font=my_font, size = my_window_size, resizable=True, modal=True)
    event,values = window.read()
    
    if event == "Cancel":
        window.close()	
    if	event	==	"-SUMBIT-":
        window.close()
        values[1], values[2], values[3] = individual_details_window()
        adm.add_individual(values[1], values[2], values[3], values[0])

def individual_details_window():

    layout =    [
                    [sg.Text('Please Enter the following information',font=my_font)],[sg.VPush()],
                    [sg.Text('Ssn',size=(10,1),font=my_font), sg.InputText(font=my_font)], [sg.VPush()],
                    [sg.Text('First Name',size=(10,1),font=my_font), sg.InputText(font=my_font)], [sg.VPush()],
                    [sg.Text('Last Name',size=(10,1),font=my_font), sg.InputText(font=my_font)], [sg.VPush()],
                    [sg.Submit(key="-SUMBIT-",button_color="green",font=my_font) , sg.VPush(),sg.Cancel(button_color="red")]
                ]
    window = sg.Window("Add Individual Window", layout, font=my_font, size = my_window_size, resizable=True, modal=True)
    event,values = window.read()	

    if event == "Cancel":
        window.close()
    if	event	==	"-SUMBIT-":
        window.close()
        return(values[0], values[1], values[2])
        
def add_release_window():
    my_font = 'Helvetica 16'
    layout =    [ 
                    [sg.Text('Please Enter the following information', font=my_font)],[sg.VPush()],
                    [sg.Text('Artist Nickname',size=(12,1),font=my_font), sg.InputText(font=my_font)], [sg.VPush()],
                    [sg.Text('Release Name',size=(12,1),font=my_font), sg.InputText(font=my_font)], [sg.VPush()],
                    [sg.Text('Release Genre',size=(12,1),font=my_font), sg.InputText(font=my_font)], [sg.VPush()],
                    [sg.Text('Choose the Release Type', font=my_font), sg.VPush(), sg.Text('        Choose the Format', font=my_font),sg.VPush()],
                    [sg.CB("  Album \t\t\t", key="Album"), sg.CB("  Vinyl", key="Vinyl")],
                    [sg.CB("  Video \t\t\t", key="Video"), sg.CB("  CD", key="CD")],
                    [sg.CB("  Single\t\t\t", key="Single"),sg.CB("  Digital", key="Digital")],
                    [sg.Submit(key="-SUMBIT-",font=my_font,button_color="green"),sg.VPush(),sg.Cancel(button_color="red",font=my_font)]
                ]

    window = sg.Window("Add Release Window",layout, font=my_font, size = my_window_size, resizable=True, modal=True)
    event, values = window.read()	
    if event == "Cancel":
        window.close()
    if	event	==	"-SUMBIT-":
        if values["Album"]==True:
            if values["Vinyl"]==True:
                values[3]=price_window()
                adm.add_release(values[0], values[1], "Album", values[2], Format="Vinyl", cost=values[3])
            elif values["CD"]==True:
                values[3]=price_window()
                adm.add_release(values[0], values[1], "Album", values[2], Format="CD", cost=values[3])
            elif values["Digital"]==True:
                adm.add_release(values[0], values[1], "Album", values[2], Format="Online")
            else:
                adm.add_release(values[0], values[1], "Album", values[2])
            window.close()
            song_window(values[1])
            
        elif values["Video"]==True:
            values[3]=duration_window()
            values[4]= videoclip_window()
            adm.add_release(values[0], values[1], "Video", values[2], Format="Digital", duration=values[3], song_name=values[4])

        elif values["Single"]==True:
            values[3], values[4], values[5]= single_window()
            if values["Vinyl"]==True:
                values[6]=price_window()
                adm.add_release(values[0], values[1], "Single", values[2], Format="Vinyl",duration=values[3], studio_id=values[4], language=values[5], cost=values[6])
            elif values["CD"]==True:
                values[6]=price_window()
                adm.add_release(values[0], values[1], "Single", values[2], Format="CD",duration=values[3], studio_id=values[4], language=values[5], cost=values[6])    
            elif values["Digital"]==True:
                adm.add_release(values[0], values[1], "Single", values[2], Format="Online",duration=values[3], studio_id=values[4], language=values[5])
            else:
                adm.add_release(values[0], values[1], "Single", values[2], duration=values[3], studio_id=values[4], language=values[5])
        window.close()
        # add_contributor_window(values[1])

def duration_window():

    layout =    [
                    [sg.Text("Please Enter the following information", font=my_font)],[sg.VPush()],
                    [sg.Text("Duration(sec)",size=(15,1),font=my_font), sg.InputText(font=my_font)], [sg.VPush()],
                    [sg.Submit(key="-SUMBIT-",button_color="green",font=my_font) , sg.VPush(),sg.Cancel(button_color="red")]
                ]
    window = sg.Window("Duration Window",layout, font=my_font, size = my_window_size, resizable=True, modal=True)
    event,values = window.read()
    
    if event == "Cancel":
        window.close()	
    if	event	==	"-SUMBIT-":
        window.close()
        return values[0]
    
def price_window():

    layout =    [
                    [sg.Text("Please Enter the following information",font=my_font)],[sg.VPush()],
                    [sg.Text("Format Price",size=(15,1),font=my_font), sg.InputText(font=my_font)], [sg.VPush()],
                    [sg.Submit(key="-SUMBIT-",button_color="green",font=my_font), sg.VPush(),sg.Cancel(button_color="red")]
                ]
    window = sg.Window("Price Window", layout, font=my_font, size = my_window_size, resizable=True, modal=True)
    event,values = window.read()
    
    if event == "Cancel":
        window.close()	
    if	event	==	"-SUMBIT-":
        window.close()
        return values[0]

def videoclip_window():

    layout =    [
                    [sg.Text("Please Enter the song's name for the videoclip", font=my_font)],[sg.VPush()],
                    [sg.Text("song name",size=(15,1),font=my_font), sg.InputText(font=my_font)], [sg.VPush()],
                    [sg.Submit(key="-SUMBIT-",button_color="green",font=my_font), sg.VPush(),sg.Cancel(button_color="red")]
                ]
    window = sg.Window("Videoclip Window", layout, font=my_font, size = my_window_size, resizable=True, modal=True)
    event,values = window.read()
    
    if event == "Cancel":
        window.close()	
    if	event	==	"-SUMBIT-":
        window.close()
        return values[0]
    

def single_window():

    layout =    [
                    [sg.Text('Please Enter the following information', font=my_font)],[sg.VPush()],
                    [sg.Text('Duration(sec)',size=(15,1),font=my_font), sg.InputText(font=my_font)], [sg.VPush()],
                    [sg.Text('Studio Id',size=(15,1),font=my_font), sg.InputText(font=my_font)], [sg.VPush()],
                    [sg.Text('Language',size=(15,1),font=my_font), sg.InputText(font=my_font)], [sg.VPush()],
                    [sg.Submit(key="-SUMBIT-",button_color="green",font=my_font) , sg.VPush(),sg.Cancel(button_color="red")]
                ]
    window = sg.Window("Add Single Window", layout, font=my_font, size = my_window_size, resizable=True, modal=True)
    event,values = window.read()

    if event == "Cancel":
        window.close()
    if event ==	"-SUMBIT-":
        window.close()
        return values[0], values[1], values[2]

    
def song_window(album_name):

    layout =    [
                    [sg.Text('Please Enter the following information to add a song to the album',font=my_font)],[sg.VPush()],
                    [sg.Text('Name',size=(15,1),font=my_font), sg.InputText(font=my_font)], [sg.VPush()],
                    [sg.Text('Duration(sec)',size=(15,1),font=my_font), sg.InputText(font=my_font)], [sg.VPush()],
                    [sg.Text('Studio Id',size=(15,1),font=my_font), sg.InputText(font=my_font)], [sg.VPush()],
                    [sg.Text('Language',size=(15,1),font=my_font), sg.InputText(font=my_font)], [sg.VPush()],
                    [sg.Submit(key="-SUMBIT-",button_color="green",font=my_font) , sg.VPush(),sg.Cancel(button_color="red")]
                ]
    window = sg.Window("Add Single Window", layout, font=my_font, size = my_window_size, resizable=True, modal=True)
    event,values = window.read()

    if event == "Cancel":
        window.close()
    if event ==	"-SUMBIT-":
        adm.add_song(None, album_name, values[1], values[2], values[3], values[0])
        window.close()
        song_window(album_name)
        

def year_window():

    layout =    [
                    [sg.Text("Please Enter the following information", font=my_font)],[sg.VPush()],
                    [sg.Text("Year",size=(15,1),font=my_font), sg.InputText(font=my_font)], [sg.VPush()],
                    [sg.Submit(key="-SUMBIT-",button_color="green",font=my_font) , sg.VPush(),sg.Cancel(button_color="red")]
                ]
    window = sg.Window("Year Window", layout, font=my_font, size = my_window_size, resizable=True, modal=True)
    event,values = window.read()

    if event == "Cancel":
        window.close()	
    if	event	==	"-SUMBIT-":
        window.close()
        return values[0]

def delete_release_window():

    layout =    [
                    [sg.Text("Please Enter the following information",font=my_font)],[sg.VPush()],
                    [sg.Text("Release Id",size=(15,1),font=my_font), sg.InputText(font=my_font)], [sg.VPush()],
                    [sg.Submit(key="-SUMBIT-",button_color="green",font=my_font) , sg.VPush(),sg.Cancel(button_color="red")]
                ]
    window = sg.Window("Delete Window", layout, font=my_font, size = my_window_size, resizable=True, modal=True)
    event,values = window.read()

    if event == "Cancel":
        window.close()	
    if	event	==	"-SUMBIT-":
        return values[0]

def delete_artist_window():

    layout =    [
                    [sg.Text("Please Enter the following information",font=my_font)],[sg.VPush()],
                    [sg.Text("Artist nickname",size=(15,1),font=my_font), sg.InputText(font=my_font)], [sg.VPush()],
                    [sg.Submit(key="-SUMBIT-",button_color="green",font=my_font) , sg.VPush(),sg.Cancel(button_color="red")]
                ]
    window = sg.Window("Delete Window", layout, font=my_font, size = my_window_size, resizable=True, modal=True)
    event,values = window.read()

    if event == "Cancel":
        window.close()	
    if	event	==	"-SUMBIT-":
        return values[0]

def print_window(headings, data, my_col_size):

    layout =    [
                    [sg.Table(data, headings=headings,auto_size_columns=False,col_widths=my_col_size, justification='left', key='-TABLE-')],
                    [[sg.Button("Back",button_color="red")]]
                ]
    window = sg.Window("Title", layout, font=my_font, size = my_window_size, resizable=True, modal=True)

    while True:
        event, values = window.read()
        if event == sg.WINDOW_CLOSED or event=="Back":
            break

    window.close()



def main():
    db = sqlite3.connect('record-company.db')
    cursor = db.cursor()
    admin_window()
  

if __name__ == '__main__':
    main()



