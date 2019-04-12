import textwrap
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
position_right = int(screen_width / 2 - window_width / 2)
position_down = int(screen_height / 2 - window_height / 2)
root.geometry('%sx%s' % (window_width, window_height))
root.geometry("+{}+{}".format(position_right, position_down))

# Set this for fill/expand when you resize the window
root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=1)
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)

# Split the main widow into left right and bottom sections
left_width = int(0.7 * window_width)
left_height = int(0.85 * window_height)
right_width = window_width - left_width
right_height = window_height
bottom_width = left_width
bottom_height = window_height - left_height

# Set width and height for the sections to show up
left = Frame(root, bg='light blue', width=left_width, height=left_height)
right = Frame(root, bg='light yellow', width=right_width, height=right_height)
bottom = Frame(root, bg='light green', width=bottom_width, height=bottom_height)

# Use sticky to specify how to fill inside the grid
left.grid(row=0, column=0, sticky="nsew")
right.grid(row=0, rowspan=2, column=1, sticky="nsew")
bottom.grid(row=1, column=0, sticky="nsew")

# Initialize margins for the photo
left_margin = DoubleVar()
left_margin.set(0.2)
right_margin = DoubleVar()
right_margin.set(0.1)
top_margin = DoubleVar()
top_margin.set(0.1)
bottom_margin = DoubleVar()
bottom_margin.set(0.1)
center_margin = DoubleVar()
center_margin.set(0.03)

# Initialize photo properties
photo_aspect_ratio = DoubleVar()
photo_aspect_ratio.set(1.5)

selected_photo_width = DoubleVar()
selected_photo_height = DoubleVar()
selected_photo_width.set(0.8 * left_width)
selected_photo_height.set(left_height/photo_aspect_ratio.get())

# Initialize margins


# Initialize photo frame dimensions
# Photo frame size will be calculated by adding margins to the selected photo size
# Fix the width of the photo frame
photo_frame_width = DoubleVar()
photo_frame_height = DoubleVar()
photo_frame_width.set(0.8 * left_width)
# Calculate the photo width given the border percentages
# 1.3 * photo_width = photo_frame_width => photo_width = photo_frame_width / 1.3
selected_photo_width.set(photo_frame_width.get() / (1 + left_margin.get() + right_margin.get()))
# Calculate photo height using the photo aspect ratio
# photo_width/photo_height = photo_aspect_ratio
selected_photo_height.set(selected_photo_width.get()/photo_aspect_ratio.get())
# Calculate the photo frame height using the margins
# 1.2 * photo_height = photo_frame_height
photo_frame_height.set((1 + top_margin.get() + bottom_margin.get()) * selected_photo_height.get())

# Coordinates to place the photo
rel_photo_1_x = DoubleVar()
rel_photo_1_y = DoubleVar()
rel_photo_2_x = DoubleVar()
rel_photo_2_y = DoubleVar()


# Frames
photo_frame = Frame(left, bg='black')
photo_landscape = Frame(photo_frame, bg='light grey')
canvas_landscape = Canvas(photo_landscape, bg='black', highlightthickness=0)
add_landscape_photo_button = Button(photo_landscape, text="Add")
photo_portrait_1 = Frame(photo_frame, bg='light grey')
canvas_portrait_1 = Canvas(photo_portrait_1, bg='black', highlightthickness=0)
add_protrait_photo_button_1 = Button(photo_portrait_1, text="Add")
photo_portrait_2 = Frame(photo_frame, bg='light grey')
canvas_portrait_2 = Canvas(photo_portrait_2, bg='black', highlightthickness=0)
add_protrait_photo_button_2 = Button(photo_portrait_2, text="Add")
buttons_frame = Frame(left, bg='light blue')
buttons_frame_width = int(left_width - photo_frame_width.get())
buttons_frame.configure(width=buttons_frame_width, height=left_height)
buttons_frame.pack(expand=True, side=RIGHT)

# Other global variables
landscape_photo_width = DoubleVar()
landscape_photo_height = DoubleVar()
file_name_1 = StringVar()
file_name_2 = StringVar()
selected_option = IntVar()
selected_option.set(0)
destination_folder_name = "C:/Users/sindh/Desktop/IcelandPhotobook"

# Initialize caption text settings
text_width = IntVar()
rel_text_x = DoubleVar()
rel_text_y = DoubleVar()
text = StringVar()
text.set("Photo Caption")
photo_text = StringVar()
photo_text.set("Text")
font_size = 15
text_font = "arial " + font_size.__str__()


text_label = Label(photo_frame, font=text_font, textvariable=text, foreground="white", bg="black", justify=CENTER)
photo_text_text = Text(photo_landscape, font=text_font, foreground="black", bg="white")

