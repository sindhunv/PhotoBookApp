import textwrap
import tkinter
from tkinter import *
from tkinter import filedialog
from tkinter.scrolledtext import ScrolledText
from PIL import ImageTk
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

root = Tk()

# App window sizes
window_width = int(0.9 * root.winfo_screenwidth())
window_height = int(0.8 * root.winfo_screenheight())
root.geometry('%sx%s' % (window_width, window_height))

top_frame_height = int((5*window_height)/6)
bottom_frame_height = int(window_height/6)

# App window frames
top = Frame(root, bg='light yellow', width=window_width, height=top_frame_height)
bottom = Frame(root, bg='light green', width=window_width, height=bottom_frame_height)

# Margins in percentage
left_margin_percentage = IntVar()
right_margin_percentage = IntVar()
top_margin_percentage = IntVar()
bottom_margin_percentage = IntVar()
center_margin_percentage = IntVar()
left_margin_percentage.set(18)
right_margin_percentage.set(7)
top_margin_percentage.set(8)
bottom_margin_percentage.set(8)
center_margin_percentage.set(2)

# Horizontal photo default size
aspect_ratio = 1.33
photo_display_height = int(0.7*top_frame_height)
photo_display_width =  int(aspect_ratio*photo_display_height)

# Margins in pixels
right_margin = (right_margin_percentage.get() * photo_display_width) / 100
left_margin = (left_margin_percentage.get() * photo_display_width) / 100
top_margin = (top_margin_percentage.get() * photo_display_width) / 100
bottom_margin = (bottom_margin_percentage.get() * photo_display_width) / 100
center_margin = (center_margin_percentage.get() * photo_display_width) / 100

# Vertical photo default size
photo_display_width_2 = int((photo_display_width - center_margin)/2)
photo_display_height_2 = int(photo_display_width_2*aspect_ratio)
print(photo_display_width, photo_display_height, photo_display_width_2, center_margin, photo_display_height_2)

# Photo frame size in pixels
photo_frame_display_height = photo_display_height + top_margin + bottom_margin
photo_frame_display_width = photo_display_width + right_margin + left_margin

# coordinates of photos in the frame
rel_x = ((photo_frame_display_width - right_margin -  photo_display_width) / photo_frame_display_width)
rel_y =  (((photo_frame_display_height - photo_display_height)/2) / photo_frame_display_height)
rel_x1 = (left_margin / photo_frame_display_width)
rel_y1 = (((photo_frame_display_height - photo_display_height_2)/2) / photo_frame_display_height)
rel_x2 = ((photo_frame_display_width - right_margin - photo_display_width_2) / photo_frame_display_width)
rel_y2 = (((photo_frame_display_height - photo_display_height_2)/2) / photo_frame_display_height)

photo_frame_display = Frame(top, bg='black', width=photo_frame_display_width, height=photo_frame_display_height)
photo = Frame(photo_frame_display, bg='light grey', width=photo_display_width, height=photo_display_height)
photo1 = Frame(photo_frame_display, bg='light grey', width=photo_display_width_2, height=photo_display_height_2)
photo2 = Frame(photo_frame_display, bg='light grey', width=photo_display_width_2, height=photo_display_height_2)

# Add buttons in the photos
add_button = Button(photo, text="Add")
add_button1 = Button(photo1, text="Add")
add_button2 = Button(photo2, text="Add")

# Canvas to display photos
canvas = Canvas(photo, bg='black', highlightthickness=0)
canvas1 = Canvas(photo1, bg='black', highlightthickness=0)
canvas2 = Canvas(photo2, bg='black', highlightthickness=0)

# Global variables
page_type = IntVar()
option_selected = IntVar()
image_path = StringVar()

# Radio button options
landscape_photo = Radiobutton(bottom, bg="orange", text="Option1", value=1, variable=page_type)
two_portrait_photos = Radiobutton(bottom, bg="orange", text="Option2", value=2, variable=page_type)
landscape_text = Radiobutton(bottom, bg="orange", text="Option3", value=3, variable=page_type)


def reset_all():
    print("reset all")
    add_button.place_forget()
    add_button1.place_forget()
    add_button2.place_forget()
    photo.place_forget()
    photo1.place_forget()
    photo2.place_forget()
    canvas.pack_forget()
    canvas1.pack_forget()
    canvas2.pack_forget()
    photo_frame_display.pack_forget()
