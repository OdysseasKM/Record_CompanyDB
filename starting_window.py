import sys
import PySimpleGUI as sg
import sqlite3
sys.path.insert(0, '../admin')
sys.path.insert(0, '../user')
import admin.admin_menu as admin_gui
import user.user_gui as user_gui

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

    result = login_check(values[0], values[1])
    print(result)
    if result == 0:
        pass
    elif result == 1:
        window.close()
        user_gui.main()

    elif result == 2:
        window.close()
        admin_gui.admin_window()

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
    check= register_check(values[0], values[1])
    if check == 0:
        pass
    else:
        login_window()

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

def main():
    global cursor,db
    db = sqlite3.connect('record-company.db')
    cursor = db.cursor()
    first_window()

if __name__ == '__main__':
    main()