def add_photo_button_clicked():
    file = filedialog.askopenfile(parent=photo_landscape, title='Choose source folder')
    if file is None:
        return
    add_landscape_photo_button.place_forget()
    file_name_1.set(file.name)
    photo_frame.pack_forget()
    im = Image.open(file_name_1.get())
    photo_aspect_ratio.set(im.size[0] / im.size[1])
    # Calculate the photo width given the border percentages
    # 1.3 * photo_width = photo_frame_width => photo_width = photo_frame_width / 1.3
    selected_photo_width.set(photo_frame_width.get() / (1 + left_margin.get() + right_margin.get()))
    # Calculate photo height using the photo aspect ratio
    # photo_width/photo_height = photo_aspect_ratio
    selected_photo_height.set(selected_photo_width.get() / photo_aspect_ratio.get())
    # Calculate the photo frame height using the margins
    # 1.2 * photo_height = photo_frame_height
    photo_frame_height.set((1 + top_margin.get() + bottom_margin.get()) * selected_photo_height.get())
    photo_frame.configure(width=photo_frame_width.get(), height=photo_frame_height.get())
    photo_frame.pack(expand=True, side=LEFT)
    rel_photo_1_x.set(left_margin.get() * selected_photo_width.get() / photo_frame_width.get())
    rel_photo_1_y.set(top_margin.get() * selected_photo_height.get() / photo_frame_height.get())
    photo_landscape.configure(width=selected_photo_width.get(), height=selected_photo_height.get())
    photo_landscape.place(relx=rel_photo_1_x.get(), rely=rel_photo_1_y.get())
    rel_text_x.set(((left_margin.get() * selected_photo_width.get()) + (selected_photo_width.get() / 2)) / photo_frame_width.get())
    rel_text_y.set((top_margin.get() * selected_photo_height.get() + selected_photo_height.get() + (bottom_margin.get() * selected_photo_height.get() / 2)) / photo_frame_height.get())
    text_label.place(relx=rel_text_x.get(), rely=rel_text_y.get(), anchor=CENTER, width=text_width.get())
    size = selected_photo_width.get(), selected_photo_height.get()
    im.thumbnail(size)
    canvas_landscape.image = ImageTk.PhotoImage(im)
    canvas_landscape.create_image(0, 0, image=canvas_landscape.image, anchor=NW)
    canvas_landscape.pack()
    left_margin_scale.configure(command=left_margin_change, state=NORMAL, bg="white smoke", relief=FLAT)
    right_margin_scale.configure(command=right_margin_change, state=NORMAL, bg="white smoke", relief=FLAT)
    top_margin_scale.configure(command=top_margin_change, state=NORMAL, bg="white smoke", relief=FLAT)
    bottom_margin_scale.configure(command=bottom_margin_change, state=NORMAL, bg="white smoke", relief=FLAT)


add_landscape_photo_button.configure(command=add_photo_button_clicked)


def add_portrait_photo_button_1_clicked():
    file = filedialog.askopenfile(parent=photo_landscape, title='Choose source folder')
    if file is None:
        return
    add_protrait_photo_button_1.place_forget()
    file_name_1.set(file.name)
    im = Image.open(file_name_1.get())
    photo_aspect_ratio.set(im.size[0] / im.size[1])
    landscape_photo_width.set((photo_frame_width.get() / (1 + left_margin.get() + right_margin.get())))
    selected_photo_width.set((landscape_photo_width.get() - center_margin.get() * landscape_photo_width.get()) / 2)
    selected_photo_height.set(photo_aspect_ratio.get() * selected_photo_width.get())
    photo_frame_height.set(selected_photo_height.get() + (top_margin.get() + bottom_margin.get()) * landscape_photo_height.get())
    photo_portrait_1.configure(width=selected_photo_width.get(), height=selected_photo_height.get())
    photo_frame.configure(width=photo_frame_width.get(), height=photo_frame_height.get())
    photo_frame.pack(expand=True, side=LEFT)
    text_label.configure(width=text_width.get())
    rel_text_x.set(((left_margin.get() * landscape_photo_width.get()) + selected_photo_width.get() + (
                center_margin.get() * landscape_photo_width.get()) / 2) / photo_frame_width.get())
    rel_text_y.set((top_margin.get() * landscape_photo_height.get() + selected_photo_height.get() + (
                bottom_margin.get() * landscape_photo_height.get() / 2)) / photo_frame_height.get())
    text_label.place(relx=rel_text_x.get(), rely=rel_text_y.get(), anchor=CENTER, width=text_width.get())
    size = selected_photo_width.get(), selected_photo_height.get()
    im = im.transpose(Image.ROTATE_270)
    im.thumbnail(size)
    canvas_portrait_1.image = ImageTk.PhotoImage(im)
    canvas_portrait_1.create_image(0, 0, image=canvas_portrait_1.image, anchor=NW)
    canvas_portrait_1.pack()
    left_margin_scale.configure(command=left_margin_change, state=NORMAL, bg="white smoke", relief=FLAT)
    right_margin_scale.configure(command=right_margin_change, state=NORMAL, bg="white smoke", relief=FLAT)
    top_margin_scale.configure(command=top_margin_change, state=NORMAL, bg="white smoke", relief=FLAT)
    bottom_margin_scale.configure(command=bottom_margin_change, state=NORMAL, bg="white smoke", relief=FLAT)
    center_margin_scale.configure(command=center_margin_change, state=NORMAL, bg="white smoke", relief=FLAT)


add_protrait_photo_button_1.configure(command=add_portrait_photo_button_1_clicked)


