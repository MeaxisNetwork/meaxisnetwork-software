from tkinter import *
from tkinter.ttk import Style

from win32api import GetMonitorInfo, MonitorFromPoint

import constants
import tkinter.font as font
import math
import platform

app = Tk()

MontserratRegular = font.Font(family='Montserrat')

width = app.winfo_screenwidth()
height = app.winfo_screenheight()

window_height = str(math.floor(height / 2))
window_width = str(math.floor(width / 5))

app.title("Login to your MeaxisNetwork Account")
app.resizable(False, False)
app.configure(background=constants.Colors.Level0)
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

app.grid_columnconfigure(0, weight=1)

# Window contents
literal_void = Label(app, text="", font=MontserratRegular, foreground="white", background=constants.Colors.Level0)
literal_void.grid(row = 0, column = 0, sticky = "we", pady = 2, columnspan=5)

welcome_title = Label(app, text="Welcome!", font=MontserratRegular, foreground="white", background=constants.Colors.Level0)
welcome_title.grid(row = 2, column = 0, sticky = "we", pady = 22, columnspan=5)

login_entry = Entry(app, borderwidth=0, font=MontserratRegular)
password_entry = Entry(app, borderwidth=0, font=MontserratRegular)

login_entry.grid(row = 3, column = 0, pady = 2)
password_entry.grid(row = 4, column = 0, pady = 2)

app.geometry(geometry_string)
app.mainloop()