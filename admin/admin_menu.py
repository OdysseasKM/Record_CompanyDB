import PySimpleGUI as sg
import admin_functions as adm
import sqlite3
import datetime

def admin_window():

    add_list = ["Insert", ["Artist", "Release", "Studio", "Format", "Individual"]]
    delete_list = ["Delete", ["Artist", "Release"]]
    inspect_list = ["Inspect", ["Artist", "Release", "Studio", "Contributor", "Individual"]]

    layout =    [
                    [sg.ButtonMenu("Insert", menu_def=add_list , size=(20,4))],
                    [sg.ButtonMenu("Delete", menu_def=delete_list , size=(20,4))],
                    [sg.ButtonMenu("Inspect", menu_def=inspect_list , size=(20,4))],
                    [sg.Button("Annual Revenue", size=(20,4))],
                    [sg.Button("Studios With the most recordings",  size=(20,4))],
                    [sg.Cancel(button_color="red")]
                ]
    window	=	sg.Window("Data	Entry Form", layout, size=(500,500))
    event, values=window.read()	
    window.close()
    if event == "Cancel":
        window.close()

    elif event == 0:
 
        if values[0] == "Artist":
            add_artist_window()
            
        elif values[0] == "Release":
            add_release_window()

        elif values[0] == "Studio":
            add_studio_window()
            
        elif values[0] == "Format":
            add_format_window()

        elif values[0] == "Individual":
            add_individual_window()
            

    elif event == 1:

        if values[1] == "Artist":
            name = delete_artist_window()
            adm.delete_artist(name)
            popup_window()

        elif values[1] == "Release":
            idn = delete_release_window()
            adm.delete_release(idn)
            popup_window()

    elif event==2:
 
        if values[2] == "Artist":
            results=adm.find_all("Artist")
            headings=['Nickname', 'Country']
            print_window(headings, results)
            
        elif values[2] == "Release":
            results=adm.find_all("Release")
            headings=['Release_title', 'Artist']
            print_window(headings, results)

        elif values[2] == "Studio":
            results=adm.find_all("Studio")
            headings=['Studio_id', 'Town']
            print_window(headings, results)

        elif values[2] == "Contributor":
            results=adm.find_all("Contributor")
            headings=['Ssn', 'First Name', 'Last Name', 'Role']
            print_window(headings, results)

    elif event == 3:
        year=year_window()
        adm.annual_revenue(year)

        

def add_artist_window():

    layout =    [
                    [sg.Text('Please Enter the following information', font=("Courier",18))],[sg.VPush()],
                    [sg.Text('Artist Nickname',	size=(15,1),font=("Courier",18)), sg.InputText(font=("Courier",	18))], [sg.VPush()],	
                    [sg.Text('Artist Country',size=(15,1),font=("Courier",18)), sg.InputText(font=("Courier",18))], [sg.VPush()],
                    [sg.Submit(key="-SUMBIT-",font=("Courier",18))],[sg.VPush()],
                    [sg.Cancel(button_color="red")]
                ]
    window = sg.Window("Add Artist Window", layout, modal=True)
    event, values = window.read()

    if event == "Cancel":
        window.close()	
    if	event	==	"-SUMBIT-":
        adm.add_artist(values[0], values[1])
        window.close()
        popup_window()

def add_format_window():

    layout =    [
                    [sg.Text('Please Enter the following information', font=("Courier",18))],[sg.VPush()],
                    [sg.Text('Release Id',	size=(15,1),font=("Courier",18)), sg.InputText(font=("Courier",	18))], [sg.VPush()],	
                    [sg.Text('Price',size=(15,1),font=("Courier",18)), sg.InputText(font=("Courier",18))], [sg.VPush()],
                    [sg.Text('Please Choose the Format', font=("Courier",18))],[sg.VPush()],
                    [sg.CB("Vinyl", key="Vinyl")],
                    [sg.CB("CD", key="CD")],
                    [sg.CB("Digital", key="Digital")],
                    [sg.Submit(key="-SUMBIT-",font=("Courier",18))],[sg.VPush()],
                    [sg.Cancel(button_color="red")]
                ]

    window = sg.Window("Add Artist Window", layout, modal=True)
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
        popup_window()