def add_portrait_photo_button_2_clicked():
    file = filedialog.askopenfile(parent=photo_portrait_2, title='Choose source folder')
    if file is None:
        return
    add_protrait_photo_button_2.place_forget()
    file_name_2.set(file.name)
    im = Image.open(file_name_2.get())
    photo_aspect_ratio.set(im.size[0] / im.size[1])
    landscape_photo_width.set((photo_frame_width.get() / (1 + left_margin.get() + right_margin.get())))
    selected_photo_width.set((landscape_photo_width.get() - center_margin.get() * landscape_photo_width.get()) / 2)
    selected_photo_height.set(photo_aspect_ratio.get() * selected_photo_width.get())
    photo_frame_height.set(selected_photo_height.get() + (top_margin.get() + bottom_margin.get()) * landscape_photo_height.get())
    photo_portrait_2.configure(width=selected_photo_width.get(), height=selected_photo_height.get())
    photo_frame.configure(width=photo_frame_width.get(), height=photo_frame_height.get())
    photo_frame.pack(expand=True, side=LEFT)
    text_label.configure(width=text_width.get())
    rel_text_x.set(((left_margin.get() * landscape_photo_width.get()) + selected_photo_width.get() + (
                center_margin.get() * landscape_photo_width.get()) / 2) / photo_frame_width.get())
    rel_text_y.set((top_margin.get() * landscape_photo_height.get() + selected_photo_height.get() + (
                bottom_margin.get() * landscape_photo_height.get() / 2)) / photo_frame_height.get())
    text_label.place(relx=rel_text_x.get(), rely=rel_text_y.get(), anchor=CENTER, width=text_width.get())
    size = selected_photo_width.get(), selected_photo_height.get()
    im = im.transpose(Image.ROTATE_270)
    im.thumbnail(size)
    canvas_portrait_2.image = ImageTk.PhotoImage(im)
    canvas_portrait_2.create_image(0, 0, image=canvas_portrait_2.image, anchor=NW)
    canvas_portrait_2.pack()
    left_margin_scale.configure(command=left_margin_change, state=NORMAL, bg="white smoke", relief=FLAT)
    right_margin_scale.configure(command=right_margin_change, state=NORMAL, bg="white smoke", relief=FLAT)
    top_margin_scale.configure(command=top_margin_change, state=NORMAL, bg="white smoke", relief=FLAT)
    bottom_margin_scale.configure(command=bottom_margin_change, state=NORMAL, bg="white smoke", relief=FLAT)
    center_margin_scale.configure(command=center_margin_change, state=NORMAL, bg="white smoke", relief=FLAT)


add_protrait_photo_button_2.configure(command=add_portrait_photo_button_2_clicked)

bottom_frames_width = int(bottom_width / 3)
bottom_left_frame = Frame(bottom, bg='orange', width=bottom_frames_width, height=bottom_height)
bottom_middle_frame = Frame(bottom, bg='light green', width=bottom_frames_width, height=bottom_height)
bottom_right_frame = Frame(bottom, bg='pink', width=bottom_frames_width, height=bottom_height)
bottom_left_frame.pack(expand=True, fill=BOTH, side=LEFT)
bottom_middle_frame.pack(expand=True, fill=BOTH, side=LEFT)
bottom_right_frame.pack(expand=True, fill=BOTH, side=RIGHT)

bottom_frames_height = int(bottom_height / 2)
bottom_left_top_frame = Frame(bottom_left_frame, bg='orange', width=bottom_frames_width, height=bottom_frames_height)
bottom_left_bottom_frame = Frame(bottom_left_frame, bg='orange', width=bottom_frames_width, height=bottom_frames_height)
bottom_left_top_frame.pack(expand=True, fill=BOTH, side=LEFT)
bottom_left_bottom_frame.pack(expand=True, fill=BOTH, side=RIGHT)


def forget_all():
    canvas_landscape.pack_forget()
    canvas_portrait_1.place_forget()
    canvas_portrait_2.pack_forget()
    photo_landscape.place_forget()
    photo_portrait_1.place_forget()
    photo_portrait_2.place_forget()
    add_landscape_photo_button.place_forget()
    add_protrait_photo_button_1.place_forget()
    add_protrait_photo_button_2.place_forget()
    photo_frame.pack_forget()
    text_label.place_forget()


def option1_selected():
    print("option 1 selected")
    if selected_option.get() != 1:
        selected_option.set(1)
        # Reset
        forget_all()
        entry_text.set("Enter photo caption")
        text_entry.pack(expand=True)
        # Set correct sizes for the frames
        # Calculate the photo width given the border percentages
        # 1.3 * photo_width = photo_frame_width => photo_width = photo_frame_width / 1.3
        selected_photo_width.set(photo_frame_width.get() / (1 + left_margin.get() + right_margin.get()))
        # Calculate photo height using the photo aspect ratio
        # photo_width/photo_height = photo_aspect_ratio
        selected_photo_height.set(selected_photo_width.get() / photo_aspect_ratio.get())
        # Calculate the photo frame height using the margins
        # 1.2 * photo_height = photo_frame_height
        photo_frame_height.set((1 + top_margin.get() + bottom_margin.get()) * selected_photo_height.get())
        photo_landscape.configure(width=selected_photo_width.get(), height=selected_photo_height.get())
        canvas_landscape.configure(width=selected_photo_width.get(), height=selected_photo_height.get())
        photo_frame.configure(width=photo_frame_width.get(), height=photo_frame_height.get())
        photo_frame.pack(expand=True, side=LEFT)
        rel_photo_1_x.set(left_margin.get() * selected_photo_width.get() / photo_frame_width.get())
        rel_photo_1_y.set(top_margin.get() * selected_photo_height.get() / photo_frame_height.get())
        photo_landscape.place(relx=rel_photo_1_x.get(), rely=rel_photo_1_y.get())
        add_landscape_photo_button.place(x=int(selected_photo_width.get() / 2), y=int(selected_photo_height.get() / 2), anchor=CENTER)
        text_width.set(selected_photo_width.get())
        text_label.configure(width=text_width.get())
        rel_text_x.set(((left_margin.get() * selected_photo_width.get()) + (selected_photo_width.get() / 2)) / photo_frame_width.get())
        rel_text_y.set((top_margin.get() * selected_photo_height.get() + selected_photo_height.get() + (bottom_margin.get() * selected_photo_height.get() / 2)) / photo_frame_height.get())
        text_label.place(relx=rel_text_x.get(), rely=rel_text_y.get(), anchor=CENTER, width=text_width.get())

