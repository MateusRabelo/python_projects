import random
import PySimpleGUI as sg
import os
   
   
# ctrl + kc
class PassGenerator:
    def __init__(self):
        
        sg.theme('BlueMono')
        layout = [
            
                [sg.Text('Site/Software', size=(10, 1)),
                 sg.Input(key='site', size=(20, 1))],
                    
                [sg.Text('Email/Usuário', size=(10, 1)),
                 sg.Input(key='usuario', size=(20,1))],
                
                [sg.Text('Quantidade de caracteres'),
                 sg.Combo(values=list(range(34)), key='totalChars', default_value=1, size=(3, 1))],
                
                [sg.Output(size=(32, 5))],
                
                [sg.Button('Gerar Senha')]
                
                ]
        # declarating window
        self.window = sg.Window('Password Generator', layout)

        
    def Initialize(self):
        
        while True:
            # looping to update the program according to the events that are happening
            event, values = self.window.read()
            if event == sg.WIN_CLOSED:
                break
            if event == 'Gerar Senha':
                newPass = self.generatePass(values)
                print(newPass)
                
            if layout == layout [sg.Combo(values=['33'])]:
                print('Calma meu patrão!')
                
                
    def generatePass(self, values):
        
        charList = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz123456789!@#$%&*'
        chars = random.choices(charList, k=int(values['totalChars']))
        
        newPass2 = ''.join(chars)
        return newPass2
                
    def savePass(self):
        pass
    
gen = PassGenerator()
gen.Initialize()