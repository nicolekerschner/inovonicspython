import PySimpleGUI as sg

sg.theme('DefaultNoMoreNagging')

headerFont = ('Helvetica', 10, 'bold')
normalFont = ('Helvetica', 10)

# SCREEN 1: DEVICE DATA
UID = [[sg.Text('Orginator', font=normalFont), sg.StatusBar('', size=10, background_color='white')],
       [sg.Text('First Hop', font=normalFont), sg.StatusBar('', size=10, background_color='white')],
       [sg.Text('Trace Count', font=normalFont), sg.StatusBar('', size=10, background_color='white')],
       [sg.Text('Trace UID', font=normalFont), sg.StatusBar('', size=10, background_color='white')],
       [sg.Text('Trace UID', font=normalFont), sg.StatusBar('', size=10, background_color='white')],
       [sg.Text('Trace UID', font=normalFont), sg.StatusBar('', size=10, background_color='white')],
       [sg.Text('Trace UID', font=normalFont), sg.StatusBar('', size=10, background_color='white')],
       [sg.Text('Trace UID', font=normalFont), sg.StatusBar('', size=10, background_color='white')]]
UID1 = [[sg.Frame(title="UID", layout=UID)]]

originInfo = [[sg.Text('Survery Bit Set', font=normalFont)],
              [sg.Text('Payload ID Present', font=normalFont)],
              [sg.Text('PTI Byte Present', font=normalFont)],
              [sg.Text('Device Class', font=normalFont), sg.StatusBar('', size=10, background_color='white')],
              [sg.Text('Device Type', font=normalFont), sg.StatusBar('', size=10, background_color='white')],
              [sg.Text('Payload ID', font=normalFont), sg.StatusBar('', size=10, background_color='white')],
              [sg.Text('Low Battery', font=normalFont)],
              [sg.Text('Supervision', font=normalFont)],
              [sg.Text('Reset', font=normalFont)],
              [sg.Text('Case Tamper', font=normalFont)],
              [sg.Text("Level  "),
               sg.ProgressBar(20, orientation='horizontal', size=(10, 10), bar_color=('green', 'grey'))],
              [sg.Text("Margin"),
               sg.ProgressBar(20, orientation='horizontal', size=(10, 10), bar_color=('green', 'grey'))]]
originInfo1 = [[sg.Frame(title="Orginator Info", layout=originInfo)]]

receiveStatus = [[sg.StatusBar('', size=5, background_color='white'), sg.Text('Messages', font=normalFont)],
                 [sg.Text('Receiver Jammed', font=normalFont)],
                 [sg.Text('Case Tamper', font=normalFont)],
                 [sg.Text('Supervisory', font=normalFont)],
                 [sg.Text('Processor Reset', font=normalFont)],
                 [sg.Text('Link Failure', font=normalFont)],
                 [sg.Checkbox('Log Rx Status')],
                 [sg.Button("Get RF Parameters", key='-RFPARA-')],
                 [sg.Button('Get RX Settings')]]
receiveStatus1 = [[sg.Frame(title="Serial Receiver Status", layout=receiveStatus)]]

inbound1 = False
inbound2 = False
inbound3 = False
receiveConfig = [[sg.Button('Inbound Complete'), sg.Image(key="-INBOUND1-", filename="grey.gif", size=(20, 20))],
                 [sg.Button('Inbound Verbatim'), sg.Image(key="-INBOUND2-", filename="grey.gif", size=(20, 20))],
                 [sg.Button('Security Extended'), sg.Image(key="-INBOUND3-", filename="grey.gif", size=(20, 20))]]
receiveConfig1 = [[sg.Frame(title="Serial Receiver Configure", layout=receiveConfig)]]

repeaterInfo = [[sg.Text('Hop Count', font=normalFont), sg.StatusBar('', size=3, background_color='white')]]
repeaterInfo1 = [[sg.Frame(title="Repeater Info", layout=repeaterInfo)]]

display = [[sg.Radio('All', "Display1", default=True)],
           [sg.Radio('Environmental', "Display1")],
           [sg.Radio('Security', "Display1")],
           [sg.Radio('Submetering', "Display1")],
           [sg.Radio('Repeater', "Display1")]]
display1 = [[sg.Frame(title="Display:", layout=display)]]

messages = [[sg.StatusBar('', size=3, background_color='white')]]
messages1 = [[sg.Frame(title='Messages/Sec', layout=messages)]]

