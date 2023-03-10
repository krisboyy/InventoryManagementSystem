
from pathlib import Path
from tkinter import *
import mysql.connector

cnx = mysql.connector.connect(
    host="localhost",
    user="root",
    password="3278",
    database="inventory"
)
cursor = cnx.cursor()

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\nykkr\Dropbox\DBMS Project\InventoryManagementSystem\build\assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()
window.geometry("1440x1024")
window.configure(bg = "#FED954")



canvas = Canvas(
    window,
    bg = "#FED954",
    height = 1024,
    width = 1440,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)

canvas.create_rectangle(
    0,
    0.0,
    200.0,
    1024.0,
    fill="#EFDEA3",
    outline="")

rectangle=canvas.create_rectangle(
    242.0,
    81.0,
    1400.0,
    900.0,
    fill="#EFDEA3",
    outline="")

scrollbar=Tk.Scrollbar(window, orient="vertical", command=canvas.yview)
canvas.configure(yscrollcommand=scrollbar.set)
scrollbar.pack(side="right", fill="y")

rectangle.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

'''v = Scrollbar(window)
v.pack(side = RIGHT, fill = Y)
t = Text(242.0, 81.0, width = 100, height = 30, wrap = NONE, yscrollcommand = v.set)'''

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))

button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    #command=check_pw,
    relief="flat"
)
button_1.place(
    x=15.0,
    y=947.0,
    width=191.0,
    height=61.0
)

image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    106.0,
    859.0,
    image=image_image_1
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_2 clicked"),
    relief="flat"
)
button_2.place(
    x=0.0,
    y=250.0,
    width=198.0,
    height=61.0
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_3 clicked"),
    relief="flat"
)
button_3.place(
    x=0.0,
    y=172.0,
    width=198.0,
    height=61.0
)

'''get_inv():
    query = "SELECT * FROM inventory.item "
    cursor.execute(query)
    results=cursor.fetchall()
    t.delete("1.0", END)
    for result in results:
        for x in [0,1,2]:
            t.insert(END, result + " ")
        t.insert(END, "\n")'''

button_image_4 = PhotoImage(
    file=relative_to_assets("button_4.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    #command=get_inv,
    relief="flat"
)


#def logout():
    
   #session.pop('loggedin', None)
   #session.pop('id', None)
   #session.pop('username', None)
   #return redirect(url_for('login'))


button_4.place(
    x=0.0,
    y=94.0,
    width=198.0,
    height=61.0
)

window.resizable(False, False)
window.mainloop()
