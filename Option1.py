from AppElements import *


def option1_selected():
    print("option1_selected")
    reset_all()
    if option_selected.get() != 1:
        option_selected.set(1)
        photo_frame_display.pack(expand=True)
        photo.place(relx=rel_x, rely=rel_y)
        add_button.configure(command=add_button_clicked)
        add_button.place(x=int(photo_display_width / 2), y=int(photo_display_height / 2), anchor=CENTER)

def add_button_clicked():
    print("Add button clicked")
    file = filedialog.askopenfile(parent=photo, title='Choose source folder')
    if file is None:
        image_path.set(None)
    else:
        image_path.set(file.name)
    if(option_selected.get() == 1) and file != None:
        add_button.place_forget()
        display_landscape()

def display_landscape():
    print("display landscape")
    im = Image.open(image_path.get())
    photo_aspect_ratio = im.size[0] / im.size[1]
    size = photo_display_width, photo_display_height/photo_aspect_ratio
    im.thumbnail(size)
    canvas.configure(width=size[0], height=size[1])
    canvas.image = ImageTk.PhotoImage(im)
    canvas.create_image(0, 0, image=canvas.image, anchor=NW)  
    canvas.pack()