def add_studio_window():

    layout =    [
                    [sg.Text('Please Enter the following information', font=("Courier",18))],[sg.VPush()],
                    [sg.Text('Street Name',size=(15,1),font=("Courier",18)), sg.InputText(font=("Courier",18))], [sg.VPush()],
                    [sg.Text('Number',size=(15,1),font=("Courier",18)), sg.InputText(font=("Courier",18))], [sg.VPush()],
                    [sg.Text('Town',size=(15,1),font=("Courier",18)), sg.InputText(font=("Courier",18))], [sg.VPush()],
                    [sg.Text('Country',size=(15,1),font=("Courier",18)), sg.InputText(font=("Courier",18))], [sg.VPush()],
                    [sg.Submit(key="-SUMBIT-",font=("Courier",18))],[sg.VPush()],
                    [sg.Cancel(button_color="red")]
                ]
    window = sg.Window("Add Artist Window", layout, modal=True)
    event,values = window.read()	

    if event == "Cancel":
        window.close()
    if	event	==	"-SUMBIT-":
        adm.add_studio(values[0], values[1], values[2], values[3])
        
        window.close()
        popup_window()

def add_contributor_window(release_name):

    layout =    [
                    [sg.Text('Please Enter the following information', font=("Courier",18))],[sg.VPush()],
                    [sg.Text('Ssn',size=(15,1),font=("Courier",18)), sg.InputText(font=("Courier",18))], [sg.VPush()],
                    [sg.Text('First Name',size=(15,1),font=("Courier",18)), sg.InputText(font=("Courier",18))], [sg.VPush()],
                    [sg.Text('Last Name',size=(15,1),font=("Courier",18)), sg.InputText(font=("Courier",18))], [sg.VPush()],
                    [sg.Text('Role',size=(15,1),font=("Courier",18)), sg.InputText(font=("Courier",18))], [sg.VPush()],
                    [sg.Submit(key="-SUMBIT-",font=("Courier",18))],[sg.VPush()],
                    [sg.Cancel(button_color="red")]
                ]
    window = sg.Window("Add Contributor Window", layout, modal=True)
    event,values = window.read()	

    if event == "Cancel":
        window.close()
    if	event	==	"-SUMBIT-":
        adm.add_contributor(release_name, values[0], values[1], values[2], values[3])
        
        window.close()
        popup_window()
        add_contributor_window(release_name)

def add_individual_window():

    layout =    [
                    [sg.Text("Please Enter the following information", font=("Courier",18))],[sg.VPush()],
                    [sg.Text("Artist Nickname",size=(15,1),font=("Courier",18)), sg.InputText(font=("Courier",18))], [sg.VPush()],
                    [sg.Submit(key="-SUMBIT-",font=("Courier",18))],[sg.VPush()],
                    [sg.Cancel(button_color="red")]
                ]
    window = sg.Window("Duration Window", layout, modal=True)
    event,values = window.read()
    
    if event == "Cancel":
        window.close()	
    if	event	==	"-SUMBIT-":
        window.close()
        values[1], values[2], values[3] = individual_details_window()
        adm.add_individual(values[1], values[2], values[3], values[0])
        popup_window()

def individual_details_window():

    layout =    [
                    [sg.Text('Please Enter the following information', font=("Courier",18))],[sg.VPush()],
                    [sg.Text('Ssn',size=(15,1),font=("Courier",18)), sg.InputText(font=("Courier",18))], [sg.VPush()],
                    [sg.Text('First Name',size=(15,1),font=("Courier",18)), sg.InputText(font=("Courier",18))], [sg.VPush()],
                    [sg.Text('Last Name',size=(15,1),font=("Courier",18)), sg.InputText(font=("Courier",18))], [sg.VPush()],
                    [sg.Submit(key="-SUMBIT-",font=("Courier",18))],[sg.VPush()],
                    [sg.Cancel(button_color="red")]
                ]
    window = sg.Window("Add Individual Window", layout, modal=True)
    event,values = window.read()	

    if event == "Cancel":
        window.close()
    if	event	==	"-SUMBIT-":
        window.close()
        return(values[0], values[1], values[2])
        
        
        

def add_release_window():

    layout =    [
                    [sg.Text('Please Enter the following information', font=("Courier",18))],[sg.VPush()],
                    [sg.Text('Artist Nickname',size=(15,1),font=("Courier",18)), sg.InputText(font=("Courier",18))], [sg.VPush()],
                    [sg.Text('Release Name',size=(15,1),font=("Courier",18)), sg.InputText(font=("Courier",18))], [sg.VPush()],
                    [sg.Text('Release Genre',size=(15,1),font=("Courier",18)), sg.InputText(font=("Courier",18))], [sg.VPush()],
                    [sg.Text('Please Choose the Release Type', font=("Courier",18))],[sg.VPush()],
                    [sg.CB("Album", key="Album")],
                    [sg.CB("Video", key="Video")],
                    [sg.CB("Single", key="Single")],
                    [sg.Text('Please Choose the Format', font=("Courier",18))],[sg.VPush()],
                    [sg.CB("Vinyl", key="Vinyl")],
                    [sg.CB("CD", key="CD")],
                    [sg.CB("Digital", key="Digital")],
                    [sg.Submit(key="-SUMBIT-",font=("Courier",18))],[sg.VPush()],
                    [sg.Cancel(button_color="red")]
                ]
    window = sg.Window("Add Release Window", layout, modal=True)
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
        add_contributor_window(values[1])
        popup_window()