def option2_selected():
    print("option 2 selected")
    if selected_option.get() != 2:
        selected_option.set(2)
        # Reset
        forget_all()
        entry_text.set("Enter photo caption")
        text_entry.pack(expand=True)
        landscape_photo_width.set((photo_frame_width.get() / (1 + left_margin.get() + right_margin.get())))
        landscape_photo_height.set((landscape_photo_width.get() / photo_aspect_ratio.get()))
        selected_photo_width.set((landscape_photo_width.get() - center_margin.get() * landscape_photo_width.get()) / 2)
        selected_photo_height.set(photo_aspect_ratio.get() * selected_photo_width.get())
        photo_frame_height.set(selected_photo_height.get() + (top_margin.get() + bottom_margin.get()) * landscape_photo_height.get())
        photo_portrait_1.configure(width=selected_photo_width.get(), height=selected_photo_height.get())
        photo_portrait_2.configure(width=selected_photo_width.get(), height=selected_photo_height.get())
        canvas_portrait_1.configure(width=selected_photo_width.get(), height=selected_photo_height.get())
        canvas_portrait_2.configure(width=selected_photo_width.get(), height=selected_photo_height.get())
        photo_frame.configure(width=photo_frame_width.get(), height=photo_frame_height.get())
        photo_frame.pack(expand=True, side=LEFT)
        rel_photo_1_x.set((left_margin.get() * landscape_photo_width.get()) / photo_frame_width.get())
        rel_photo_1_y.set(top_margin.get() * landscape_photo_height.get() / photo_frame_height.get())
        photo_portrait_1.place(relx=rel_photo_1_x.get(), rely=rel_photo_1_y.get())
        add_protrait_photo_button_1.place(x=int(selected_photo_width.get() / 2), y=int(selected_photo_height.get() / 2), anchor=CENTER)
        rel_photo_2_x.set((selected_photo_width.get() + (center_margin.get() + left_margin.get()) * landscape_photo_width.get()) / photo_frame_width.get())
        rel_photo_2_y.set(top_margin.get() * landscape_photo_height.get() / photo_frame_height.get())
        photo_portrait_2.place(relx=rel_photo_2_x.get(), rely=rel_photo_2_y.get())
        add_protrait_photo_button_2.place(x=int(selected_photo_width.get() / 2), y=int(selected_photo_height.get() / 2), anchor=CENTER)
        text_width.set(selected_photo_width.get() * 2)
        text_label.configure(width=text_width.get())
        rel_text_x.set(((left_margin.get() * landscape_photo_width.get()) + selected_photo_width.get() + (center_margin.get() * landscape_photo_width.get())/2) / photo_frame_width.get())
        rel_text_y.set((top_margin.get() * landscape_photo_height.get() + selected_photo_height.get() + (bottom_margin.get() * landscape_photo_height.get() / 2)) / photo_frame_height.get())
        text_label.place(relx=rel_text_x.get(), rely=rel_text_y.get(), anchor=CENTER, width=text_width.get())


def option3_selected():
    print("option 3 selected")
    if selected_option.get() != 3:
        selected_option.set(3)
        # Reset
        forget_all()
        entry_text.set("Enter photo caption")
        text_entry.pack(expand=True)
        # Set correct sizes for the frames
        # Calculate the photo width given the border percentages
        # 1.3 * photo_width = photo_frame_width => photo_width = photo_frame_width / 1.3
        selected_photo_width.set(photo_frame_width.get() / (1 + left_margin.get() + right_margin.get()))
        # Calculate photo height using the photo aspect ratio
        # photo_width/photo_height = photo_aspect_ratio
        selected_photo_height.set(selected_photo_width.get() / photo_aspect_ratio.get())
        # Calculate the photo frame height using the margins
        # 1.2 * photo_height = photo_frame_height
        photo_frame_height.set((1 + top_margin.get() + bottom_margin.get()) * selected_photo_height.get())
        photo_frame_width.set((1 + right_margin.get() + left_margin.get()) * selected_photo_height.get())
        photo_landscape.configure(width=selected_photo_width.get(), height=selected_photo_height.get())
        photo_frame.configure(width=photo_frame_width.get(), height=photo_frame_height.get())
        photo_frame.pack(expand=True, side=LEFT)
        rel_photo_1_x.set(left_margin.get() * selected_photo_width.get() / photo_frame_height.get())
        rel_photo_1_y.set(top_margin.get() * selected_photo_height.get() / photo_frame_height.get())
        photo_landscape.place(relx=rel_photo_1_x.get(), rely=rel_photo_1_y.get())
        multi_line_entry.config(state='normal', bg='light grey')
        multi_line_entry.delete(0.0, END)
        multi_line_entry.insert(0.0, "Enter text for page")
        photo_text_text.configure(bd=0, spacing2=10, bg="light grey", wrap=WORD, width=45)
        photo_text_text.place(x=int(selected_photo_width.get()/2), y=int(selected_photo_height.get()/2) + int(0.3*selected_photo_height.get()), anchor=CENTER)


