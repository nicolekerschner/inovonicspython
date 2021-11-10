import PySimpleGUI as sg

sg.theme('DefaultNoMoreNagging')

headerFont = ('Helvetica', 10, 'bold')
normalFont = ('Helvetica', 11)

# SCREEN 1: DEVICE DATA
UID = [[sg.Text('UID', font=headerFont)],
       [sg.Text('Orginator', font=normalFont), sg.StatusBar('', size=10, background_color='white')],
       [sg.Text('First Hop', font=normalFont), sg.StatusBar('', size=10, background_color='white')],
       [sg.Text('Trace Count', font=normalFont), sg.StatusBar('', size=10, background_color='white')],
       [sg.Text('Trace UID', font=normalFont), sg.StatusBar('', size=10, background_color='white')],
       [sg.Text('Trace UID', font=normalFont), sg.StatusBar('', size=10, background_color='white')],
       [sg.Text('Trace UID', font=normalFont), sg.StatusBar('', size=10, background_color='white')],
       [sg.Text('Trace UID', font=normalFont), sg.StatusBar('', size=10, background_color='white')],
       [sg.Text('Trace UID', font=normalFont), sg.StatusBar('', size=10, background_color='white')]]

originInfo = [[sg.Text('Orignator Info', font=headerFont)],
              [sg.Text('Survery Bit Set', font=normalFont)],
              [sg.Text('Payload ID Present', font=normalFont)],
              [sg.Text('PTI Byte Present', font=normalFont)],
              [sg.Text('Device Class', font=normalFont), sg.StatusBar('', size=10, background_color='white')],
              [sg.Text('Device Type', font=normalFont), sg.StatusBar('', size=10, background_color='white')],
              [sg.Text('Payload ID', font=normalFont), sg.StatusBar('', size=10, background_color='white')],
              [sg.Text('Low Battery', font=normalFont)],
              [sg.Text('Supervision', font=normalFont)],
              [sg.Text('Reset', font=normalFont)],
              [sg.Text('Case Tamper', font=normalFont)],
              [sg.Text("Level  "), sg.ProgressBar(20, orientation='horizontal', size=(10,10), bar_color=('green', 'grey'))],
              [sg.Text("Margin"), sg.ProgressBar(20, orientation='horizontal', size=(10,10), bar_color=('green', 'grey'))]]


receiveStatus = [[sg.Text('Serial Receiver Status', font=headerFont)],
                 [sg.StatusBar('', size=5, background_color='white'), sg.Text('Messages', font=normalFont)],
                 [sg.Text('Receiver Jammed', font=normalFont)],
                 [sg.Text('Case Tamper', font=normalFont)],
                 [sg.Text('Supervisory', font=normalFont)],
                 [sg.Text('Processor Reset', font=normalFont)],
                 [sg.Text('Link Failure', font=normalFont)],
                 [sg.Checkbox('Log Rx Status')],
                 [sg.Button("Get RF Parameters", key='-RFPARA-')],
                 [sg.Button('Get RX Settings')]]


inbound1 = False
inbound2 = False
inbound3 = False
receiveConfig = [[sg.Text('Serial Receiver Configure', font=headerFont)],
                 [sg.Button('Inbound Complete'), sg.Image(key = "-INBOUND1-", filename="grey.gif", size=(20, 20))],
                 [sg.Button('Inbound Verbatim'), sg.Image(key = "-INBOUND2-", filename="grey.gif", size=(20, 20))],
                 [sg.Button('Security Extended'), sg.Image(key = "-INBOUND3-", filename="grey.gif", size=(20, 20))]]

repeaterInfo = [[sg.Text('Repeater Info', font=headerFont)],
                [sg.Text('Hop Count', font=normalFont), sg.StatusBar('', size=3, background_color='white')]]


display = [[sg.Text("Display:", font=headerFont)],
           [sg.Radio('All', "Display1", default=True)],
           [sg.Radio('Environmental', "Display1")],
           [sg.Radio('Security', "Display1")],
           [sg.Radio('Submetering', "Display1")],
           [sg.Radio('Repeater', "Display1")]]

messages = [[sg.Text('Messages/Sec', font=headerFont)],
            [sg.StatusBar('', size=3, background_color='white')]]

layout1 = [[sg.Column(UID, vertical_alignment='top'),
            sg.VerticalSeparator(),
            sg.Column(originInfo, vertical_alignment='top'),
            sg.VerticalSeparator(),
            sg.Column(receiveStatus, vertical_alignment='top'),
            sg.VerticalSeparator(),
            sg.Column(receiveConfig, vertical_alignment='top'),
            sg.VerticalSeparator(),
            sg.Column(messages, vertical_alignment='top')],
           [sg.Column(repeaterInfo, vertical_alignment= 'top')],
           [sg.Column(display, vertical_alignment='top')]]

