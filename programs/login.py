from tkinter import *
from tkinter.ttk import Style

from win32api import GetMonitorInfo, MonitorFromPoint

import math
import platform

app = Tk()

width = app.winfo_screenwidth()
height = app.winfo_screenheight()

window_height = str(math.floor(height / 2))
window_width = str(math.floor(width / 5))

app.title("Login to your MeaxisNetwork Account")
app.resizable(False, False)
app.configure(background="#1c1c20")
app.overrideredirect(True)

if platform.system() == "Windows":
    monitor_info = GetMonitorInfo(MonitorFromPoint((0, 0)))
    monitor_area = monitor_info.get("Monitor")
    work_area = monitor_info.get("Work")

    width = work_area[2]
    height = work_area[3]

    width = math.floor((width - int(window_width)) / 2)
    height = math.floor((height - int(window_height)) / 2)

    geometry_string = window_width + "x" + window_height + "+" + str(width) + "+" + str(
        height)
else:
    geometry_string = window_width + "x" + window_height + "+" + str(width - int(window_width)) + "+" + str(
        height - int(window_height))

# Window contents
welcome_title = Label(app, text="Test")
welcome_title.grid(row = 0, column = 0, sticky = W, pady = 2)
welcome_title.grid(row = 1, column = 0, sticky = W, pady = 2)

app.geometry(geometry_string)
app.mainloop()