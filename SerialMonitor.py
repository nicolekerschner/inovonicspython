import threading
import PySimpleGUI as sg
from datetime import datetime
from EchoStream_device import EchoStream_device


#hello
def User_Display():
    current_device = EchoStream_device()
    current_device.Device_Name = "Echostream1"
    print(current_device.Device_Name)


    sg.theme('DefaultNoMoreNagging')

    headerFont = ('Helvetica', 10, 'bold')
    normalFont = ('Helvetica', 10)

    # SCREEN 1: DEVICE DATA
    repeaterInfo = [[sg.Text('Hop Count', font=normalFont), sg.StatusBar('', size=3, background_color='white')]]

    display = [[sg.Radio('All', "Display1", default=True)],
               [sg.Radio('Environmental', "Display1")],
               [sg.Radio('Security', "Display1")],
               [sg.Radio('Submetering', "Display1")],
               [sg.Radio('Repeater', "Display1")]]
    spinValues = ['1', '2', '3']
    UID = [[sg.Text('Orginator', font=normalFont), sg.StatusBar('', size=10, background_color='white')],
           [sg.Text('First Hop', font=normalFont), sg.StatusBar('', size=10, background_color='white')],
           [sg.Text('Trace Count', font=normalFont), sg.StatusBar('', size=10, background_color='white')],
           [sg.Text('Trace UID', font=normalFont), sg.StatusBar('', size=10, background_color='white')],
           [sg.Text('Trace UID', font=normalFont), sg.StatusBar('', size=10, background_color='white')],
           [sg.Text('Trace UID', font=normalFont), sg.StatusBar('', size=10, background_color='white')],
           [sg.Text('Trace UID', font=normalFont), sg.StatusBar('', size=10, background_color='white')],
           [sg.Text('Trace UID', font=normalFont), sg.StatusBar('', size=10, background_color='white')]]

    UID1 = [[sg.Frame(title="UID", layout=UID)],
            [sg.Frame(title="Repeater Info", layout=repeaterInfo)],
            [sg.Frame(title="Display:", layout=display)]]

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

    comColor1 = "red"
    comText1 = "COM OFF"
    comOn1 = False

    receiveConfig = [[sg.Button('Inbound Complete'), sg.Image(key="-INBOUND1-", filename="grey.gif", size=(20, 20))],
                     [sg.Button('Inbound Verbatim'), sg.Image(key="-INBOUND2-", filename="grey.gif", size=(20, 20))],
                     [sg.Button('Security Extended'), sg.Image(key="-INBOUND3-", filename="grey.gif", size=(20, 20))],
                     [sg.Button('Message Screening ON')],
                     [sg.Checkbox('Disable Enhanced Message Screening')],
                     [sg.Button('CFG MID')],
                     [sg.Text("MID:"), sg.StatusBar('', background_color='white')],
                     [sg.Text("MID:"), sg.StatusBar('', size=5, expand_x=False, background_color='white')],
                     [sg.Text("MID:"), sg.StatusBar('', size=5, expand_x=False, background_color='white')],
                     [sg.Text("MID:"), sg.StatusBar('', size=5, expand_x=False, background_color='white')],
                     [sg.Text("MID:"), sg.StatusBar('', size=5, expand_x=False, background_color='white')],
                     [sg.Text("Input CIG"), sg.Input(""), sg.Button("Input CIG"), sg.Button(button_text=comText1,
                                                                                            button_color=comColor1,
                                                                                            key="-COMBUTTON1-",
                                                                                            size=(7, 1),
                                                                                            auto_size_button=False)]]
    receiveConfig1 = [[sg.Frame(title="Serial Receiver Configure", layout=receiveConfig)]]

    messageNum = 0
    messages = [[sg.StatusBar('', size=3, background_color='white')],
                [sg.Slider(range=(100, 0), default_value=messageNum, disabled=True, key='-MESSAGESLIDE-')]]
    messages1 = [[sg.Frame(title='Messages/Sec', layout=messages)]]

    rows1, cols1 = (10, 2)
    arr1 = [[""] * cols1] * rows1
    messageHeadings = ['      Timestamp     ',
                       'Message                                                                   '
                       '               ']

    rows0, cols0 = (2, 24)
    arr0 = [[""] * cols0] * rows0
    messageHeadings1 = [' 1 ', ' 2 ', ' 3 ', ' 4 ', ' 5 ', ' 6 ', ' 7 ', ' 8 ', ' 9 ', ' 10 ', ' 11 ', ' 12 ', ' 13 ',
                        ' 14 ', ' 15 ', ' 16 ', ' 17 ', ' 18 ', ' 19 ', ' 20 ', ' 21 ', ' 22 ', ' 23 ', ' 24 ']

    layout1 = [[sg.Column(UID1, vertical_alignment='top'),
                sg.Column(originInfo1, vertical_alignment='top'),
                sg.Column(receiveStatus1, vertical_alignment='top'),
                sg.Column(receiveConfig1, vertical_alignment='top'),
                sg.Column(messages1, vertical_alignment='top')],
               [sg.Text("Messages"), sg.Button("GRAPHS")],
               [sg.Table(values=arr1, headings=messageHeadings, vertical_scroll_only=True, num_rows=7,
                         alternating_row_color='lightBlue', key='-TABLE1-')],
               [sg.Table(values=arr0, headings=messageHeadings1, key="-TABLE0-", num_rows=2, expand_x=True)],
               [sg.Graph(canvas_size=(1000, 75), graph_bottom_left=(0, 0), graph_top_right=(1000, 75),
                         background_color="darkgrey", key='-GRAPH0-')]]

    graphs = True

    # SCREEN 2: LOGGING
    rows2, cols2 = (255, 2)
    arr2 = [[""] * cols2] * rows2
    loggingHeadings = ['      Timestamp     ',
                       '         Message                                                         ']

    monitorColor2 = "red"
    monitorText2 = "Monitor OFF"
    monitorOn2 = False

    comColor2 = "red"
    comText2 = "COM OFF"
    comOn2 = False

    hopCount2 = [[sg.Radio('0', "Hop2", default=True)],
                 [sg.Radio('1', "Hop2")],
                 [sg.Radio('All', "Hop2")]]

    layout2 = [
        [sg.Table(values=arr2, headings=loggingHeadings, vertical_scroll_only=True, alternating_row_color='lightBlue',
                  num_rows=15,
                  key='-Table2-')],
        [sg.Button(monitorText2, button_color=monitorColor2, key='-MONITOR2-'),
         sg.Button(comText2, button_color=comColor2, key="-COMBUTTON2-"), sg.Checkbox("Log Raw Data")],
        [sg.Frame(title="Hop Count", layout=hopCount2, vertical_alignment="center")]]

    # SCREEN 3: ENVIRONMENTAL
    enviroHeadings = ['Device', ' MID ', ' SNH ', ' SNM ', ' SNL ', ' ID1 ', ' ID2 ', ' ID3 ', 'Analog Data',
                      'Options', 'Level', 'Margin', 'Status', '      Timestamp      ']
    rows3, cols3 = (255, 14)
    arr3 = [[""] * cols3] * rows3

    monitorColor3 = "red"
    monitorText3 = "Monitor OFF"
    monitorOn3 = False

    comColor3 = "red"
    comText3 = "COM OFF"
    comOn3 = False

    hopCount3 = [[sg.Radio('0', "Hop3", default=True)],
                 [sg.Radio('1', "Hop3")],
                 [sg.Radio('All', "Hop3")]]

    IDScreen = [[sg.Radio('TXID', "ID", default=True)],
                [sg.Radio('Payload ID', "ID")]]

    layout3 = [
        [sg.Table(values=arr3, headings=enviroHeadings, vertical_scroll_only=True, alternating_row_color='lightBlue',
                  num_rows=15,
                  key='-TABLE3-', expand_x=True)],
        [sg.Graph(canvas_size=(1000, 75), graph_bottom_left=(0, 0), graph_top_right=(1000, 75),
                  background_color="darkgrey")],
        [sg.Button('Register Device', key='-REGISTER3-', enable_events=True), sg.Button('Clear', key='-CLEAR3-')],
        [sg.Frame(title="Hop Count", layout=hopCount3),
         sg.Frame(title="ID Screening", layout=IDScreen, vertical_alignment='top')],
        [sg.Button(monitorText3, button_color=monitorColor3, key='-MONITOR3-'),
         sg.Button(comText3, button_color=comColor3, key='-COMBUTTON3-'), sg.Checkbox("Log Raw Data")],
        [sg.Checkbox("Analog Sensor")]]

    # SCREEN 4: SECURITY
    securityHeadings = ['Device', '  MID  ', '  SNH  ', '  SNM  ', '  SNL  ', ' Status ', 'Level', '  Margin  ',
                        '      Timestamp      ']
    rows4, cols4 = (255, 9)
    arr4 = [[""] * cols4] * rows4

    monitorColor4 = "red"
    monitorText4 = "Monitor OFF"
    monitorOn4 = False

    comColor4 = "red"
    comText4 = "COM OFF"
    comOn4 = False

    hopCount4 = [[sg.Radio('0', "Hop4", default=True)],
                 [sg.Radio('1', "Hop4")],
                 [sg.Radio('All', "Hop4")]]

    hitRate = [[sg.Radio("Off", "hitRate", default=True)],
               [sg.Radio("Heartbeat", "hitRate")],
               [sg.Radio("Other", "hitRate")],
               [sg.Radio("Alarm", "hitRate")]]

    diagnostics = [[sg.Text("Skipped Characters")],
                   [sg.StatusBar("", size=10)],
                   [sg.Text("Level Timer Interval(s)")]]

    layout4 = [[sg.Table(values=arr4, headings=securityHeadings, vertical_scroll_only=True, key='-TABLE4-', num_rows=15,
                         alternating_row_color='lightBlue', expand_x=True)],
               [sg.Graph(canvas_size=(1000, 75), graph_bottom_left=(0, 0), graph_top_right=(1000, 75),
                         background_color="darkgrey")],
               [sg.Button('Register Device', enable_events=True, key='-REGISTER4-'),
                sg.Button('Clear', key='-CLEAR4-')],
               [sg.Button(monitorText4, button_color=monitorColor4, key="-MONITOR4-"), sg.Button(comText4,
                                                                                                 button_color=comColor4,
                                                                                                 key='-COMBUTTON4-'),
                sg.Checkbox("Log Raw Data")],
               [sg.Frame(title="TX Hit Rate", layout=hitRate), sg.Frame(title="Diagnostics", layout=diagnostics,
                                                                        vertical_alignment="top"), sg.Frame(
                   title="Hop Count", layout=hopCount4, vertical_alignment='top')]]

    # SCREEN 5: SUBMETERING
    submeteringHeadings = ['Device', '  MID  ', '  SNH  ', '  SNM  ', '  SNL  ', 'Total Count', 'Leak Detect', 'Level',
                           'Margin', '      Timestamp       ']
    rows5, cols5 = (255, 10)
    arr5 = [[""] * cols5] * rows5

    monitorColor5 = "red"
    monitorText5 = "Monitor OFF"
    monitorOn5 = False

    comColor5 = "red"
    comText5 = "COM OFF"
    comOn5 = False

    hopCount5 = [[sg.Radio('0', "Hop5", default=True)],
                 [sg.Radio('1', "Hop5")],
                 [sg.Radio('All', "Hop5")]]

    layout5 = [
        [sg.Table(values=arr5, headings=submeteringHeadings, vertical_scroll_only=True, key='-TABLE5-', num_rows=15,
                  alternating_row_color='lightBlue', expand_x=True)],
        [sg.Graph(canvas_size=(1000, 75), graph_bottom_left=(0, 0), graph_top_right=(1000, 75),
                  background_color="darkgrey")],
        [sg.Button('Register Device', enable_events=True, key='-REGISTER5-'), sg.Button('Clear', key='-CLEAR5-')],
        [sg.Button(monitorText5, button_color=monitorColor5, key="-MONITOR5-"), sg.Button(comText5,
                                                                                          button_color=comColor5,
                                                                                          key="-COMBUTTON5-"),
         sg.Checkbox("Log Raw Data")],
        [sg.Frame(title="Hop Count", layout=hopCount5, vertical_alignment='top')]]

    top_menu_def = [['File', ['Exit', 'About']],
                    ['Ports', ['Com No.', 'Settings']],
                    ['ID', ['Read', 'Save', 'Clear']],
                    ['Log File', ['Create New::NewLogFile', 'Open Text', 'Close Text', 'Open Excel', 'Close Excel']]]

    tabs = [[sg.Tab('Device Data', layout1, font='Helvetica')],
            [sg.Tab('Logging', layout2, font='Helvetica')],
            [sg.Tab('Environmental', layout3, font='Helvetica')],
            [sg.Tab('Security', layout4, font='Helvetica')],
            [sg.Tab('Submetering', layout5, font='Helvetica')]]

    bits = ['110', '300', '1200', '4800', '9600', '19200', '38400', '57600', '115200', '230400', '460800', '921600']
    current_device.BAUD = 9600
    dataBits = ['5', '6', '7', '8']
    current_device.Data_Bits = 8
    parity = ['Even', 'Odd', 'None', 'Mark', 'Space']
    current_device.Parity = 'None'
    stopBits = ['1', '1.5', '2']
    current_device.Stop_Bits = 1
    flowControl = ['Xon/Xoff', 'Hardware', 'None']
    current_device.Flow_Control= 'None'

    windowLayout = [[sg.Menu(top_menu_def)],
                    [sg.TabGroup(tabs)]]

    # COM Window from Menu Event
    comMenu = ['Com PLACEHOLDER']

    def create_layout_com():
        comLayout = [[sg.Combo(comMenu, enable_events=True, readonly=True)],
                     [sg.Button("OK", key='-OK1-')]]
        return comLayout

    def open_com():
        com_window = sg.Window("COM Port", create_layout_com(), modal=True)
        while True:
            event, values = com_window.read()
            if event == sg.WIN_CLOSED or event == '-OK1-':
                break
        com_window.close()

    # ABOUT Window from Menu Event
    def create_layout_about():
        aboutLayout = [[sg.Text('PLACEHOLDER TEXT (reference section 9.4.2 of requirements)')],
                       [sg.Button("OK", key='-OK2-')]]
        return aboutLayout

    def open_about():
        about_window = sg.Window("COM Port", create_layout_about(), modal=True)
        while True:
            event, values = about_window.read()
            if event == sg.WIN_CLOSED or event == '-OK2-':
                break
        about_window.close()

    # SETTINGS Window from Menu Element
    def create_layout_settings():
        settings = [[sg.Text("Bits per seconds:"), sg.Combo(bits, key='-BITS-', default_value=current_device.BAUD, enable_events=True, readonly=True)],
                    [sg.Text("Data Bits:"), sg.Combo(dataBits, default_value=current_device.Data_Bits, key='-DATABITS-', enable_events=True, readonly=True)],
                    [sg.Text("Parity:"), sg.Combo(parity, default_value=current_device.Parity, key='-PARITY-', enable_events=True, readonly=True)],
                    [sg.Text('Stop Bits'), sg.Combo(stopBits, default_value=current_device.Stop_Bits, key='-STOPBITS-', enable_events=True, readonly=True)],
                    [sg.Text('Flow Control'), sg.Combo(flowControl, default_value=current_device.Flow_Control, key='-FLOWCONTROL-', enable_events=True, readonly=True)]]

        settingsLayout = [[sg.Frame(title="Port Settings", layout=settings)],
                          [sg.Button('Restore Defaults'), sg.Button("OK", key="-OK3-")]]
        return settingsLayout


    def open_settings():
        settings_window = sg.Window("Port Settings", create_layout_settings(), modal=True)

        while True:
            event, values = settings_window.read()
            if event == sg.WIN_CLOSED or event == "-OK3-":
                break
            if event == 'Restore Defaults':
                settings_window['-BITS-'].update(value='9600')
                current_device.BAUD = 9600
                settings_window['-DATABITS-'].update(value='8')
                current_device.Data_Bits = 8
                settings_window['-PARITY-'].update(value='None')
                current_device.Parity = "None"
                settings_window['-STOPBITS-'].update(value='1')
                current_device.Stop_Bits = 1
                settings_window['-FLOWCONTROL-'].update(value='None')
                current_device.Flow_Control = "None"

            if event == '-BITS-':
                current_device.BAUD = values["-BITS-"]
            if event == '-DATABITS-':
                current_device.Data_Bits = values["-DATABITS-"]
            if event == '-PARITY-':
                current_device.Parity = values["-PARITY-"]
            if event == '-STOPBITS-':
                current_device.Stop_Bits = values["-STOPBITS-"]
            if event == '-FLOWCONTROL-':
                current_device.Flow_Control = values["-FLOWCONTROL-"]

        settings_window.close()

    # REGISTER Window
    register_menu = ["Device1", "Device2"]
    device = ""

    def create_layout_register():
        register_1 = [[sg.Frame(title="Search For Devices:",
                                layout=[[sg.Button("Scan", key='-SCAN-'), sg.Button("Stop Scanning", visible=False)],
                                        [sg.Text("Device List:"),
                                         sg.Combo(register_menu, key="-OPTIONMENU-", enable_events=True, readonly=True),
                                         sg.Button("Register", key='-MENUREGISTER-')]])]]
        register_2 = [
            [sg.Frame(title="Input Device:", layout=[[sg.Text("Device ID:"), sg.Input(key="-REGISTER_INPUT-", size=10),
                                                      sg.Button("Register", key="-REGISTER-")]])]]
        registerLayout = [[sg.Text("Register Device")],
                          [sg.Column(register_1), sg.Column(register_2, vertical_alignment="top")],
                          [sg.Text("Device Selected:"),
                           sg.StatusBar(text=device, background_color='white', auto_size_text=True,
                                        key='-DEVICE_STATUS-')],
                          [sg.Button("OK")]]
        return registerLayout

    def open_register():

        register_window = sg.Window("Register Device", create_layout_register(), modal=True)
        while True:
            event, values = register_window.read()
            if event == sg.WIN_CLOSED:
                break
            if event == "OK":
                if device == '':
                    sg.popup("NO DEVICE REGISTERED")
                else:
                    break
            if event == '-REGISTER-':
                device = (values['-REGISTER_INPUT-'])
                register_window['-DEVICE_STATUS-'].update(value=device)
            if event == "-SCAN-":
                register_window['-SCAN-'].update(text="Scanning...")
                register_window['-SCAN-'].update(disabled=True)
                register_window['Stop Scanning'].update(visible=True)
            if event == "Stop Scanning":
                register_window['-SCAN-'].update(text='Scan')
                register_window['-SCAN-'].update(disabled=False)
                register_window['Stop Scanning'].update(visible=False)
            if event == '-MENUREGISTER-':
                device = (values['-OPTIONMENU-'])
                register_window['-DEVICE_STATUS-'].update(value=device)

        register_window.close()

    # Create the Window
    window = sg.Window('Window Title', windowLayout, size=(1050, 825), default_element_size=(10, 1), resizable=True)
    window.Finalize()


    # Event Loop to process "events" and get the "values" of the inputs
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Exit':  # if user closes window
            break

        if event == 'GRAPHS':
            if graphs == False:
                for i in range(0, 960, 40):
                    window['-GRAPH0-'].draw_rectangle(top_left=(i + 10, 70), bottom_right=(i + 40, 0), fill_color='red',
                                                      line_color='red', line_width=2)
                graphs = True
            else:
                window['-GRAPH0-'].erase()
                graphs = False

        # Menu Events
        if event == 'Settings':
            open_settings()

        if event == 'Com No.':
            open_com()

        if event == 'About':
            open_about()

        # Register Device - Environmental
        if event == '-REGISTER3-':
            open_register()
            text3 = device
            arr3.insert(0, [text3, '', '', '', '', '', '', '', '', '', '', '', '',
                            datetime.now().strftime(",%m/%d/%Y %H:%M:%S.%f")])
            window['-TABLE3-'].update(values=arr3)
        if event == '-CLEAR3-':
            arr3 = [[""] * cols3] * rows3
            window['-TABLE3-'].update(values=arr3)

        # Register Device - Security
        if event == '-REGISTER4-':
            open_register()
            text4 = device
            arr4.insert(0, [text4, '', '', '', '', '', '', '', '', '', '', '', '',
                            datetime.now().strftime(",%m/%d/%Y %H:%M:%S.%f")])
            window['-TABLE4-'].update(values=arr4)
        if event == '-CLEAR4-':
            arr4 = [[""] * cols4] * rows4
            window['-TABLE4-'].update(values=arr4)

        # Register Device - Submetering
        if event == '-REGISTER5-':
            open_register()
            text5 = device
            arr5.insert(0, [text5, '', '', '', '', '', '', '', '', '', '', '', '',
                            datetime.now().strftime(",%m/%d/%Y %H:%M:%S.%f")])
            window['-TABLE5-'].update(values=arr5)
        if event == '-CLEAR5-':
            arr5 = [[""] * cols5] * rows5
            window['-TABLE5-'].update(values=arr5)

        # Uses GIFS to monitor status of Inbound Complete, Inbound Verbatim, & Security Extended
        if event == 'Inbound Complete':
            if not inbound1 and not inbound2 and not inbound3:
                window['-INBOUND1-'].update(filename='green.gif', size=(20, 20))
                inbound1 = True
            elif not inbound1:
                window['-INBOUND2-'].update(filename='grey.gif', size=(20, 20))
                inbound2 = False
                window['-INBOUND3-'].update(filename='grey.gif', size=(20, 20))
                inbound3 = False
                window['-INBOUND1-'].update(filename='green.gif', size=(20, 20))
                inbound1 = True
            elif inbound1:
                window['-INBOUND1-'].update(filename='grey.gif', size=(20, 20))
                inbound1 = False

        if event == 'Inbound Verbatim':
            if not inbound1 and not inbound2 and not inbound3:
                window['-INBOUND2-'].update(filename=('green.gif'), size=(20, 20))
                inbound2 = True
            elif not inbound2:
                window['-INBOUND1-'].update(filename='grey.gif', size=(20, 20))
                inbound1 = False
                window['-INBOUND3-'].update(filename='grey.gif', size=(20, 20))
                inbound3 = False
                window['-INBOUND2-'].update(filename='green.gif', size=(20, 20))
                inbound2 = True
            elif inbound2:
                window['-INBOUND2-'].update(filename='grey.gif', size=(20, 20))
                inbound2 = False

        if event == 'Security Extended':
            if not inbound1 and not inbound2 and not inbound3:
                window['-INBOUND3-'].update(filename=('green.gif'), size=(20, 20))
                inbound3 = True
            elif not inbound3:
                window['-INBOUND1-'].update(filename='grey.gif', size=(20, 20))
                inbound1 = False
                window['-INBOUND2-'].update(filename='grey.gif', size=(20, 20))
                inbound2 = False
                window['-INBOUND3-'].update(filename='green.gif', size=(20, 20))
                inbound3 = True
            elif inbound3:
                window['-INBOUND3-'].update(filename='grey.gif', size=(20, 20))
                inbound3 = False

        # Monitor Button - Logging
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

        # Monitor Button - Environmental
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

        # Monitor Button - Security
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

        # Monitor Button - Submetering
        if event == '-MONITOR5-':
            if not monitorOn5:
                monitorColor5 = "green"
                monitorText5 = "Monitor ON"
                window['-MONITOR5-'].update(button_color=monitorColor5)
                window['-MONITOR5-'].update(monitorText5)
                monitorOn5 = True
            else:
                monitorColor5 = "red"
                monitorText5 = "Monitor OFF"
                window['-MONITOR5-'].update(button_color=monitorColor5)
                window['-MONITOR5-'].update(monitorText5)
                monitorOn5 = False

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

        # COM Button - Logging
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

            # COM Button - Environmental
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

            # COM Button - Security
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

            # COM Button - Submetering
        if event == "-COMBUTTON5-":
            if not comOn5:
                comColor5 = "green"
                comText5 = "COM ON"
                window['-COMBUTTON5-'].update(button_color=comColor5)
                window['-COMBUTTON5-'].update(comText5)
                comOn5 = True
            else:
                comColor5 = "red"
                comText5 = "COM OFF"
                window['-COMBUTTON5-'].update(button_color=comColor5)
                window['-COMBUTTON5-'].update(comText5)
                comOn5 = False

    window.close()


##Define Data Collection Function
##Purpose: Constantly collect data from registered devices
def Monitor():
    print("hello")
    ##Code to be extended


##Define Individual Threads
Run_Display = threading.Thread(target=User_Display)
Run_Monitor = threading.Thread(target=Monitor, daemon=True)

##Start Individual Threads
Run_Display.start()
Run_Monitor.start()
