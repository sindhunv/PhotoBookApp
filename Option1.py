from AppElements import *

# One landscape photo
def option1_selected():
    print("option1_selected")
    if option_selected.get() != 1:
        reset_all()
        option_selected.set(1)
        photo_frame_display.pack(expand=True)
        photo.place(relx=rel_x, rely=rel_y)
        add_button.configure(command=add_button_clicked)
        add_button.place(x=int(photo_display_width / 2), y=int(photo_display_height / 2), anchor=CENTER)        
        bottom_text_space = (photo_frame_display_height - photo_display_height)/2
        rel_text_x = (left_margin + (photo_display_width/2))/photo_frame_display_width
        rel_text_y = (photo_frame_display_height - (bottom_text_space/2))/photo_frame_display_height
        caption_label.place(relx=rel_text_x, rely=rel_text_y, anchor=CENTER)       

def add_button_clicked():
    print("Add button clicked")
    file = filedialog.askopenfile(parent=photo, title='Choose source folder')
    if file is None:
        image_path.set(None)
    else:
        image_path.set(file.name)
    if(option_selected.get() == 1) and file != None:
        add_button.place_forget()
        show.configure(command=show_landscape)
        save.configure(command=save_landscape)
        display_landscape()

def display_landscape():
    print("display landscape")
    im = Image.open(image_path.get())    
    if im.size[0] < im.size[1]:
        im = im.transpose(Image.ROTATE_270)
    photo_aspect_ratio = im.size[0] / im.size[1]
    size = photo_display_width, photo_display_width/photo_aspect_ratio
    im.thumbnail(size)
    canvas.configure(width=size[0], height=size[1])
    canvas.image = ImageTk.PhotoImage(im)
    canvas.create_image(0, 0, image=canvas.image, anchor=NW)  
    canvas.pack()

def save_landscape():
     print("save landscape")
     is_save.set("True")
     show_landscape()

def show_landscape():
    if image_path.get() is None:
        return
    print("show landscape")
    im = Image.open(image_path.get())
    if im.size[0] < im.size[1]:
        im = im.transpose(Image.ROTATE_270)
    photo_aspect_ratio = im.size[0] / im.size[1]
    photo_left_margin = (left_margin_percentage.get() * im.size[0])/100
    photo_right_margin = (right_margin_percentage.get() * im.size[0])/100
    photo_frame_show_width = photo_left_margin + photo_right_margin + im.size[0]
    photo_frame_show_height = photo_frame_show_width/aspect_ratio
    photo_top_margin = (photo_frame_show_height - im.size[1])/2
    size = (int(photo_frame_show_width), int(photo_frame_show_height))
    canvas = Image.new(im.mode, size , black)
    canvas.paste(im, (int(photo_left_margin), int(photo_top_margin)))
    draw = ImageDraw.Draw(canvas)
    text_font = ImageFont.truetype(arial, size=50)
    (text_width, text_height) = draw.textsize(text.get(), text_font)
    text_x = photo_left_margin + (im.size[0]/2) - (text_width/2)
    text_y = photo_top_margin + im.size[1] + (photo_top_margin/2) - (text_height/2)
    text_size = (int(text_x), int(text_y))
    draw.text(text_size, text.get(), font=text_font, fill=white)
    if is_save.get() == "False":
        canvas.show()
    else:
        new_filename = destination_folder_name.get() + "/" + image_path.get().split("/")[-1]
        canvas.save(new_filename)
        is_save.set("False")
    