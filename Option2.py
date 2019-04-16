from AppElements import *

# Two portrait photos on one page
def option2_selected():
    print("option2_selected")
    reset_all()
    if option_selected.get() != 2:
        option_selected.set(2)        
        photo_frame_display.pack(expand=True)        
        photo1.place(relx=rel_x1, rely=rel_y1)        
        photo2.place(relx=rel_x2, rely=rel_y2)
        add_button1.configure(command=add_button1_clicked)
        add_button2.configure(command=add_button2_clicked)
        add_button1.place(x=int(photo_display_width_2 / 2), y=int(photo_display_height_2 / 2), anchor=CENTER)
        add_button2.place(x=int(photo_display_width_2 / 2), y=int(photo_display_height_2 / 2), anchor=CENTER)

def add_button1_clicked():
    print("Add button 1 clicked")
    file = filedialog.askopenfile(parent=photo1, title='Choose source folder')
    if file is None:
        image_path.set(None)
    else:
        image_path.set(file.name)
    if(option_selected.get() == 2) and file != None:
        add_button1.place_forget()
        display_portrait1(photo1)

def add_button2_clicked():
    print("Add button 2 clicked")
    file = filedialog.askopenfile(parent=photo2, title='Choose source folder')
    if file is None:
        image_path.set(None)
    else:
        image_path.set(file.name)
    if(option_selected.get() == 2) and file != None:
        add_button2.place_forget()
        display_portrait2(photo2)

def display_portrait1(frame):
    print("display portrait 2")
    display_portrait(frame, canvas1)

def display_portrait2(frame):
    print("display portrait 2")
    display_portrait(frame, canvas2)

def display_portrait(frame, c):
    print("display portrait")
    im = Image.open(image_path.get())
    if im.size[0] > im.size[1]:
        im = im.transpose(Image.ROTATE_270)
    photo_aspect_ratio = im.size[1] / im.size[0]
    size = photo_display_width_2, photo_display_width_2*photo_aspect_ratio
    im.thumbnail(size)    
    c.configure(width=size[0], height=size[1])
    c.image = ImageTk.PhotoImage(im)
    c.create_image(0, 0, image=c.image, anchor=NW)  
    c.pack()

def save_portrait():
    print("save landscape")