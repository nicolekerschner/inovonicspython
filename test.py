import PySimpleGUI as sg
import random

sg.theme('DefaultNoMoreNagging')

# creating filler table
# rows, cols = (5, 5)
# arr = [[4] * cols] * rows
# data = arr
# headings = ['hello', 'hello','hello', 'hello', 'hello']

headerFont = ('Helvetica', 10, 'bold')
normalFont = ('Helvetica', 11)
UID = [[sg.Text('UID', font=headerFont)],
       [sg.Text('Orginator', font=normalFont), sg.InputText(size=10)],
       [sg.Text('First Hop', font=normalFont), sg.InputText(size=10)],
       [sg.Text('Trace Count', font=normalFont), sg.InputText(size=10)],
       [sg.Text('Trace UID', font=normalFont), sg.InputText(size=10)],
       [sg.Text('Trace UID', font=normalFont), sg.InputText(size=10)],
       [sg.Text('Trace UID', font=normalFont), sg.InputText(size=10)],
       [sg.Text('Trace UID', font=normalFont), sg.InputText(size=10)],
       [sg.Text('Trace UID', font=normalFont), sg.InputText(size=10)]]

originInfo = [[sg.Text('Orignator Info', font=headerFont)],
              [sg.Text('Survery Bit Set', font=normalFont)],
              [sg.Text('Payload ID Present', font=normalFont)],
              [sg.Text('PTI Byte Present', font=normalFont)],
              [sg.Text('Device Class', font=normalFont), sg.InputText(size=10)],
              [sg.Text('Device Type', font=normalFont), sg.InputText(size=10)],
              [sg.Text('Payload ID', font=normalFont), sg.InputText(size=10)],
              [sg.Text('Low Battery', font=normalFont)],
              [sg.Text('Supervision', font=normalFont)],
              [sg.Text('Reset', font=normalFont)],
              [sg.Text('Case Tamper', font=normalFont)]]
receiveStatus = [[sg.Text('Serial Receiver Status', font=headerFont)],
                 [sg.InputText(size=5), sg.Text('Messages', font=normalFont)],
                 [sg.Text('Receiver Jammed', font=normalFont)],
                 [sg.Text('Case Tamper', font=normalFont)],
                 [sg.Text('Supervisory', font=normalFont)],
                 [sg.Text('Processor Reset', font=normalFont)],
                 [sg.Text('Link Failure', font=normalFont)],
                 [sg.Button("Get RF Parameters")],
                 [sg.Button('Get RX Settings')]]

receiveConfig = [[sg.Text('Serial Receiver Configure', font=headerFont)],
                 [sg.Button('Inbound Complete')],
                 [sg.Button('Inbound Verbatim')],
                 [sg.Button('Security Extended')]]

messages = [[sg.Text('Messages/Sec', font=headerFont)],
            [sg.InputText(size=3)]]

layout1 = [[sg.Column(UID)],
           [sg.Column(originInfo)],
           [sg.Column(receiveStatus)],
           [sg.Column(receiveConfig)],
           [sg.Column(messages)]]

enviroHeadings = ('Device', 'MID', ' H ', ' M ', ' L ', ' CH1 ', ' CH2 ', ' TX ', 'Meas',
                  'Delta', 'Int', 'Ext', 'Level', 'Margin', 'Status', 'Timestamp')
rows1, cols1 = (20, 16)
arr1 = [[""] * cols1] * rows1

layout2 = [
    [sg.Table(values=arr1, headings=enviroHeadings, vertical_scroll_only=True, alternating_row_color='lightBlue')],
    [sg.Button('Register')],
    [sg.Button('Monitor', button_color='red')]]

securityHeadings = ('Device', 'MID', 'IDH', 'IDM', 'IDL', 'Lvl', 'Mgn', ' Status ', 'Timestamp',
                    'PHR', 'RNDS', 'Alarm Rnds', 'Al MS', 'Super Count', 'Sp Ms', 'Sup. Sts')