page_type = tkinter.IntVar()
landscape_photo = Radiobutton(bottom_left_top_frame, bg="orange", text="Option1", value=1, variable=page_type, command=option1_selected)
two_portrait_photos = Radiobutton(bottom_left_bottom_frame, bg="orange", text="Option2", value=2, variable=page_type, command=option2_selected)
two_portrait_texts = Radiobutton(bottom_left_top_frame, bg="orange", text="Option3", value=3, variable=page_type, command=option3_selected)
two_portrait_photo_and_text = Radiobutton(bottom_left_bottom_frame, bg="orange", text="Option4", value=4, variable=page_type)
two_portrait_text_and_photo = Radiobutton(bottom_left_top_frame, bg="orange", text="Option5", value=5, variable=page_type)
landscape_text = Radiobutton(bottom_left_bottom_frame, bg="orange", text="Option6", value=6, variable=page_type)
page_type.set(1)

landscape_photo.pack(expand=True)
two_portrait_photos.pack(expand=True)
two_portrait_texts.pack(expand=True)
two_portrait_photo_and_text.pack(expand=True)
two_portrait_text_and_photo.pack(expand=True)
landscape_text.pack(expand=True)

bottom_middle_left_frame = Frame(bottom_middle_frame, bg='light green', width=int(bottom_width / 2), height=bottom_height)
bottom_middle_right_frame = Frame(bottom_middle_frame, bg='light green', width=int(bottom_width / 2), height=bottom_height)
bottom_middle_left_frame.pack(expand=True, fill=BOTH, side=LEFT)
bottom_middle_right_frame.pack(expand=True, fill=BOTH, side=RIGHT)


# Initialize slider value variables
left_border_percentage = DoubleVar()
left_border_percentage.set(20)
right_border_percentage = DoubleVar()
right_border_percentage.set(10)
top_border_percentage = DoubleVar()
top_border_percentage.set(10)
bottom_border_percentage = DoubleVar()
bottom_border_percentage.set(10)
center_border_percentage = DoubleVar()
center_border_percentage.set(10)

left_margin_scale = Scale(bottom_middle_left_frame, label="Left margin %", variable=left_border_percentage, orient=HORIZONTAL)


def left_margin_change(val):
    left_margin.set(int(val)/100)
    photo_frame.pack_forget()
    im = Image.open(file_name_1.get())
    photo_aspect_ratio.set(im.size[0] / im.size[1])
    # Calculate the photo width given the border percentages
    # 1.3 * photo_width = photo_frame_width => photo_width = photo_frame_width / 1.3
    selected_photo_width.set(photo_frame_width.get() / (1 + left_margin.get() + right_margin.get()))
    # Calculate photo height using the photo aspect ratio
    # photo_width/photo_height = photo_aspect_ratio
    selected_photo_height.set(selected_photo_width.get() / photo_aspect_ratio.get())
    # Calculate the photo frame height using the margins
    # 1.2 * photo_height = photo_frame_height
    photo_frame_height.set((1 + top_margin.get() + bottom_margin.get()) * selected_photo_height.get())
    photo_frame.configure(width=photo_frame_width.get(), height=photo_frame_height.get())
    photo_frame.pack(expand=True, side=LEFT)
    rel_photo_1_x.set(left_margin.get() * selected_photo_width.get() / photo_frame_width.get())
    rel_photo_1_y.set(top_margin.get() * selected_photo_height.get() / photo_frame_height.get())
    photo_landscape.configure(width=selected_photo_width.get(), height=selected_photo_height.get())
    photo_landscape.place(relx=rel_photo_1_x.get(), rely=rel_photo_1_y.get())
    if text_label.winfo_height() > (bottom_margin.get() * selected_photo_height.get()):
        print("text lable big")
        text_label.place_forget()
        text_label.forget()
    else:
        rel_text_x.set(((left_margin.get() * selected_photo_width.get()) + (
                    selected_photo_width.get() / 2)) / photo_frame_width.get())
        rel_text_y.set((top_margin.get() * selected_photo_height.get() + selected_photo_height.get() + (
                    bottom_margin.get() * selected_photo_height.get() / 2)) / photo_frame_height.get())
        text_label.place(relx=rel_text_x.get(), rely=rel_text_y.get(), anchor=CENTER, width=text_width.get())
    size = selected_photo_width.get(), selected_photo_height.get()
    im.thumbnail(size)
    canvas_landscape.image = ImageTk.PhotoImage(im)
    canvas_landscape.create_image(0, 0, image=canvas_landscape.image, anchor=NW)
    canvas_landscape.pack()


left_margin_scale.configure(command=left_margin_change, state=DISABLED, bg="light grey", relief=SUNKEN)

right_margin_scale = Scale(bottom_middle_left_frame, label="Right margin %", variable=right_border_percentage, orient=HORIZONTAL)


