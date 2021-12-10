import PySimpleGUI as sg

window = sg.Window('Graph Element - Bar Chart', [[sg.Graph((400, 400), (0,0), (10, 100), k='-GRAPH-')]], finalize=True)

for i, data in enumerate([50, 10, 20,80]):
    window['-GRAPH-'].draw_rectangle((i*2+1, data), (i*2+2, 0), fill_color='purple', line_color='white', line_width=2)
    window['-GRAPH-'].draw_text(f'      {data}', (i*2+1, data+3), color='white', font='_ 18')

window.read(close=True)