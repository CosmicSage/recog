from tkinter import *
from PIL import ImageTk, Image
from sql import *
app = Tk()
app.title("Welcome")
img =Image.open('222.ppm')
bg = ImageTk.PhotoImage(img)
import random
app.geometry("650x450")

# Add image
label = Label(app, image=bg)
label.place(x = 0,y = 0)

# Add text
label2 = Label(app, text = f"{random.randrange(0,100)}",
               font=("Times New Roman", 24))

label2.pack(pady = 50)

def refresh():
    t = cur.execute("SELECT * from presence").fetchall()
    label2.config(text=t)


refresh_button= Button(app, text="Refresh",command =refresh,font='bold', width=6)
refresh_button.pack()

# Execute tkinter
app.mainloop()