def duration_window():

    layout =    [
                    [sg.Text("Please Enter the following information", font=("Courier",18))],[sg.VPush()],
                    [sg.Text("Duration(sec)",size=(15,1),font=("Courier",18)), sg.InputText(font=("Courier",18))], [sg.VPush()],
                    [sg.Submit(key="-SUMBIT-",font=("Courier",18))],[sg.VPush()],
                    [sg.Cancel(button_color="red")]
                ]
    window = sg.Window("Duration Window", layout, modal=True)
    event,values = window.read()
    
    if event == "Cancel":
        window.close()	
    if	event	==	"-SUMBIT-":
        window.close()
        return values[0]
    
    

def price_window():

    layout =    [
                    [sg.Text("Please Enter the following information", font=("Courier",18))],[sg.VPush()],
                    [sg.Text("Format Price",size=(15,1),font=("Courier",18)), sg.InputText(font=("Courier",18))], [sg.VPush()],
                    [sg.Submit(key="-SUMBIT-",font=("Courier",18))],[sg.VPush()],
                    [sg.Cancel(button_color="red")]
                ]
    window = sg.Window("Price Window", layout, modal=True)
    event,values = window.read()
    
    if event == "Cancel":
        window.close()	
    if	event	==	"-SUMBIT-":
        window.close()
        return values[0]

def videoclip_window():

    layout =    [
                    [sg.Text("Please Enter the song's name for the videoclip", font=("Courier",18))],[sg.VPush()],
                    [sg.Text("song name",size=(15,1),font=("Courier",18)), sg.InputText(font=("Courier",18))], [sg.VPush()],
                    [sg.Submit(key="-SUMBIT-",font=("Courier",18))],[sg.VPush()],
                    [sg.Cancel(button_color="red")]
                ]
    window = sg.Window("Videoclip Window", layout, modal=True)
    event,values = window.read()
    
    if event == "Cancel":
        window.close()	
    if	event	==	"-SUMBIT-":
        window.close()
        return values[0]
    

def single_window():

    layout =    [
                    [sg.Text('Please Enter the following information', font=("Courier",18))],[sg.VPush()],
                    [sg.Text('Duration(sec)',size=(15,1),font=("Courier",18)), sg.InputText(font=("Courier",18))], [sg.VPush()],
                    [sg.Text('Studio Id',size=(15,1),font=("Courier",18)), sg.InputText(font=("Courier",18))], [sg.VPush()],
                    [sg.Text('Language',size=(15,1),font=("Courier",18)), sg.InputText(font=("Courier",18))], [sg.VPush()],
                    [sg.Submit(key="-SUMBIT-",font=("Courier",18))],[sg.VPush()],
                    [sg.Cancel(button_color="red")]
                ]
    window = sg.Window("Add Single Window", layout, modal=True)
    event,values = window.read()

    if event == "Cancel":
        window.close()
    if event ==	"-SUMBIT-":
        window.close()
        return values[0], values[1], values[2]

    
def song_window(album_name):

    layout =    [
                    [sg.Text('Please Enter the following information to add a song to the album', font=("Courier",18))],[sg.VPush()],
                    [sg.Text('Name',size=(15,1),font=("Courier",18)), sg.InputText(font=("Courier",18))], [sg.VPush()],
                    [sg.Text('Duration(sec)',size=(15,1),font=("Courier",18)), sg.InputText(font=("Courier",18))], [sg.VPush()],
                    [sg.Text('Studio Id',size=(15,1),font=("Courier",18)), sg.InputText(font=("Courier",18))], [sg.VPush()],
                    [sg.Text('Language',size=(15,1),font=("Courier",18)), sg.InputText(font=("Courier",18))], [sg.VPush()],
                    [sg.Submit(key="-SUMBIT-",font=("Courier",18))],[sg.VPush()],
                    [sg.Cancel(button_color="red")]
                ]
    window = sg.Window("Add Single Window", layout, modal=True)
    event,values = window.read()

    if event == "Cancel":
        window.close()
    if event ==	"-SUMBIT-":
        adm.add_song(None, album_name, values[1], values[2], values[3], values[0])
        window.close()
        popup_window()
        song_window(album_name)
        