def right_margin_change(val):
    right_margin.set(int(val)/100)
    photo_frame.pack_forget()
    im = Image.open(file_name_1.get())
    photo_aspect_ratio.set(im.size[0] / im.size[1])
    # Calculate the photo width given the border percentages
    # 1.3 * photo_width = photo_frame_width => photo_width = photo_frame_width / 1.3
    selected_photo_width.set(photo_frame_width.get() / (1 + left_margin.get() + right_margin.get()))
    # Calculate photo height using the photo aspect ratio
    # photo_width/photo_height = photo_aspect_ratio
    selected_photo_height.set(selected_photo_width.get() / photo_aspect_ratio.get())
    # Calculate the photo frame height using the margins
    # 1.2 * photo_height = photo_frame_height
    photo_frame_height.set((1 + top_margin.get() + bottom_margin.get()) * selected_photo_height.get())
    photo_frame.configure(width=photo_frame_width.get(), height=photo_frame_height.get())
    photo_frame.pack(expand=True, side=LEFT)
    rel_photo_1_x.set(left_margin.get() * selected_photo_width.get() / photo_frame_width.get())
    rel_photo_1_y.set(top_margin.get() * selected_photo_height.get() / photo_frame_height.get())
    photo_landscape.configure(width=selected_photo_width.get(), height=selected_photo_height.get())
    photo_landscape.place(relx=rel_photo_1_x.get(), rely=rel_photo_1_y.get())
    if text_label.winfo_height() > (bottom_margin.get() * selected_photo_height.get()):
        text_label.place_forget()
        text_label.forget()
    else:
        rel_text_x.set(((left_margin.get() * selected_photo_width.get()) + (
                    selected_photo_width.get() / 2)) / photo_frame_width.get())
        rel_text_y.set((top_margin.get() * selected_photo_height.get() + selected_photo_height.get() + (
                    bottom_margin.get() * selected_photo_height.get() / 2)) / photo_frame_height.get())
        text_label.place(relx=rel_text_x.get(), rely=rel_text_y.get(), anchor=CENTER, width=text_width.get())
    size = selected_photo_width.get(), selected_photo_height.get()
    im.thumbnail(size)
    canvas_landscape.image = ImageTk.PhotoImage(im)
    canvas_landscape.create_image(0, 0, image=canvas_landscape.image, anchor=NW)
    canvas_landscape.pack()


right_margin_scale.configure(command=right_margin_change, state=DISABLED, bg="light grey", relief=SUNKEN)

top_margin_scale = Scale(bottom_middle_right_frame, label="Top margin %", variable=top_border_percentage, orient=HORIZONTAL)


def top_margin_change(val):
    top_margin.set(int(val)/100)
    photo_frame.pack_forget()
    im = Image.open(file_name_1.get())
    photo_aspect_ratio.set(im.size[0] / im.size[1])
    # Calculate the photo width given the border percentages
    # 1.3 * photo_width = photo_frame_width => photo_width = photo_frame_width / 1.3
    selected_photo_height.set(photo_frame_height.get() / (1 + top_margin.get() + bottom_margin.get()))
    # Calculate photo height using the photo aspect ratio
    # photo_width/photo_height = photo_aspect_ratio
    selected_photo_width.set(photo_aspect_ratio.get() * selected_photo_height.get())
    # Calculate the photo frame height using the margins
    # 1.2 * photo_height = photo_frame_height
    photo_frame_height.set((1 + top_margin.get() + bottom_margin.get()) * selected_photo_height.get())
    photo_frame.configure(width=photo_frame_width.get(), height=photo_frame_height.get())
    photo_frame.pack(expand=True, side=LEFT)
    rel_photo_1_x.set(left_margin.get() * selected_photo_width.get() / photo_frame_width.get())
    rel_photo_1_y.set(top_margin.get() * selected_photo_height.get() / photo_frame_height.get())
    photo_landscape.configure(width=selected_photo_width.get(), height=selected_photo_height.get())
    photo_landscape.place(relx=rel_photo_1_x.get(), rely=rel_photo_1_y.get())
    if text_label.winfo_height() > (bottom_margin.get() * selected_photo_height.get()):
        text_label.place_forget()
        text_label.forget()
    else:
        rel_text_x.set(((left_margin.get() * selected_photo_width.get()) + (selected_photo_width.get() / 2)) / photo_frame_width.get())
        rel_text_y.set((top_margin.get() * selected_photo_height.get() + selected_photo_height.get() + (bottom_margin.get() * selected_photo_height.get() / 2)) / photo_frame_height.get())
        text_label.place(relx=rel_text_x.get(), rely=rel_text_y.get(), anchor=CENTER, width=text_width.get())
    size = selected_photo_width.get(), selected_photo_height.get()
    im.thumbnail(size)
    canvas_landscape.image = ImageTk.PhotoImage(im)
    canvas_landscape.create_image(0, 0, image=canvas_landscape.image, anchor=NW)
    canvas_landscape.pack()


top_margin_scale.configure(command=top_margin_change, state=DISABLED, bg="light grey", relief=SUNKEN)

bottom_margin_scale = Scale(bottom_middle_right_frame, label="Bottom margin %", variable=bottom_border_percentage, orient=HORIZONTAL)