rows2, cols2 = (20, 16)
arr2 = [[""] * cols2] * rows2

layout3 = [[sg.Table(values=arr2, headings=securityHeadings, vertical_scroll_only=True,
                     alternating_row_color='lightBlue')],
           [sg.Button('Register')],
           [sg.Button('Monitor', button_color='red')]]

submeteringHeadings = ('Device', 'MID', 'SNH', 'SNM', 'Total Count', 'Leak Det', 'Level', 'Margin'
                                                                                          'Status', 'Timestamp')
rows3, cols3 = (20, 11)
arr3 = [[""] * cols3] * rows3

layout4 = [[sg.Table(values=arr3, headings=submeteringHeadings, vertical_scroll_only=True,
                     alternating_row_color='lightBlue')],
           [sg.Button('Register')],
           [sg.Button('Monitor', button_color='red')]]

testTransmitter = [[sg.Text('Test Transmitter', font=headerFont)],
                   [sg.Text('MID', font=normalFont), sg.InputText(size=5)],
                   [sg.Text('IDH', font=normalFont), sg.InputText(size=5)],
                   [sg.Text('IDM', font=normalFont), sg.InputText(size=5)],
                   [sg.Text('IDL', font=normalFont), sg.InputText(size=5)],
                   [sg.Text('Level', font=normalFont), sg.InputText(size=5)],
                   [sg.Text('Margin', font=normalFont), sg.InputText(size=5)],
                   [sg.Text('Status', font=normalFont), sg.InputText(size=7)],
                   [sg.Text('Timestamp', font=normalFont), sg.InputText(size=10)]]

repeater = [[sg.Text('Repeater', font=headerFont)],
            [sg.Text('MID', font=normalFont), sg.InputText(size=5)],
            [sg.Text('IDH', font=normalFont), sg.InputText(size=5)],
            [sg.Text('IDM', font=normalFont), sg.InputText(size=5)],
            [sg.Text('IDL', font=normalFont), sg.InputText(size=5)],
            [sg.Text('Level', font=normalFont), sg.InputText(size=5)],
            [sg.Text('Margin', font=normalFont), sg.InputText(size=5)],
            [sg.Text('Status', font=normalFont), sg.InputText(size=7)],
            [sg.Text('Timestamp', font=normalFont), sg.InputText(size=10)]]

messageNum = [[sg.Text('Message Number', font=headerFont), sg.InputText(size=5)],
              [sg.Text('Total Missed Messages', font=normalFont), sg.InputText(size=5)],
              [sg.Text('Message Hit Rate %', font=normalFont), sg.InputText(size=5)],
              [sg.Text('Rounds', font=normalFont), sg.InputText(size=5)]]

messageCount = [[sg.Text('Message Counting', headerFont)],
                [sg.Button('Off', button_color='red')]]

layout5 = [[sg.Column(testTransmitter)],
           [sg.Column(repeater)],
           [sg.Column(messageNum)],
           [sg.Column(messageCount)]]

top_menu_def = [['File', ['Close']],
                ['Ports', ['Com No.', 'Settings']],
                ['ID', ['Read', 'Save', 'Clear']],
                ['Log File', ['Open', 'Close']]]

tabs = [[sg.Tab('Device Data', layout1, font='Helvetica')],
        [sg.Tab('Environmental', layout2, font='Helvetica')],
        [sg.Tab('Security', layout3, font='Helvetica')],
        [sg.Tab('Submetering', layout4, font='Helvetica')],
        [sg.Tab('CENELEC', layout5, font='Helvetica', border_width=5)]]

windowLayout = [[sg.Menu(top_menu_def)],
                [sg.TabGroup(tabs, tab_location='lefttop', font=normalFont)]]

# Create the Window
window = sg.Window('Window Title', windowLayout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:  # if user closes window or clicks cancel
        break
window.close()
