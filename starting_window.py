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
        print(result[0])
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
    if len(result) != 0:
        return 0
    else:
        sql="""INSERT INTO USER
        VALUES(?, ?, 0);"""
        cursor.execute(sql,(username, password))
        db.commit()

def login_window(note):

    layout =    [
                    [sg.Text("Please Enter the following information to login\n")],
                    [sg.Text("Username"),sg.InputText(font=my_font)],
                    [sg.Text("Password "),sg.InputText(password_char="*")], 
                    [sg.Text("\n"+note+"\n")],
                    [sg.Button("SUBMIT",button_color="green"),sg.Button("Exit",button_color="red")],    
                ]
    window = sg.Window("Login Window", layout,font=my_font,size = my_window_size,resizable = True,finalize=True)
    
    while True:
        event,values = window.read()
        if event == "Exit" or event == sg.WINDOW_CLOSED:
            break
        elif event == "SUBMIT":
            result = login_check(values[0], values[1])
            if result == 0:
                window.close()
                login_window("Please try again.")
            elif result == 1:
                window.close()
                user_gui.main()
            elif result == 2:
                window.close()
                admin_gui.admin_window()
    window.close()


def register_window(note):
    layout =    [
                    [sg.Text("Please Enter the following information to Register\n")],
                    [sg.Text("Username"),sg.InputText(font=my_font)],
                    [sg.Text("Password "),sg.InputText(password_char="*")], 
                    [sg.Text("\n"+note+"\n")],
                    [sg.Button("SUBMIT",button_color="green"),sg.Button("Exit",button_color="red")]
                ]
    window = sg.Window("Register Window", layout,font=my_font,size = my_window_size,resizable = True,finalize=True)
    
    while True:
        event,values = window.read()
        if event == "Exit" or event == sg.WINDOW_CLOSED:
            window.close()
            return False
        elif event == "SUBMIT":
            result = register_check(values[0], values[1])
            if result == 0:
                window.close()
                register_window("This username already exists. Please select another username.")
            else: 
                window.close
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

    # Run the event loop to process user input
    while True:
        event, values = window.Read()
        if event == "Close" or event == sg.WINDOW_CLOSED:
            break
        elif event == 'Login':  # If the user clicks the Login button
            # Open the login window
            window.hide()
            login_window("")
            window.un_hide()
        elif event == 'Register':  # If the user clicks the Register button
            # Open the register window
            window.hide()
            if (register_window("")): 
                window.close()
                first_window("Congratulations, your account has been succesfully created. \nYou can login now!")
            else: 
                window.un_hide()

    # Close the window
    window.Close()

def main():
    global cursor,db
    db = sqlite3.connect('record-company.db')
    cursor = db.cursor()
    first_window("")

if __name__ == '__main__':
    main()

