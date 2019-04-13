import tkinter
from tkinter import *
from tkinter import filedialog
from tkinter.scrolledtext import ScrolledText
from PIL import ImageTk
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
from TrialCanvas import *
from TrialButton import *


# Initialize the main window
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
print(screen_width, screen_height)
window_width = int(0.9 * screen_width)
window_height = int(0.8 * screen_height)
root.geometry('%sx%s' % (window_width, window_height))

canvas1.configure(width=int(window_width/2))
button1.configure(command=button1clicked)
canvas1.pack()
button1.pack()

root.mainloop()