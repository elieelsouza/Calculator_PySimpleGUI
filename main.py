import PySimpleGUI as sg

sg.theme('BlueMono')


#Menu layout
menu_layout = [
    ['Opções', ['Sair']],
    ['Ajuda', ['Sobre']]
]
layout = [[sg.Menu(menu_layout)],
    [sg.Input('0', size=(15, 1), font=('Consolas', 20), key='visor'),
     sg.Button('<-', font=('Consolas', 20), key='-BACKSPACE-'),
     sg.Button('C', font=('Consolas',20), key='CLEAR')],

    # Linha 2
    [sg.Button('7', font=('Consolas', 20), key='seven'),
     sg.Button('8', font=('Consolas', 20), key='eight'),
     sg.Button('9', font=('Consolas', 20), key='nine'),
     sg.Button('+', font=('Consolas', 20), key='plus'),
     sg.Button('*', font=('Consolas', 20), key='times')],

     # Linha 3
    [sg.Button('4', font=('Consolas', 20), key='four'),
     sg.Button('5', font=('Consolas', 20), key='five'),
     sg.Button('6', font=('Consolas', 20), key='six'),
     sg.Button('-', font=('Consolas', 20), key='minus'),
     sg.Button('/', font=('Consolas', 20), key='divided')],
     # Linha 4
    [sg.Button('1', font=('Consolas', 20), key='one'),
     sg.Button('2', font=('Consolas', 20), key='two'),
     sg.Button('3', font=('Consolas', 20), key='three'),
     sg.Button('0', font=('Consolas', 20), key='zero'),
     sg.Button('=', font=('Consolas', 20), key='result')]
]

# classe de app

class App:
    def __init__(self):
        self.window = sg.Window('Eliel Calculator', layout=layout, margins=(0, 0), resizable=True, return_keyboard_events=False)
        self.result = 0
        self.oper = ''
        self.window.read(timeout=1)
        for i in range(1, 5):
            for button in layout[i]:
                button.expand(expand_x=True, expand_y=True)

    #funções do menu
    def sobre(self):
        sg.popup('Sobre', 'just an example', 'Github: elieelsouza')


    def resultado(self):
        if self.oper == '+':
            return float(self.result) + float(self.values['visor'])
        if self.oper == '-':
            return float(self.result) - float(self.values['visor'])
        if self.oper == '*':
            return float(self.result) * float(self.values['visor'])
        if self.oper == '/':
            return float(self.result) / float(self.values['visor'])

    def start(self):
        while True:
            event, self.values = self.window.read()

            if event in (None, 'Sair', sg.WIN_CLOSED):
                break


            # clicando em about no menu, ativa essa função
            if event in ('Sobre'):
                self.sobre()


            # atualizando valores no visor
            if event in ('one'):
                if self.values['visor'] == '0':
                    self.window['visor'].update(value='1')
                else:
                    self.window['visor'].update(value=self.values['visor'] + '1')

            if event in ('two'):
                if self.values['visor'] == '0':
                    self.window['visor'].update(value='2')
                else:
                    self.window['visor'].update(value=self.values['visor'] + '2')

            if event in ('three'):
                if self.values['visor'] == '0':
                    self.window['visor'].update(value='3')
                else:
                    self.window['visor'].update(value=self.values['visor'] + '3')

            if event in ('four'):
                if self.values['visor'] == '0':
                    self.window['visor'].update(value='4')
                else:
                    self.window['visor'].update(value=self.values['visor'] + '4')

            if event in ('five'):
                if self.values['visor'] == '0':
                    self.window['visor'].update(value='5')
                else:
                    self.window['visor'].update(value=self.values['visor'] + '5')

            if event in ('six'):
                if self.values['visor'] == '0':
                    self.window['visor'].update(value='6')
                else:
                    self.window['visor'].update(value=self.values['visor'] + '6')

            if event in ('seven'):
                if self.values['visor'] == '0':
                    self.window['visor'].update(value='7')
                else:
                    self.window['visor'].update(value=self.values['visor'] + '7')

            if event in ('eight'):
                if self.values['visor'] == '0':
                    self.window['visor'].update(value='8')
                else:
                    self.window['visor'].update(value=self.values['visor'] + '8')

            if event in ('nine'):
                if self.values['visor'] == '0':
                    self.window['visor'].update(value='9')
                else:
                    self.window['visor'].update(value=self.values['visor'] + '9')

            if event in ('zero'):
                if self.values['visor'] == '0':
                    self.window['visor'].update(value='0')
                else:
                    self.window['visor'].update(value=self.values['visor'] + '0')


            #vamos definir as funções especiais, apagar ultimo e clear all
            if event in ('CLEAR'):
                self.result = 0
                self.window['visor'].update(value=self.result)
            if event in ('-BACKSPACE-'):
                self.window['visor'].update(value=self.values['visor'][:-1])


            # vamos definir as funções de + - * /
            if event in ('plus'):
                if self.oper != '':
                    self.result = self.resultado()
                else:
                    self.oper = '+'
                    self.result = self.values['visor']
                self.window['visor'].update(value='')

            if event in ('minus'):
                if self.oper != '':
                    self.result = self.resultado()
                else:
                    self.oper = '-'
                    self.result = self.values['visor']
                self.window['visor'].update(value='')

            if event in ('divided'):
                if self.oper != '':
                    self.result = self.values['visor']
                else:
                    self.oper = '/'
                    self.result = self.values['visor']
                self.window['visor'].update(value='')

            if event in ('times'):
                if self.oper != '':
                    self.result = self.values['visor']
                else:
                    self.oper = '*'
                    self.result = self.values['visor']
                self.window['visor'].update(value='')

            if event in ('result'):
                self.result = self.resultado()
                self.window['visor'].update(value=self.result)
                self.result = 0
                self.oper = ''
App().start()

