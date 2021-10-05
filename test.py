import PySimpleGUI as sg
import random

sg.theme('LightGreen')
# Add a touch of color
# All the stuff inside your window.
# layoutTable = []
rows, cols = (5, 5)
arr = [[4]*cols]*rows
print(arr)
text = "hello"


data = arr
headings = [str(data[0][x]) for x in range(len(data[0]))]

layout1 = [  [sg.Text(text, font='Arial')],
            [sg.Text('Enter something on Row 2', font='Helvetica'), sg.InputText()],
            [sg.Button('Ok', font='Helvetica'), sg.Button('Cancel', font='Helvetica')],
            [sg.Button('Beep', size=(4,1))],
           [sg.Table(values=data[1:][:], headings=headings, max_col_width=100, background_color='lightblue',
                    display_row_numbers=True,
                    justification='right',
                    num_rows=rows,
                    alternating_row_color='lightyellow',
                    tooltip='This is a table')]
             ]
layout2 = [[sg.Text('Testing 1 2 3', font='Helvetica')]]
layout3 = [[sg.Text('Beep Bop Boop')]]
layout4 = [[sg.Table(values=data, headings=headings, max_col_width=20, background_color='lightblue',
                    display_row_numbers=False,
                    justification='right',
                    auto_size_columns=True,
                    num_rows=10,
                    hide_vertical_scroll= True,
                    expand_y=True,
                    alternating_row_color='lightyellow',
                    size=(100,100),
                    tooltip='This is a table')]]

tabgrp = [[sg.TabGroup([[sg.Tab('Tab1', layout1, font='Helvetica'),
                         sg.Tab('Tab2', layout2, font='Helvetica'),
                         sg.Tab('Tab3', layout3, font='Helvetica'),
                         sg.Tab('Tab4', layout4, font='Helvetica')]], tab_location='topleft', border_width=5), sg.Button('Close')]]


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