# SCREEN 2: ENVIRONMENTAL
enviroHeadings = ['Device', ' MID ', ' H ', ' M ', ' L ', ' CH1 ', ' CH2 ', ' TX ', ' Meas ',
                  'Delta', ' Int ', ' Ext ', 'Level', 'Margin', 'Status', 'Timestamp']
rows1, cols1 = (20, 16)
arr1 = [[""] * cols1] * rows1


monitorColor = "red"
monitorText = "Monitor OFF"
monitorOn = False

layout2 = [
    [sg.Table(values=arr1, headings=enviroHeadings, vertical_scroll_only=True, alternating_row_color='lightBlue',
              key='-TABLE1-')],
    [sg.Text("Register Device:"), sg.InputText(size=10, key='-INPUT1-')],
    [sg.Button('Register', enable_events=True), sg.Button(monitorText, button_color=monitorColor, key='-MONITOR-')],
    [sg.Checkbox("Analog Sensor"), sg.Checkbox("Log Raw Data")]]

# SCREEN 3: SECURITY
securityHeadings = ['Device', '  MID  ', '  IDH  ', '  IDM  ', '  IDL  ', '  Lvl  ', '  Mgn  ', ' Status ', 'Timestamp',
                    '  PHR  ', ' RNDS ', 'Alarm Rnds', 'Al MS', 'Super Count', 'Sp Ms', 'Sup. Sts']
rows2, cols2 = (20, 16)
arr2 = [[""] * cols2] * rows2

monitorColor2 = "red"
monitorText2 = "Monitor OFF"
monitorOn2 = False

layout3 = [[sg.Table(values=arr2, headings=securityHeadings, vertical_scroll_only=True,
                     alternating_row_color='lightBlue', enable_click_events=True, enable_events=True)],
           [sg.Button('Register'), sg.Button(monitorText2, button_color=monitorColor2, key="-MONITOR2-"),
            sg.Checkbox("Log Raw Data")],
           [sg.Text("TX Hit Rate")],
           [sg.Text("Diagnostics")]]

# SCREEN 4: SUBMETERING
submeteringHeadings = ['Device', '  MID  ', '  SNH  ', '  SNM  ', 'Total Count', 'Leak Det', 'Level', 'Margin',
                       'Status', 'Timestamp']
rows3, cols3 = (20, 11)
arr3 = [[""] * cols3] * rows3

monitorColor3 = "red"
monitorText3 = "Monitor OFF"
monitorOn3 = False

layout4 = [[sg.Table(values=arr3, headings=submeteringHeadings, vertical_scroll_only=True,
                     alternating_row_color='lightBlue')],
           [sg.Button('Register')],
           [sg.Button(monitorText3, button_color=monitorColor3, key="-MONITOR3-")]]

# SCREEN 5: CENELEC
testTransmitter = [[sg.Text('Test Transmitter', font=headerFont)],
                   [sg.Text('MID', font=normalFont), sg.StatusBar('', size=5, background_color='white')],
                   [sg.Text('IDH', font=normalFont), sg.StatusBar('', size=5, background_color='white')],
                   [sg.Text('IDM', font=normalFont), sg.StatusBar('', size=5, background_color='white')],
                   [sg.Text('IDL', font=normalFont), sg.StatusBar('', size=5, background_color='white')],
                   [sg.Text('Level', font=normalFont), sg.StatusBar('', size=5, background_color='white')],
                   [sg.Text('Margin', font=normalFont), sg.StatusBar('', size=5, background_color='white')],
                   [sg.Text('Status', font=normalFont), sg.StatusBar('', size=7, background_color='white')],
                   [sg.Text('Timestamp', font=normalFont), sg.StatusBar('', size=10, background_color='white')]]

repeater = [[sg.Text('Repeater', font=headerFont)],
            [sg.Text('MID', font=normalFont), sg.StatusBar('', size=5, background_color='white')],
            [sg.Text('IDH', font=normalFont), sg.StatusBar('', size=5, background_color='white')],
            [sg.Text('IDM', font=normalFont), sg.StatusBar('', size=5, background_color='white')],
            [sg.Text('IDL', font=normalFont), sg.StatusBar('', size=5, background_color='white')],
            [sg.Text('Level', font=normalFont), sg.StatusBar('', size=5, background_color='white')],
            [sg.Text('Margin', font=normalFont), sg.StatusBar('', size=5, background_color='white')],
            [sg.Text('Status', font=normalFont), sg.StatusBar('', size=7, background_color='white')],
            [sg.Text('Timestamp', font=normalFont), sg.StatusBar('', size=10, background_color='white')]]

messageNum = [[sg.Text('Message Number', font=headerFont), sg.StatusBar('', size=5, background_color='white')],
              [sg.Text('Total Missed Messages', font=normalFont), sg.StatusBar('', size=5, background_color='white')],
              [sg.Text('Message Hit Rate %', font=normalFont), sg.StatusBar('', size=5, background_color='white')],
              [sg.Text('Rounds', font=normalFont), sg.StatusBar('', size=5, background_color='white')]]

