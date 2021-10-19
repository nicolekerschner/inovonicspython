import PySimpleGUI as sg
import random

sg.theme('Default')
# Add a touch of color
# All the stuff inside your window.
# layoutTable = []
rows, cols = (5, 5)
arr = [[4] * cols] * rows
print(arr)

data = arr
headings = ['hello', 'hello','hello', 'hello', 'hello']


UID= [[sg.Text('UID', font='Arial')],
           [sg.Text('Orginator', font='Helvetica'), sg.InputText(size=10)],
           [sg.Text('First Hop', font='Helvetica'), sg.InputText(size=10)],
           [sg.Text('Trace Count', font='Helvetica'), sg.InputText(size=10)],
           [sg.Text('Trace UID', font='Helvetica'), sg.InputText(size=10)],
           [sg.Text('Trace UID', font='Helvetica'), sg.InputText(size=10)],
           [sg.Text('Trace UID', font='Helvetica'), sg.InputText(size=10)],
           [sg.Text('Trace UID', font='Helvetica'), sg.InputText(size=10)],
           [sg.Text('Trace UID', font='Helvetica'), sg.InputText(size=10)],

          # [sg.Button('Ok', font='Helvetica'), sg.Button('Cancel', font='Helvetica')],
          # [sg.Button('Beep', size=(4, 1))],
           ]
originInfo = [[sg.Text('Orignator Info', font='Arial')],
              [sg.Text('Survery Bit Set', font='Helvetica')],
              [sg.Text('Payload ID Present', font='Helvetica')],
              [sg.Text('PTI Byte Present', font='Helvetica')],
              [sg.Text('Device Class', font='Helvetica'), sg.InputText(size=10)],
              [sg.Text('Device Type', font='Helvetica'), sg.InputText(size=10)],
              [sg.Text('Payload ID', font='Helvetica'), sg.InputText(size=10)],
              [sg.Text('Low Battery', font='Helvetica')],
              [sg.Text('Supervision', font='Helvetica')],
              [sg.Text('Reset', font='Helvetica')],
              [sg.Text('Case Tamper', font='Helvetica')],
              ]
receiveStatus = [[sg.Text('Serial Receiver Status')],
                 [sg.InputText(size=5), sg.Text('Messages', font="Helvetica")],
                 [sg.Text('Receiver Jammed', font= 'Helvetica')],
                 [sg.Text('Case Tamper', font= 'Helvetica')],
                 [sg.Text('Supervisory', font= 'Helvetica')],
                 [sg.Text('Processor Reset', font= 'Helvetica')],
                 [sg.Text('Link Failure', font= 'Helvetica')],
                 [sg.Button("Get RF Parameters")],
                 [sg.Button('Get RX Settings')]]

receiveConfig = [[sg.Text('Serial Receiver Configure')],
                 [sg.Button('Inbound Complete')],
                 [sg.Button('Inbound Verbatim')],
                 [sg.Button('Security Extended')]]

layout1 = [[sg.Column(UID),
           sg.Column(originInfo),
           sg.Column(receiveStatus),
           sg.Column(receiveConfig)]]
layout2 = [[sg.Text('Testing 1 2 3', font='Helvetica')]]
layout3 = [[sg.Text('Beep Bop Boop')]]
layout4 = [[sg.Table(values=data,
                     headings=headings,
                     max_col_width=20,
                     background_color='lightblue',
                     display_row_numbers=False,
                     col_widths=10,
                     justification='left',
                     auto_size_columns=True,
                     num_rows=10,
                     hide_vertical_scroll=True,
                     expand_y=True,
                     size=(100, 100),
                     tooltip='This is a table')]]
layout5 = [[sg.Text("Transmitter")]]

tabgrp = [[sg.TabGroup([[sg.Tab('Device Data', layout1, font='Helvetica'),
                         sg.Tab('Environmental', layout2, font='Helvetica'),
                         sg.Tab('Security', layout3, font='Helvetica'),
                         sg.Tab('Submetering', layout4, font='Helvetica'),
                         sg.Tab('CENELEC', layout5, font='Helvetica')]], tab_location='topleft', border_width=5),
                         sg.Button('Close')]]

# Create the Window
window = sg.Window('Window Title', tabgrp)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == 'Beep':
        print('beep')
    if event == sg.WIN_CLOSED or event == 'Cancel':  # if user closes window or clicks cancel
        break
    if event == 'Ok':
        print('You entered ', values[0])

window.close()
