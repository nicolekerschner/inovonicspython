import PySimpleGUI as sg


def callback(var, index, mode):
    """
    For OptionMenu
    var - tkinter control variable.
    index - index of var, '' if var is not a list.
    mode - 'w' for 'write' here.
    """
    window.write_event_value("Language", window['Language'].TKStringVar.get())

sg.theme("DarkBlue3")
sg.set_options(font=("Courier New", 16))

data = ["Arabic", "Chinese", "English", "German", "Japanese", "Latin", "Spanish"]

layout = [
    [sg.OptionMenu(data, default_value=data[2], key='Language')],
    [sg.Button("Click")],
]

window = sg.Window('Title', layout, finalize=True)
window['Language'].TKStringVar.trace("w", callback)

while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED:
        break
    elif event == 'Language':
        print(event, values['Language'])
    elif event == 'Click':
        print(event, values['Language'])

window.close()