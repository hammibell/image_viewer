from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog

root = Tk()
root.geometry("500x500")
root.title("Image Viewer")
root.configure(background = "light green")

image = Label(root, bg = "white", highlightthickness = 5)
image.place(relx = 0.5, rely = 0.2, anchor = CENTER)

img_path = ""

def open_image():
    global name
    filedialog.askopenfilename(title = "Open Text File", filetypes = [("Image Files", "*.jpg", "*.gif", "*.png", "*txt")])
    image = img_path


open_image_button = Button(root, text = "Open Image", command = open_image)
open_image_button.place(relx = 0.5, rely = 0.3, anchor = CENTER)

root.mainloop()