import PySimpleGUI as sg

sg.theme('LightGreen')
# Add a touch of color
# All the stuff inside your window.
# layoutTable = []
rows, cols = (5, 5)
arr = [[0]*cols]*rows

layout1 = [  [sg.Text('Some text on Row 1', font='Arial')],
            [sg.Text('Enter something on Row 2', font='Helvetica'), sg.InputText()],
            [sg.Button('Ok', font='Helvetica'), sg.Button('Cancel', font='Helvetica')],
            [sg.Button('Beep', size=(4,1))],
            [sg.Table
             (values=arr, num_rows = 2, visible = True, select_rows = [1, 2], alternating_row_color ='Red', row_colors ='White')]
             ]
layout2 = [[sg.Text('Testing 1 2 3', font='Helvetica')]]
layout3 = [[sg.Text('Beep Bop Boop')]]
tabgrp = [[sg.TabGroup([[sg.Tab('Tab1', layout1, font='Helvetica'),
                         sg.Tab('Tab2', layout2, font='Helvetica'),
                         sg.Tab('Tab3', layout3, font='Helvetica')]], tab_location='topleft', border_width=5), sg.Button('Close')]]
# Create the Window
window = sg.Window('Window Title', tabgrp)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == 'Beep':
        print('beep')
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break
    if event == 'Ok':
        print('You entered ', values[0])


window.close()