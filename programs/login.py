from tkinter import *
from win32api import GetMonitorInfo, MonitorFromPoint

import math
import platform

app = Tk()

width = app.winfo_screenwidth()
height = app.winfo_screenheight()

window_height = str(math.floor(height/2))
window_width = str(math.floor(width/5))

app.title("Login to your MeaxisNetwork Account")
app.resizable(False, False)
# app.overrideredirect(1)

if platform.system() == "Windows":
	monitor_info = GetMonitorInfo(MonitorFromPoint((0, 0)))
	monitor_area = monitor_info.get("Monitor")
	work_area = monitor_info.get("Work")
	taskbar_height = format(monitor_area[3]-work_area[3])

	geometry_string = window_width + "x" + window_height + "+" + str(width - int(window_width)) + "+" + str(
		height - (int(window_height) + int(taskbar_height)+32))

	print(geometry_string)
else:
	geometry_string = window_width + "x" + window_height + "+" + str(width - int(window_width)) + "+" + str(
		height - int(window_height))

app.geometry(geometry_string)

app.mainloop()