layout1 = [[sg.Column(UID1, vertical_alignment='top'),
            sg.Column(originInfo1, vertical_alignment='top'),
            sg.Column(receiveStatus1, vertical_alignment='top'),
            sg.Column(receiveConfig1, vertical_alignment='top'),
            sg.Column(messages1, vertical_alignment='top')],
           [sg.Column(repeaterInfo1, vertical_alignment='top')],
           [sg.Column(display1, vertical_alignment='top')]]

# SCREEN 2: LOGGING
rows, cols = (20, 2)
arr = [[""] * cols] * rows
loggingHeadings = ['         Message           ', '      Timestamp     ']

monitorColor4 = "red"
monitorText4 = "Monitor OFF"
monitorOn4 = False

comColor1 = "red"
comText1 = "COM OFF"
comOn1 = False

hopCount1 = [[sg.Radio('0', "Hop", default=True)],
             [sg.Radio('1', "Hop")],
             [sg.Radio('All', "Hop")]]

layout2 = [[sg.Table(values=arr, headings=loggingHeadings, vertical_scroll_only=True, alternating_row_color='lightBlue',
                     key='-Table4-')],
           [sg.Button(monitorText4, button_color=monitorColor4, key='-MONITOR4-'), sg.Button(comText1, button_color=comColor1, key="-COMBUTTON1-")],
           [sg.Frame(title="Hop Count", layout=hopCount1, vertical_alignment="center")],
           [sg.Checkbox("Log Raw Data")]]

# SCREEN 3: ENVIRONMENTAL
enviroHeadings = ['Device', ' MID ', ' SNH ', ' SNM ', ' SNL ', ' ID1 ', ' ID2 ', ' ID3 ', 'Analog Data',
                  'Options', 'Level', 'Margin', 'Status', 'Timestamp']
rows1, cols1 = (20, 14)
arr1 = [[""] * cols1] * rows1

monitorColor = "red"
monitorText = "Monitor OFF"
monitorOn = False

comColor2 = "red"
comText2 = "COM OFF"
comOn2 = False

hopCount = [[sg.Radio('0', "Hop1", default=True)],
            [sg.Radio('1', "Hop1")],
            [sg.Radio('All', "Hop1")]]

IDScreen = [[sg.Radio('TXID', "ID", default=True)],
            [sg.Radio('Payload ID', "ID")]]

layout3 = [
    [sg.Table(values=arr1, headings=enviroHeadings, vertical_scroll_only=True, alternating_row_color='lightBlue',
              key='-TABLE1-')],
    [sg.Text("Register Device:"), sg.InputText(size=10, key='-INPUT1-', default_text=" "),
     sg.Button('Register', enable_events=True), sg.Button('Clear', key='-CLEAR1-')],
    [sg.Frame(title="Hop Count",layout=hopCount), sg.Frame(title="ID Screening", layout=IDScreen, vertical_alignment='top')],
    [sg.Button(monitorText, button_color=monitorColor, key='-MONITOR-'), sg.Button(comText2, button_color=comColor2, key='-COMBUTTON2-')],
    [sg.Checkbox("Analog Sensor"), sg.Checkbox("Log Raw Data")]]

# SCREEN 4: SECURITY
securityHeadings = ['Device', '  MID  ', '  SNH  ', '  SNM  ', '  SNL  ', ' Status ', 'Level', '  Margin  ',
                    ' Timestamp ']
rows2, cols2 = (20, 9)
arr2 = [[""] * cols2] * rows2

monitorColor2 = "red"
monitorText2 = "Monitor OFF"
monitorOn2 = False

comColor3 = "red"
comText3 = "COM OFF"
comOn3 = False

hopCount3 = [[sg.Radio('0', "Hop3", default=True)],
            [sg.Radio('1', "Hop3")],
            [sg.Radio('All', "Hop3")]]

hitRate = [[sg.Radio("Off", "hitRate", default=True)],
           [sg.Radio("Heartbeat", "hitRate")],
           [sg.Radio("Other", "hitRate")],
           [sg.Radio("Alarm", "hitRate")]]

diagnostics = [[sg.Text("Skipped Characters")],
               [sg.StatusBar("", size=10)],
               [sg.Text("Level Timer Interval(s)")]]

