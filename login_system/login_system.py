from turtle import bgcolor, color
import PySimpleGUI as sg
import os


class LoginSystem:

    def __init__(self):
        
        sg.theme('Black')
        layout = [

            #[sg.Text('')],

            [sg.Text('Login', size=(10, 1))],
            [sg.Input(key='login', size=(30, 1))],

            [sg.Text('Senha', size=(10, 1))],
            [sg.Input(key='password', size=(30, 1))],

            [sg.HorizontalSeparator('DarkBlack')],
            [sg.HorizontalSeparator('DarkBlack')],
            #[sg.Text('')],

            [sg.Button('Login', button_color="light gray", size=(5, 1)), sg.Text('', key='scriptMessage')],
            
            [sg.HorizontalSeparator('DarkBlack')]
            
            #[sg.Text('')]
            
        ]

        self.window = sg.Window('Login System', layout)

    def start(self):

        while True:
            
            event, values = self.window.read()
            if event == sg.WINDOW_CLOSED:
                break
            elif event == 'Login':

                acc_login = 'Arkes'
                acc_password = '1232'

                login = values['login']
                password = values['password']

                if acc_login == login and acc_password == password:
                    self.window['scriptMessage'].update('Login Sucessfully')
                else:
                    self.window['scriptMessage'].update('Wrong credentials')

            else:
                pass


main = LoginSystem()
main.start()