def bottom_margin_change(val):
    bottom_margin.set(int(val)/100)
    photo_frame.pack_forget()
    im = Image.open(file_name_1.get())
    photo_aspect_ratio.set(im.size[0] / im.size[1])
    # Calculate the photo width given the border percentages
    # 1.3 * photo_width = photo_frame_width => photo_width = photo_frame_width / 1.3
    selected_photo_height.set(photo_frame_height.get() / (1 + top_margin.get() + bottom_margin.get()))
    # Calculate photo height using the photo aspect ratio
    # photo_width/photo_height = photo_aspect_ratio
    selected_photo_width.set(photo_aspect_ratio.get() * selected_photo_height.get())
    # Calculate the photo frame height using the margins
    # 1.2 * photo_height = photo_frame_height
    photo_frame_height.set((1 + top_margin.get() + bottom_margin.get()) * selected_photo_height.get())
    photo_frame.configure(width=photo_frame_width.get(), height=photo_frame_height.get())
    photo_frame.pack(expand=True, side=LEFT)
    rel_photo_1_x.set(left_margin.get() * selected_photo_width.get() / photo_frame_width.get())
    rel_photo_1_y.set(top_margin.get() * selected_photo_height.get() / photo_frame_height.get())
    photo_landscape.configure(width=selected_photo_width.get(), height=selected_photo_height.get())
    photo_landscape.place(relx=rel_photo_1_x.get(), rely=rel_photo_1_y.get())
    if text_label.winfo_height() > (bottom_margin.get() * selected_photo_height.get()):
        text_label.place_forget()
        text_label.forget()
    else:
        rel_text_x.set(((left_margin.get() * selected_photo_width.get()) + (selected_photo_width.get() / 2)) / photo_frame_width.get())
        rel_text_y.set((top_margin.get() * selected_photo_height.get() + selected_photo_height.get() + (bottom_margin.get() * selected_photo_height.get() / 2)) / photo_frame_height.get())
        text_label.place(relx=rel_text_x.get(), rely=rel_text_y.get(), anchor=CENTER, width=text_width.get())
    size = selected_photo_width.get(), selected_photo_height.get()
    im.thumbnail(size)
    canvas_landscape.image = ImageTk.PhotoImage(im)
    canvas_landscape.create_image(0, 0, image=canvas_landscape.image, anchor=NW)
    canvas_landscape.pack()


bottom_margin_scale.configure(command=bottom_margin_change, state=DISABLED, bg="light grey", relief=SUNKEN)

center_margin_scale = Scale(bottom_middle_right_frame, label="Center margin %", variable=center_border_percentage, orient=HORIZONTAL)


def center_margin_change(val):
    center_margin.set(int(val)/100)


center_margin_scale.configure(command=center_margin_change, state=DISABLED, bg="light grey", relief=SUNKEN)

left_margin_scale.pack(expand=True)
right_margin_scale.pack(expand=True)
top_margin_scale.pack(expand=True)
bottom_margin_scale.pack(expand=True)
center_margin_scale.pack(expand=True)

caption_label = Label(bottom_right_frame, text="Caption", bg="pink")
caption_label.pack()

entry_text = StringVar()
entry_text.set("Enter photo caption")


def text_entry_validation():
    if entry_text.get() != "Enter photo caption":
        text.set(entry_text.get())
        text_label.place(relx=rel_text_x.get(), rely=rel_text_y.get(), anchor=CENTER, width=text_width.get())
    else:
        text.set("Photo Caption")
        text_label.place(relx=rel_text_x.get(), rely=rel_text_y.get(), anchor=CENTER, width=text_width.get())
    return True


validation = bottom_right_frame.register(text_entry_validation)
text_entry = Entry(bottom_right_frame, justify=CENTER, textvariable=entry_text, width=int(bottom_frames_width / 6),
                   fg="black", bg="white", validate="all", validatecommand=validation)
text_entry.pack(expand=True)

bottom_right_frame_width = int(bottom_frames_width / 5)
multi_line_entry = ScrolledText(bottom_right_frame, width=int(4 * bottom_right_frame_width/5),
                                height=int(bottom_frames_height / 6))
multi_line_entry.insert(0.0, "Text page - Not available for photo option")
multi_line_entry.pack(expand=True)
multi_line_entry.config(state='disabled', bg='light grey')
multi_line_entry_button = Button(bottom_right_frame, text="Add")
multi_line_entry_button.pack(expand=True)


def multi_line_entry_button_clicked():
    print("add text")
    input_text = multi_line_entry.get(0.0, END)
    photo_text_text.delete(0.0, END)
    photo_text_text.insert(0.0, input_text)
    print(input_text)


multi_line_entry_button.configure(command=multi_line_entry_button_clicked)


def reset_button_clicked():
    if selected_option.get() == 1:
        left_margin_scale.set(value=20)
        right_margin_scale.set(value=10)
        bottom_margin_scale.set(value=10)
        top_margin_scale.set(value=10)
        center_margin_scale.set(value=10)
        selected_option.set(0)
        option1_selected()
    elif selected_option.get() == 2:
        selected_option.set(0)
        option2_selected()
    elif selected_option.get() == 3:
        selected_option.set(0)
        option3_selected()
    entry_text.set("Enter photo caption")
    text_entry.pack(expand=True)
    canvas_landscape.pack_forget()
    canvas_portrait_1.pack_forget()
    canvas_portrait_2.pack_forget()


black = (0, 0, 0)
white = (255, 255, 255, 100)
arial = "arial.ttf"