def year_window():

    layout =    [
                    [sg.Text("Please Enter the following information", font=("Courier",18))],[sg.VPush()],
                    [sg.Text("Year",size=(15,1),font=("Courier",18)), sg.InputText(font=("Courier",18))], [sg.VPush()],
                    [sg.Submit(key="-SUMBIT-",font=("Courier",18))],[sg.VPush()],
                    [sg.Cancel(button_color="red")]
                ]
    window = sg.Window("Year Window", layout, modal=True)
    event,values = window.read()

    if event == "Cancel":
        window.close()	
    if	event	==	"-SUMBIT-":
        window.close()
        return values[0]

def delete_release_window():

    layout =    [
                    [sg.Text("Please Enter the following information", font=("Courier",18))],[sg.VPush()],
                    [sg.Text("Release Id",size=(15,1),font=("Courier",18)), sg.InputText(font=("Courier",18))], [sg.VPush()],
                    [sg.Submit(key="-SUMBIT-",font=("Courier",18))],[sg.VPush()],
                    [sg.Cancel(button_color="red")]
                ]
    window = sg.Window("Delete Window", layout, modal=True)
    event,values = window.read()

    if event == "Cancel":
        window.close()	
    if	event	==	"-SUMBIT-":
        return values[0]

def delete_artist_window():

    layout =    [
                    [sg.Text("Please Enter the following information", font=("Courier",18))],[sg.VPush()],
                    [sg.Text("Artist nickname",size=(15,1),font=("Courier",18)), sg.InputText(font=("Courier",18))], [sg.VPush()],
                    [sg.Submit(key="-SUMBIT-",font=("Courier",18))],[sg.VPush()],
                    [sg.Cancel(button_color="red")]
                ]
    window = sg.Window("Delete Window", layout, modal=True)
    event,values = window.read()

    if event == "Cancel":
        window.close()	
    if	event	==	"-SUMBIT-":
        return values[0]

def print_window(headings, results):
    
    headings = headings
    data = results

    layout = [[sg.Table(data, headings=headings,auto_size_columns=False,col_widths=[20,20], justification='left', key='-TABLE-')],]
    window = sg.Window("Title", layout, size=(500, 500), finalize=True)

    while True:
        event, values = window.read()
        if event == sg.WINDOW_CLOSED:
            break
        print(event, values)

    window.close()

def popup_window():

    sg.popup("Your action has been completed")

def first_window():

    layout =    [
                    [sg.Button("Login", size=(20,4))],
                    [sg.Button("Register",  size=(20,4))],
                ]
    window	=	sg.Window("First Window", layout, size=(500,500))
    event, values=window.read()	
    print(event)
    window.close()
    if event == 'Login':
        login_window()
        
    elif event == 'Register':
        register_window()

def login_window():

    layout =    [
                    [sg.Text("Please Enter the following information to login", font=("Courier",18))],[sg.VPush()],
                    [sg.Text("Username",size=(15,1),font=("Courier",18)), sg.InputText(font=("Courier",18))], [sg.VPush()],
                    [sg.Text("Password",size=(15,1),font=("Courier",18)), sg.InputText(password_char="*", font=("Courier",18))], [sg.VPush()],
                    [sg.Submit(key="-SUMBIT-",font=("Courier",18))],[sg.VPush()],
                    [sg.Cancel(button_color="red")]
                ]
    window = sg.Window("Login Window", layout, modal=True)
    event,values = window.read()

    result = adm.login_check(values[0], values[1])
    print(result)
    if result == 0:
        pass
    elif result == 1:
        window.close()
        user_window()

    elif result == 2:
        window.close()
        admin_window()

def register_window():

    layout =    [
                    [sg.Text("Please Enter the following information to login", font=("Courier",18))],[sg.VPush()],
                    [sg.Text("Username",size=(15,1),font=("Courier",18)), sg.InputText(font=("Courier",18))], [sg.VPush()],
                    [sg.Text("Password",size=(15,1),font=("Courier",18)), sg.InputText(password_char="*", font=("Courier",18))], [sg.VPush()],
                    [sg.Submit(key="-SUMBIT-",font=("Courier",18))],[sg.VPush()],
                    [sg.Cancel(button_color="red")]
                ]
    window = sg.Window("Register Window", layout, modal=True)
    event,values = window.read()
    check=adm.register_check(values[0], values[1])
    if check == 0:
        pass
    else:
        login_window()

def main():

    db = sqlite3.connect('record_db.db')
    cursor = db.cursor()
    first_window()
  

if __name__ == '__main__':
    main()



