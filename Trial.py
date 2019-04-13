import tkinter
from tkinter import *
from tkinter import filedialog
from tkinter.scrolledtext import ScrolledText
from PIL import ImageTk
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont


# Initialize the main window
root = Tk()
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
print(screen_width, screen_height)
window_width = int(0.9 * screen_width)
window_height = int(0.8 * screen_height)
root.geometry('%sx%s' % (window_width, window_height))

black = (0, 0, 0)
white = (255, 255, 255, 100)

canvas1_height = int(window_width/3)
canvas1_width = int(canvas1_height*3)
canvas1 = Image.new("RGBX", (canvas1_width, canvas1_height), black)

canvas2_height = int(window_width/2)
canvas2_width = int(canvas2_height*3)
canvas2 = Image.new("RGBX", (canvas2_width, canvas2_height), black)

draw1 = ImageDraw.Draw(canvas1)
rect_width = canvas1_width - int(0.2 * canvas1_height)
rect_height = canvas1_height - int(0.2 * canvas1_height)
x1 = 0 + int(0.1 * canvas1_height)
y1 = 0 + int(0.1 * canvas1_height)
x2 = x1 + rect_width
y2 = y1 + rect_height
draw1.rectangle([x1, y1, x2, y2], fill=white)
filename1 = "D:/HobbyProjects/trial1.jpg"
canvas1.save(filename1)

draw2 = ImageDraw.Draw(canvas2)
rect_width = canvas2_width - int(0.2 * canvas2_height)
rect_height = canvas2_height - int(0.2 * canvas2_height)
x1 = 0 + int(0.1 * canvas2_height)
y1 = 0 + int(0.1 * canvas2_height)
x2 = x1 + rect_width
y2 = y1 + rect_height
draw2.rectangle([x1, y1, x2, y2], fill=white)
filename2 = "D:/HobbyProjects/trial2.jpg"
canvas2.save(filename2)

root.mainloop()