messageColor = "red"
messageText = "OFF"
messageOn = False

messageCount = [[sg.Text('Message Counting', font=headerFont)],
                [sg.Button(messageText, button_color=messageColor, key="-MESSAGE-")]]

layout5 = [[sg.Column(testTransmitter, vertical_alignment='top'),
            sg.VerticalSeparator(),
            sg.Column(repeater, vertical_alignment='top'),
            sg.VerticalSeparator(),
            sg.Column(messageNum, vertical_alignment='top'),
            sg.VerticalSeparator(),
            sg.Column(messageCount, vertical_alignment='top')]]

top_menu_def = [['File', ['Exit','About']],
                ['Ports', ['Com No.', 'Settings']],
                ['ID', ['Read', 'Save', 'Clear']],
                ['Log File', ['Create New::NewLogFile', 'Open Text', 'Close Text', 'Open Excel', 'Close Excel']]]

tabs = [[sg.Tab('Device Data', layout1, font='Helvetica')],
        [sg.Tab('Environmental', layout2, font='Helvetica')],
        [sg.Tab('Security', layout3, font='Helvetica')],
        [sg.Tab('Submetering', layout4, font='Helvetica')],
        [sg.Tab('CENELEC', layout5, font='Helvetica', border_width=5)]]

windowLayout = [[sg.Menu(top_menu_def)],
                [sg.TabGroup(tabs)]]

##Not Currently Functional
#def create_new_log():



# Create the Window
window = sg.Window('Window Title', windowLayout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()


    if event == sg.WIN_CLOSED:  # if user closes window or clicks cancel
        break

    ##Not Currently Functional
    #if event == 'Create New::NewLogFile':
        #create_new_log()


    if event == 'Register':
        text1 = (values['-INPUT1-'])
        arr1.insert(0, text1)
        window['-TABLE1-'].update(values=arr1)

    if event == 'Inbound Complete':
        if not inbound1 and not inbound2 and not inbound3:
            window['-INBOUND1-'].update(filename=('green.gif'), size=(20,20))
            inbound1 = True
        else:
            window['-INBOUND1-'].update(filename=('grey.gif'), size=(20, 20))
            inbound1 = False

    if event == 'Inbound Verbatim':
        if not inbound1 and not inbound2 and not inbound3:
            window['-INBOUND2-'].update(filename=('green.gif'), size=(20, 20))
            inbound2 = True
        else:
            window['-INBOUND2-'].update(filename=('grey.gif'), size=(20, 20))
            inbound2 = False

    if event == 'Security Extended':
        if not inbound1 and not inbound2 and not inbound3:
            window['-INBOUND3-'].update(filename=('green.gif'), size=(20, 20))
            inbound3 = True
        else:
            window['-INBOUND3-'].update(filename=('grey.gif'), size=(20, 20))
            inbound3 = False

    if event == '-MONITOR-':
        if not monitorOn:
            monitorColor = "green"
            monitorText = "Monitor ON"
            window['-MONITOR-'].update(button_color=monitorColor)
            window['-MONITOR-'].update(monitorText)
            monitorOn = True
        else:
            monitorColor = "red"
            monitorText = "Monitor OFF"
            window['-MONITOR-'].update(button_color=monitorColor)
            window['-MONITOR-'].update(monitorText)
            monitorOn = False

    if event == '-MONITOR2-':
        if not monitorOn2:
            monitorColor2 = "green"
            monitorText2 = "Monitor ON"
            window['-MONITOR2-'].update(button_color=monitorColor2)
            window['-MONITOR2-'].update(monitorText2)
            monitorOn2 = True
        else:
            monitorColor2 = "red"
            monitorText2 = "Monitor OFF"
            window['-MONITOR2-'].update(button_color=monitorColor2)
            window['-MONITOR2-'].update(monitorText2)
            monitorOn2 = False

    if event == '-MONITOR3-':
        if not monitorOn3:
            monitorColor3 = "green"
            monitorText3 = "Monitor ON"
            window['-MONITOR3-'].update(button_color=monitorColor3)
            window['-MONITOR3-'].update(monitorText3)
            monitorOn3 = True
        else:
            monitorColor3 = "red"
            monitorText3 = "Monitor OFF"
            window['-MONITOR3-'].update(button_color=monitorColor3)
            window['-MONITOR3-'].update(monitorText3)
            monitorOn3 = False

    if event == '-MESSAGE-':
        if not messageOn:
            messageColor = "green"
            messageText = "ON"
            window['-MESSAGE-'].update(button_color=messageColor)
            window['-MESSAGE-'].update(messageText)
            messageOn = True
        else:
            messageColor = "red"
            messageText = "OFF"
            window['-MESSAGE-'].update(button_color=messageColor)
            window['-MESSAGE-'].update(messageText)
            messageOn = False

window.close()