layout4 = [[sg.Table(values=arr2, headings=securityHeadings, vertical_scroll_only=True, key='-TABLE2-',
                     alternating_row_color='lightBlue', enable_click_events=True, enable_events=True)],
           [sg.Text("Register Device:"), sg.InputText(size=10, key='-INPUT2-', default_text=" "), sg.Button('Register',
                                                                                                    enable_events=True,
                                                                                                    key='-REGISTER2-'),
            sg.Button('Clear', key='-CLEAR2-')],
           [sg.Button(monitorText2, button_color=monitorColor2, key="-MONITOR2-"), sg.Button(comText3,
                            button_color=comColor3, key='-COMBUTTON3-'), sg.Checkbox("Log Raw Data")],
           [sg.Frame(title="TX Hit Rate", layout=hitRate), sg.Frame(title="Diagnostics", layout=diagnostics,
                                                                    vertical_alignment="top"), sg.Frame(
               title="Hop Count", layout=hopCount3, vertical_alignment='top')]]

# SCREEN 5: SUBMETERING
submeteringHeadings = ['Device', '  MID  ', '  SNH  ', '  SNM  ', '  SNL  ', 'Total Count', 'Leak Detect', 'Level',
                       'Margin', 'Timestamp']
rows3, cols3 = (20, 10)
arr3 = [[""] * cols3] * rows3

monitorColor3 = "red"
monitorText3 = "Monitor OFF"
monitorOn3 = False

comColor4 = "red"
comText4 = "COM OFF"
comOn4 = False

hopCount4 = [[sg.Radio('0', "Hop4", default=True)],
            [sg.Radio('1', "Hop4")],
            [sg.Radio('All', "Hop4")]]

layout5 = [[sg.Table(values=arr3, headings=submeteringHeadings, vertical_scroll_only=True, key='-TABLE3-',
                     alternating_row_color='lightBlue')],
           [sg.Text("Register Device:"), sg.InputText(size=10, key='-INPUT3-', default_text=" "),
            sg.Button('Register', enable_events=True, key='-REGISTER3-'), sg.Button('Clear', key='-CLEAR3-')],
           [sg.Button(monitorText3, button_color=monitorColor3, key="-MONITOR3-"), sg.Button(comText4,
            button_color=comColor4, key="-COMBUTTON4-"), sg.Checkbox("Log Raw Data")],
           [sg.Frame(title="Hop Count", layout=hopCount4, vertical_alignment='top')]]


# SCREEN 6: CENELEC
testTransmitter = [[sg.Text('MID', font=normalFont), sg.StatusBar('', size=5, background_color='white')],
                   [sg.Text('IDH', font=normalFont), sg.StatusBar('', size=5, background_color='white')],
                   [sg.Text('IDM', font=normalFont), sg.StatusBar('', size=5, background_color='white')],
                   [sg.Text('IDL', font=normalFont), sg.StatusBar('', size=5, background_color='white')],
                   [sg.Text('Level', font=normalFont), sg.StatusBar('', size=5, background_color='white')],
                   [sg.Text('Margin', font=normalFont), sg.StatusBar('', size=5, background_color='white')],
                   [sg.Text('Status', font=normalFont), sg.StatusBar('', size=7, background_color='white')],
                   [sg.Text('Timestamp', font=normalFont), sg.StatusBar('', size=10, background_color='white')]]
testTransmitter1 = [[sg.Frame(title="Test Transmitter", layout=testTransmitter)]]

repeater = [[sg.Text('MID', font=normalFont), sg.StatusBar('', size=5, background_color='white')],
            [sg.Text('IDH', font=normalFont), sg.StatusBar('', size=5, background_color='white')],
            [sg.Text('IDM', font=normalFont), sg.StatusBar('', size=5, background_color='white')],
            [sg.Text('IDL', font=normalFont), sg.StatusBar('', size=5, background_color='white')],
            [sg.Text('Level', font=normalFont), sg.StatusBar('', size=5, background_color='white')],
            [sg.Text('Margin', font=normalFont), sg.StatusBar('', size=5, background_color='white')],
            [sg.Text('Status', font=normalFont), sg.StatusBar('', size=7, background_color='white')],
            [sg.Text('Timestamp', font=normalFont), sg.StatusBar('', size=10, background_color='white')]]
repeater1 = [[sg.Frame(title="Repeater", layout=repeater)]]

messageNum = [[sg.Text('Message Number', font=normalFont), sg.StatusBar('', size=5, background_color='white')],
              [sg.Text('Total Missed Messages', font=normalFont), sg.StatusBar('', size=5, background_color='white')],
              [sg.Text('Message Hit Rate %', font=normalFont), sg.StatusBar('', size=5, background_color='white')],
              [sg.Text('Rounds', font=normalFont), sg.StatusBar('', size=5, background_color='white')]]
