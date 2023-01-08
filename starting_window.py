import sys
import PySimpleGUI as sg
import sqlite3
sys.path.insert(0, '../admin')
sys.path.insert(0, '../user')
import admin.admin_menu as admin_gui
import user.user_gui as user_gui

my_window_size = [800,350] #width, height
my_font = 'Helvetica 22'

def login_check(username, password):
    sql="""SELECT *
        FROM USER
        WHERE username=? AND password=?;"""
    cursor.execute(sql,(username, password))
    result = cursor.fetchall()

    if len(result) == 0:
        return 0 # user doesnt exist
    else: 
        sql="""SELECT is_admin
        FROM USER
        WHERE username=? AND password=?;"""
        cursor.execute(sql,(username, password))
        result = cursor.fetchone()
        if result[0]==0:
            return 1 # user is not admin
        else:
            return 2 # user is admin

def register_check(username, password):
    sql="""SELECT *
        FROM USER
        WHERE username=?;"""
    cursor.execute(sql,(username,))
    result = cursor.fetchall()
    if len(result) != 0:return True
    else:
        sql="""INSERT INTO USER
        VALUES(?, ?, 0);"""
        cursor.execute(sql,(username, password))
        db.commit()
        return False

def login_window(note):

    layout =    [
                    [sg.Text("Please Enter the following information to login\n")],
                    [sg.Text("Username"),sg.InputText(font=my_font)],
                    [sg.Text("Password "),sg.InputText(password_char="*")], 
                    [sg.Text("\n"+note+"\n")],
                    [sg.Button("SUBMIT",button_color="green"),sg.Button("Exit",button_color="red")],    
                ]
    window = sg.Window("Login Window", layout,font=my_font,size = my_window_size,resizable = True,finalize=True)
    event,values = window.read()
    window.close()
    if event == "Exit" or event == sg.WINDOW_CLOSED:
        print("bye!")
    elif event == "SUBMIT":
        result = login_check(values[0], values[1])
        if result == 0:
            login_window("Please try again.")
        elif result == 1:
            user_gui.main()
            first_window("")
        elif result == 2:
            admin_gui.main()
            first_window("")


def register_window(note):
    layout =    [
                    [sg.Text("Please Enter the following information to Register\n")],
                    [sg.Text("Username"),sg.InputText(font=my_font)],
                    [sg.Text("Password "),sg.InputText(password_char="*")], 
                    [sg.Text("\n"+note+"\n")],
                    [sg.Button("SUBMIT",button_color="green"),sg.Button("Exit",button_color="red")]
                ]
    window = sg.Window("Register Window", layout,font=my_font,size = my_window_size,resizable = True,finalize=True)

    event,values = window.read()
    window.close()

    if event == "Exit" or event == sg.WINDOW_CLOSED:
        return False
    elif event == "SUBMIT":
        if (register_check(values[0], values[1])):
            register_window("This username already exists. Please select another username.")
        else: 
            return True

def first_window(note):

    layout = [
        [sg.Text("Welcome to DBRC\n\n", font=('Helvetica', 25), justification='center')],
        [sg.Button("Login", size=(22, 2),button_color=('dark blue')), sg.Button("Register", size=(22, 2), button_color=('dark blue'))],
        [sg.Text(note)],
        [sg.Button("Close",button_color=("red"))]
    ]

    # Create the login/register window
    window = sg.Window('DBRC', layout, font = my_font, size = my_window_size, resizable=True)
    event, values = window.Read()
    window.close()

    if event == "Close" or event == sg.WINDOW_CLOSED:
        window.close()
    elif event == 'Login':  # If the user clicks the Login button
        # Open the login window
        login_window("") 
    elif event == 'Register':  # If the user clicks the Register button
        # Open the register window   
        if (register_window("")): 
            first_window("Congratulations, your account has been succesfully created. \nYou can login now!")
        else:first_window("")
    

def main():
    global cursor,db
    db = sqlite3.connect('record-company.db')
    cursor = db.cursor()
    first_window("")

if __name__ == '__main__':
    main()

