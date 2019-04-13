import textwrap
import tkinter
from tkinter import *
from tkinter import filedialog
from tkinter.scrolledtext import ScrolledText
from PIL import ImageTk
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
from AppElements import *
from Option1 import *
from Option2 import *
from Option3 import *

def main():
    landscape_photo.configure(command=option1_selected)
    two_portrait_photos.configure(command=option2_selected)
    landscape_text.configure(command=option3_selected)

    landscape_photo.pack(expand=True, side=LEFT)
    two_portrait_photos.pack(expand=True, side=LEFT)
    landscape_text.pack(expand=True, side=LEFT)

    option2_selected()
    page_type.set(option_selected.get())
    
    top.pack(expand=True, fill=BOTH)
    bottom.pack(expand=True, fill=BOTH)

    root.mainloop()

if __name__ == "__main__":
    main()