import PySimpleGUI as sg
import webbrowser

sg.theme('DarkAmber')

layout = [[sg.Text('Max memory :'), sg.InputText()],
          [sg.Text('Min  memory :'), sg.InputText()],
          [sg.Text('Select jar file :'), sg.InputText(), sg.FileBrowse()],
          [sg.Text('Server folder  :'), sg.InputText(key='-fd-'), sg.FolderBrowse()],
          [sg.Checkbox('Accept Eula', default=False, key='-ae-'), sg.Checkbox('Open readme', default=True, key='-wb-')],
          [sg.Submit(), sg.Button('Close')]]

window = sg.Window('Setup', layout, icon=r'images\Luxury_Logo (2).ico')

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Close':
        break

window.close()

b = open(f"{values['-fd-']}/start.bat", 'w')
b.write(f"java -Xmx{values[0]}M -Xms{values[1]}M -jar {values[2]} nogui pause")

b.close()

e = open(f"{values['-fd-']}/eula.txt", "w")
e.write(f"eula={values['-ae-']}")

e.close()

if values['-wb-']:
    webbrowser.open("readme.txt")