messageNum = [[sg.Frame(title="Messages", layout=messageNum)]]

messageColor = "red"
messageText = "OFF"
messageOn = False

messageCount = [[sg.Text("Message Counting", font=headerFont)],
                [sg.Button(messageText, button_color=messageColor, key="-MESSAGE-")]]

layout6 = [[sg.Column(testTransmitter1, vertical_alignment='top'),
            sg.Column(repeater1, vertical_alignment='top'),
            sg.Column(messageNum, vertical_alignment='top'),
            sg.Column(messageCount, vertical_alignment='top')]]

top_menu_def = [['File', ['Exit', 'About']],
                ['Ports', ['Com No.', 'Settings']],
                ['ID', ['Read', 'Save', 'Clear']],
                ['Log File', ['Create New::NewLogFile', 'Open Text', 'Close Text', 'Open Excel', 'Close Excel']]]

tabs = [[sg.Tab('Device Data', layout1, font='Helvetica')],
        [sg.Tab('Logging', layout2, font='Helvetica')],
        [sg.Tab('Environmental', layout3, font='Helvetica')],
        [sg.Tab('Security', layout4, font='Helvetica')],
        [sg.Tab('Submetering', layout5, font='Helvetica')],
        [sg.Tab('CENELEC', layout6, font='Helvetica', border_width=5)]]

bits = ['110', '300', '1200', '4800', '9600', '19200', '38400', '57600', '115200', '230400', '460800', '921600']
dataBits = ['5', '6', '7', '8']
parity = ['Even', 'Odd', 'None', 'Mark', 'Space']
stopBits = ['1', '1.5', '2']
flowControl = ['Xon/Xoff', 'Hardware', 'None']

windowLayout = [[sg.Menu(top_menu_def)],
                [sg.TabGroup(tabs)]]

# COM Window from Menu Event
comMenu = ['Com PLACEHOLDER']


def create_layout_com():
    comLayout = [[sg.OptionMenu(comMenu)],
                 [sg.Button("Ok", key='-OK1-')]]
    return comLayout


def open_com():
    com_window = sg.Window("COM Port", create_layout_com())
    while True:
        event, values = com_window.read()
        if event == sg.WIN_CLOSED or event == '-OK1-':
            break
    com_window.close()


# ABOUT Window from Menu Event
def create_layout_about():
    aboutLayout = [[sg.Text('PLACEHOLDER TEXT (reference section 9.4.2 of requirements)')],
                   [sg.Button("Ok", key='-OK2-')]]
    return aboutLayout


def open_about():
    about_window = sg.Window("COM Port", create_layout_about())
    while True:
        event, values = about_window.read()
        if event == sg.WIN_CLOSED or event == '-OK2-':
            break
    about_window.close()


# SETTINGS Window from Menu Element
def create_layout_settings():
    settings = [[sg.Text("Bits per seconds:"), sg.OptionMenu(bits, default_value='9600', key='-BITS-')],
                [sg.Text("Data Bits:"), sg.OptionMenu(dataBits, default_value='8', key='-DATABITS-')],
                [sg.Text("Parity:"), sg.OptionMenu(parity, default_value='None', key='-PARITY-')],
                [sg.Text('Stop Bits'), sg.OptionMenu(stopBits, default_value='1', key='-STOPBITS-')],
                [sg.Text('Flow Control'), sg.OptionMenu(flowControl, default_value='None', key='-FLOWCONTROL-')]]

    settingsLayout = [[sg.Frame(title="Port Settings", layout=settings)],
                      [sg.Button('Restore Defaults')]]
    return settingsLayout


def open_settings():
    settings_window = sg.Window("Port Settings", create_layout_settings())
    while True:
        event, values = settings_window.read()
        if event == sg.WIN_CLOSED:
            break
        if event == 'Restore Defaults':
            settings_window['-BITS-'].update(value='9600')
            settings_window['-DATABITS-'].update(value='8')
            settings_window['-PARITY-'].update(value='None')
            settings_window['-STOPBITS-'].update(value='1')
            settings_window['-FLOWCONTROL-'].update(value='None')
    settings_window.close()


