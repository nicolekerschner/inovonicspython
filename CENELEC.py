# SCREEN 6: CENELEC
#testTransmitter = [[sg.Text('MID', font=normalFont), sg.StatusBar('', size=5, background_color='white')],
#                   [sg.Text('IDH', font=normalFont), sg.StatusBar('', size=5, background_color='white')],
#                   [sg.Text('IDM', font=normalFont), sg.StatusBar('', size=5, background_color='white')],
#                   [sg.Text('IDL', font=normalFont), sg.StatusBar('', size=5, background_color='white')],
#                  [sg.Text('Level', font=normalFont), sg.StatusBar('', size=5, background_color='white')],
#                   [sg.Text('Margin', font=normalFont), sg.StatusBar('', size=5, background_color='white')],
#                   [sg.Text('Status', font=normalFont), sg.StatusBar('', size=7, background_color='white')],
#                   [sg.Text('Timestamp', font=normalFont), sg.StatusBar('', size=10, background_color='white')]]
#testTransmitter1 = [[sg.Frame(title="Test Transmitter", layout=testTransmitter)]]

#repeater = [[sg.Text('MID', font=normalFont), sg.StatusBar('', size=5, background_color='white')],
#            [sg.Text('IDH', font=normalFont), sg.StatusBar('', size=5, background_color='white')],
#            [sg.Text('IDM', font=normalFont), sg.StatusBar('', size=5, background_color='white')],
#            [sg.Text('IDL', font=normalFont), sg.StatusBar('', size=5, background_color='white')],
#            [sg.Text('Level', font=normalFont), sg.StatusBar('', size=5, background_color='white')],
#            [sg.Text('Margin', font=normalFont), sg.StatusBar('', size=5, background_color='white')],
#            [sg.Text('Status', font=normalFont), sg.StatusBar('', size=7, background_color='white')],
#            [sg.Text('Timestamp', font=normalFont), sg.StatusBar('', size=10, background_color='white')]]
#repeater1 = [[sg.Frame(title="Repeater", layout=repeater)]]

#messageNum = [[sg.Text('Message Number', font=normalFont), sg.StatusBar('', size=5, background_color='white')],
#              [sg.Text('Total Missed Messages', font=normalFont), sg.StatusBar('', size=5, background_color='white')],
#              [sg.Text('Message Hit Rate %', font=normalFont), sg.StatusBar('', size=5, background_color='white')],
#              [sg.Text('Rounds', font=normalFont), sg.StatusBar('', size=5, background_color='white')]]
#messageNum = [[sg.Frame(title="Messages", layout=messageNum)]]

#messageColor = "red"
#messageText = "OFF"
#messageOn = False

messageCount = [[sg.Text("Message Counting", font=headerFont)],
                [sg.Button(messageText, button_color=messageColor, key="-MESSAGE-")]]

layout6 = [[sg.Column(testTransmitter1, vertical_alignment='top'),
            sg.Column(repeater1, vertical_alignment='top'),
            sg.Column(messageNum, vertical_alignment='top'),
            sg.Column(messageCount, vertical_alignment='top')]]



# Message Button - CENELEC
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