def save_button_clicked():
    aspect_ratio = 1.3333
    if selected_option.get() == 1:
        print("saving landscape photo")
        save_image = Image.open(file_name_1.get())
        image_width = save_image.size[0]
        image_height = save_image.size[1]
        # Create canvas with same margins for all photos
        save_canvas_height = int((top_margin.get() + bottom_margin.get()) * image_height + image_height)
        save_canvas_width = int(((right_margin.get() + left_margin.get()) * image_height) + (aspect_ratio * image_height))
        save_canvas = Image.new(save_image.mode, (save_canvas_width, save_canvas_height), black)
        print(image_height, image_width, save_canvas_width, save_canvas_height)
        # Image placement in the canvas
        image_x = save_canvas_width - image_width - int((save_canvas_width - image_width)/3)
        image_y = int(top_margin.get() * image_height)
        save_canvas.paste(save_image, (image_x, image_y))
        # Caption placement in the canvas
        draw = ImageDraw.Draw(save_canvas)
        font = ImageFont.truetype(arial, size=100)
        # Find the text size to figure out where to h elp center the text
        save_text_width, save_text_height = draw.textsize(entry_text.get(), font)
        # Center the text horizontally and center it vertically on the lower border
        text_x = int((save_canvas_width - (image_width/2) - ((save_canvas_width - image_width)/3)) - (save_text_width/2))
        # Margin is 16% so center of lower margin will be image height plus 12%
        text_y = save_canvas_height - int(bottom_margin.get() * image_height / 2) - int(save_text_height / 2)
        draw.text((text_x, text_y), entry_text.get(), font=font, fill=white)
        new_filename = destination_folder_name + "/" + file_name_1.get().split("/")[-1]
        save_canvas.save(new_filename)
    elif selected_option.get() == 2:
        center_margin.set(0.03)
        print("saving two portraits photos")
        save_image1 = Image.open(file_name_1.get())
        save_image2 = Image.open(file_name_2.get())
        image_width = save_image1.size[0]
        image_height = save_image1.size[1]
        photo_aspect_ratio.set(image_width/image_height)
        save_canvas_height = int((top_margin.get() + bottom_margin.get()) * image_height + image_height)
        save_canvas_width = int(((right_margin.get() + left_margin.get()) * image_height) + (aspect_ratio * image_height))
        photo_height = image_height
        photo_width = photo_height/photo_aspect_ratio.get()
        save_canvas = Image.new(save_image1.mode, (save_canvas_width, save_canvas_height), black)
        image_x_1 = int(save_canvas_width - ((right_margin.get() + center_margin.get()) * image_height) - (2 * photo_width))
        image_y_1 = int(top_margin.get() * image_height)
        size = photo_width, photo_height
        print(photo_height, photo_width, save_canvas_width, save_canvas_height)
        save_image1 = save_image1.transpose(Image.ROTATE_270)
        save_image1.thumbnail(size)
        save_canvas.paste(save_image1, (image_x_1, image_y_1))
        image_x_2 = int(save_canvas_width - (right_margin.get() * image_height) - photo_width)
        image_y_2 = int(top_margin.get() * image_height)
        save_image2 = save_image2.transpose(Image.ROTATE_270)
        save_image2.thumbnail(size)
        save_canvas.paste(save_image2, (image_x_2, image_y_2))
        draw = ImageDraw.Draw(save_canvas)
        font = ImageFont.truetype(arial, size=70)
        save_text_width, save_text_height = draw.textsize(entry_text.get(), font)
        text_x = int(save_canvas_width - photo_width - (right_margin.get() * photo_height) - (center_margin.get() * photo_height/2) - (save_text_width / 2))
        text_y = int(save_canvas_height - (bottom_margin.get() * image_height / 2) - (save_text_height / 2))
        draw.text((text_x, text_y), entry_text.get(), font=font, fill=white)
        new_filename = destination_folder_name + "/" + file_name_1.get().split("/")[-1]
        save_canvas.save(new_filename)
    elif selected_option.get() == 3:
        print("saving landscape text")
        photo_frame_width.set(0.8 * left_width)
        # 1.5ph + (l+r * ph)) = pfw
        text_box_height = int(photo_frame_width.get() / (left_margin.get() + right_margin.get() + aspect_ratio))
        text_box_width = int(text_box_height * aspect_ratio)
        photo_frame_height.set(text_box_height + (text_box_height * (top_margin.get() + bottom_margin.get())))
        save_canvas = Image.new("RGBX", (int(photo_frame_width.get()), int(photo_frame_height.get())), black)
        draw = ImageDraw.Draw(save_canvas)
        x1 = int(left_margin.get() * text_box_height)
        y1 = int(top_margin.get() * text_box_height)
        x2 = int((left_margin.get() * text_box_height) + text_box_width)
        y2 = int((1 + top_margin.get()) * text_box_height)
        draw.rectangle([x1, y1, x2, y2], fill=white)
        font = ImageFont.truetype(arial, size=40)
        lines = textwrap.wrap(multi_line_entry.get(0.0, END), width=78)
        save_text = textwrap.fill(multi_line_entry.get(0.0, END), width=78, expand_tabs=False)
        tw, th = draw.textsize(lines[0], font)
        text_x = int(x1 + ((x2 - x1 - tw)/2))
        height = lines.__len__() * (th + 10)
        text_y = int(y1 + ((y2 - y1 - height)/2))
        draw.text((text_x, text_y), save_text, font=font, fill=black, spacing=15)
        new_filename = destination_folder_name + "/" + "mytxt" + ".jpg"
        save_canvas.save(new_filename)


reset_button = Button(buttons_frame, text="Reset", command=reset_button_clicked)
reset_button.pack()

label = Label(buttons_frame, bg='light blue')
label.pack()

save_button = Button(buttons_frame, text="Save", command=save_button_clicked)
save_button.pack()
option1_selected()
root.mainloop()