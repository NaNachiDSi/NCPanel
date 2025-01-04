import tkinter as tk
import subprocess
import os

os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"

buttonStates = {}
runningProcesses = {}
frame = tk.Tk()
frame.title("NCPanel")

channel_var = tk.StringVar(value=os.getenv('CHANNEL', ''))

channel_entry = tk.Entry(frame, textvariable=channel_var, width=30)
channel_entry.pack(side=tk.TOP)

def update_channel():
    os.environ['CHANNEL'] = channel_var.get()
    print(f"Zu {os.environ['CHANNEL']} gewechselt.")

update_button = tk.Button(frame, text="Update Channel", command=update_channel)
update_button.pack(pady=5, side=tk.TOP)

def switchButtonState(button, button_name):
    buttonStates[button_name] = not buttonStates[button_name]

    if buttonStates[button_name]:
        button.config(bg="lime")
        print(f"{button_name} wird gestartet...")
        runningProcesses[button_name] = subprocess.Popen(["python", f"modules/{button_name}.py"])
    else:
        button.config(bg="red")
        print(f"{button_name} wird beendet...")
        runningProcesses[button_name].terminate()

def getFiles():
    for file in os.listdir("modules"):
        if file.endswith(".py"):
            button_name = file[:-3]
            button = tk.Button(frame, text=button_name, width=20, height=1)
            buttonStates[button_name] = False
            button.config(bg="red")
            button.pack(pady=5)
            button.config(command=lambda btn=button, name=button_name: switchButtonState(btn, name))

getFiles()
frame.mainloop()