# Create the Window
window = sg.Window('Window Title', windowLayout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:  # if user closes window
        break

    # Menu Events
    if event == 'Settings':
        open_settings()

    if event == 'Com No.':
        open_com()

    if event == 'About':
        open_about()

    # Register Device - Environmental
    if event == 'Register':
        text1 = (values['-INPUT1-'])
        arr1.insert(0, text1)
        window['-TABLE1-'].update(values=arr1)
        window['-INPUT1-'].update(value="")
    if event == '-CLEAR1-':
        arr1 = [[""] * cols1] * rows1
        window['-TABLE1-'].update(values=arr1)

    # Register Device - Security
    if event == '-REGISTER2-':
        text2 = (values['-INPUT2-'])
        arr2.insert(0, text2)
        window['-TABLE2-'].update(values=arr2)
        window['-INPUT2-'].update(value="")
    if event == '-CLEAR2-':
        arr2 = [[""] * cols1] * rows1
        window['-TABLE2-'].update(values=arr2)

    # Register Device - Submetering
    if event == '-REGISTER3-':
        text3 = (values['-INPUT3-'])
        arr3.insert(0, text3)
        window['-TABLE3-'].update(values=arr3)
        window['-INPUT3-'].update(value="")
    if event == '-CLEAR3-':
        arr3 = [[""] * cols1] * rows1
        window['-TABLE3-'].update(values=arr3)

    # Uses GIFS to monitor status of Inbound Complete, Inbound Verbatim, & Security Extended
    if event == 'Inbound Complete':
        if not inbound1 and not inbound2 and not inbound3:
            window['-INBOUND1-'].update(filename='green.gif', size=(20, 20))
            inbound1 = True
        else:
            window['-INBOUND1-'].update(filename='grey.gif', size=(20, 20))
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

    # Monitor Button - Environmental
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

    # Monitor Button - Security
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

    # Monitor Button - Submetering
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

    # Monitor Button - Logging
    if event == '-MONITOR4-':
        if not monitorOn4:
            monitorColor4 = "green"
            monitorText4 = "Monitor ON"
            window['-MONITOR4-'].update(button_color=monitorColor4)
            window['-MONITOR4-'].update(monitorText4)
            monitorOn4 = True
        else:
            monitorColor4 = "red"
            monitorText4 = "Monitor OFF"
            window['-MONITOR4-'].update(button_color=monitorColor4)
            window['-MONITOR4-'].update(monitorText4)
            monitorOn4 = False

    # COM Button - Logging
    if event == "-COMBUTTON1-":
        if not comOn1:
            comColor1 = "green"
            comText1 = "COM ON"
            window['-COMBUTTON1-'].update(button_color=comColor1)
            window['-COMBUTTON1-'].update(comText1)
            comOn1 = True
        else:
            comColor1 = "red"
            comText1 = "COM OFF"
            window['-COMBUTTON1-'].update(button_color=comColor1)
            window['-COMBUTTON1-'].update(comText1)
            comOn1 = False

        # COM Button - Environmental
    if event == "-COMBUTTON2-":
        if not comOn2:
            comColor2 = "green"
            comText2 = "COM ON"
            window['-COMBUTTON2-'].update(button_color=comColor2)
            window['-COMBUTTON2-'].update(comText2)
            comOn2 = True
        else:
            comColor2 = "red"
            comText2 = "COM OFF"
            window['-COMBUTTON2-'].update(button_color=comColor2)
            window['-COMBUTTON2-'].update(comText2)
            comOn2 = False

        # COM Button - Security
    if event == "-COMBUTTON3-":
        if not comOn3:
            comColor3 = "green"
            comText3 = "COM ON"
            window['-COMBUTTON3-'].update(button_color=comColor3)
            window['-COMBUTTON3-'].update(comText3)
            comOn3 = True
        else:
            comColor3 = "red"
            comText3 = "COM OFF"
            window['-COMBUTTON3-'].update(button_color=comColor3)
            window['-COMBUTTON3-'].update(comText3)
            comOn3 = False

        # COM Button - Submetering
    if event == "-COMBUTTON4-":
        if not comOn4:
            comColor4 = "green"
            comText4 = "COM ON"
            window['-COMBUTTON4-'].update(button_color=comColor4)
            window['-COMBUTTON4-'].update(comText4)
            comOn4 = True
        else:
            comColor4 = "red"
            comText4 = "COM OFF"
            window['-COMBUTTON4-'].update(button_color=comColor4)
            window['-COMBUTTON4-'].update(comText4)
            comOn4 = False

    #Message Button - CENELEC
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
