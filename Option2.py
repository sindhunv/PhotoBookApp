from AppElements import *

# Two portrait photos on one page
def option2_selected():
    print("option2_selected")
    if option_selected.get() != 2:
        reset_all()
        option_selected.set(2)        
        photo_frame_display.pack(expand=True)        
        photo1.place(relx=rel_x1, rely=rel_y1)        
        photo2.place(relx=rel_x2, rely=rel_y2)
        add_button1.configure(command=add_button1_clicked)
        add_button2.configure(command=add_button2_clicked)
        add_button1.place(x=int(photo_display_width_2 / 2), y=int(photo_display_height_2 / 2), anchor=CENTER)
        add_button2.place(x=int(photo_display_width_2 / 2), y=int(photo_display_height_2 / 2), anchor=CENTER)
        bottom_text_space = (photo_frame_display_height - photo_display_height_2)/2
        rel_text_x = (left_margin + (photo_display_width/2))/photo_frame_display_width
        rel_text_y = (photo_frame_display_height - (bottom_text_space/2))/photo_frame_display_height
        caption_label.place(relx=rel_text_x, rely=rel_text_y, anchor=CENTER) 

def add_button1_clicked():
    print("Add button 1 clicked")
    file = filedialog.askopenfile(parent=photo1, title='Choose source folder')
    if file is None:
        image_path1.set(None)
    else:
        image_path1.set(file.name)
    if(option_selected.get() == 2) and file != None:
        add_button1.place_forget()
        display_portrait1(photo1)
    if(image_path1.get() != None and image_path2.get() != None):
        show.configure(command=show_portrait)
        save.configure(command=save_portrait)
        
def add_button2_clicked():
    print("Add button 2 clicked")
    file = filedialog.askopenfile(parent=photo2, title='Choose source folder')
    if file is None:
        image_path2.set(None)
    else:
        image_path2.set(file.name)
    if(option_selected.get() == 2) and file != None:
        add_button2.place_forget()
        display_portrait2(photo2)
    if(image_path1.get() != None and image_path2.get() != None):
        show.configure(command=show_portrait)
        save.configure(command=save_portrait)

def display_portrait1(frame):
    print("display portrait 2")
    display_portrait(frame, image_path1.get(), canvas1)

def display_portrait2(frame):
    print("display portrait 2")
    display_portrait(frame, image_path2.get(), canvas2)

def display_portrait(frame, img, c):
    print("display portrait")
    im = Image.open(img)
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
     print("save portrait")
     is_save.set("True")
     show_portrait()

def show_portrait():
    if image_path1.get() is None:
        return
    if image_path2.get() is None:
        return
    print("show portrait")
    im1 = Image.open(image_path1.get())
    im2 = Image.open(image_path2.get())
    if im1.size[0] > im1.size[1]:
        im = im.transpose(Image.ROTATE_270)
    if im2.size[0] > im2.size[1]:
        im = im.transpose(Image.ROTATE_270)
    photo_aspect_ratio = im1.size[1] / im1.size[0]
    photo_left_margin = (left_margin_percentage.get() * im1.size[1])/100
    photo_right_margin = (right_margin_percentage.get() * im1.size[1])/100
    photo_center_margin = (center_margin_percentage.get() * im1.size[1])/100
    photo_frame_show_width = photo_left_margin + photo_right_margin + im1.size[1]
    photo_frame_show_height = photo_frame_show_width/aspect_ratio
    size = (int(photo_frame_show_width), int(photo_frame_show_height))
    canvas = Image.new(im1.mode, size , black)
    img_width = (photo_frame_show_width - photo_left_margin - photo_right_margin - photo_center_margin)/2
    img_height = img_width * photo_aspect_ratio
    img_size = (int(img_width), int(img_height))
    photo_top_margin = (photo_frame_show_height - img_height)/2
    im1.thumbnail(img_size)
    im2.thumbnail(img_size)
    canvas.paste(im1, (int(photo_left_margin), int(photo_top_margin)))
    canvas.paste(im2, (int(photo_left_margin+img_width+photo_center_margin), int(photo_top_margin)))
    draw = ImageDraw.Draw(canvas)
    text_font = ImageFont.truetype(arial, size=50)
    (text_width, text_height) = draw.textsize(text.get(), text_font)
    text_x = photo_left_margin + img_width + ((photo_center_margin)/2) - (text_width/2)
    text_y = photo_top_margin + img_height + (photo_top_margin/2) - (text_height/2)
    text_size = (int(text_x), int(text_y))
    draw.text(text_size, text.get(), font=text_font, fill=white)
    if is_save.get() == "False":
        canvas.show()
    else:
        new_filename = destination_folder_name.get() + "/" + image_path1.get().split("/")[-1]
        canvas.save(new_filename)
        is_save.set("False")