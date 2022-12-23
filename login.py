import PySimpleGUI as sg


def starting_window():

    layout = [
        [sg.Text('Username:'), sg.InputText()],
        [sg.Text('Password:'), sg.InputText(password_char='*')],
        [sg.Submit(), sg.Cancel()]
    ]

    window	=	sg.Window("Login", layout)

    while True:
        event, values = window.read()
        if event == sg.Submit:
            # Check the entered username and password and log the user in if they are correct
            pass
        elif event == sg.Cancel:
            # Close the window and exit the loop
            break

    window.close()

def main():
    # db = sqlite3.connect('record-company.db')
    starting_window()

if __name__ == '__main__':
    main()
