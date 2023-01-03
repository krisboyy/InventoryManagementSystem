
from pathlib import Path
from tkinter import *
import subprocess
import tkinter as tk
import mysql.connector
from tkinter import ttk

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

with open("current_user.txt", "r") as f:
    user_id = f.read()
query="SELECT username FROM inventory.user WHERE userid=%s"
cursor.execute(query, (user_id,))
user_name=cursor.fetchone()
print(user_name)

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

text_id=canvas.create_text(
    332.0,
    485.0,
    anchor="nw",
    text="Select an option from the hamburger menu.",
    fill="#000000",
    font=("Inter Black", 45 * -1)
)

text_id2=canvas.create_text(
    50.0,
    885.0,
    anchor="nw",
    text="Hi, " + user_name[0],
    fill="#000000",
    font=("Inter Black", 30 * -1)
)

def inv_click():
    canvas.delete(text_id)
    canvas1 = Canvas(
        window,
        bg = "#EFDEA3",
        height = 862,
        width = 1154,
        bd = 1,
        highlightthickness = 0,
        relief = "ridge"
    )

    canvas1.place(x = 242, y = 80)
    canvas1.configure(scrollregion=(242, 81, 1400, 950))


   


    tree = ttk.Treeview(canvas1, columns=("column1", "column2", "column3"))
    tree.pack(fill="both", expand=True)
    tree.heading("#0", text="Serial Number")
    tree.column("#0", width=100)
    tree.heading("column1", text="Item ID")
    tree.column("#1", width=250)
    tree.heading("column2", text="Item Name")
    tree.column("#2", width=250)
    tree.heading("column3", text="Location")
    tree.column("#3", width=250)

    def get_inv():
        i=0
        query = "SELECT * FROM inventory.item "
        cursor.execute(query)
        results=cursor.fetchall()
        for result in results:
            tree.insert("", "end", text=i, values=(result[0], result[1], result[2]))
            i+=1
        
    get_inv()

def log_click():
    canvas.delete(text_id)
    canvas2 = Canvas(
        window,
        bg = "#EFDEA3",
        height = 862,
        width = 1154,
        bd = 1,
        highlightthickness = 0,
        relief = "ridge"
    )

    canvas2.place(x = 242, y = 80)
    canvas2.configure(scrollregion=(242, 81, 1400, 950))

    tree = ttk.Treeview(canvas2, columns=("column1", "column2", "column3", "column4", "column5", "column6", "column7"))
    tree.pack(fill="both", expand=True)
    tree.heading("#0", text="Serial Number")
    tree.column("#0", width=100)
    tree.heading("column1", text="Movement ID")
    tree.column("#1", width=150)
    tree.heading("column2", text="Item ID")
    tree.column("#2", width=150)
    tree.heading("column3", text="User ID")
    tree.column("#3", width=150)
    tree.heading("column4", text="Source")
    tree.column("#4", width=150)
    tree.heading("column5", text="Destination")
    tree.column("#5", width=150)
    tree.heading("column6", text="Movement Time")
    tree.column("#6", width=150)
    tree.heading("column7", text="Movement Date")
    tree.column("#7", width=150)

    def get_inv():
        i=0
        query = "SELECT * FROM inventory.movement "
        cursor.execute(query)
        results=cursor.fetchall()
        for result in results:
            tree.insert("", "end", text=i, values=(result[0], result[1], result[2], result[3], result[4], result[5], result[6]))
            i+=1
        
    get_inv()

def prof_click():
    canvas.delete(text_id)

    canvas2 = Canvas(
        window,
        bg = "#EFDEA3",
        height = 862,
        width = 1154,
        bd = 1,
        highlightthickness = 0,
        relief = "ridge"
    )

    canvas2.place(x = 242, y = 80)
    canvas2.configure(scrollregion=(242, 81, 1400, 950))


    tree = ttk.Treeview(canvas2, columns=("column1", "column2", "column3", "column4", "column5", "column6", "column7"))
    tree.pack(fill="both", expand=True)
    tree.heading("#0", text="Serial Number")
    tree.column("#0", width=100)
    tree.heading("column1", text="Movement ID")
    tree.column("#1", width=150)
    tree.heading("column2", text="Item ID")
    tree.column("#2", width=150)
    tree.heading("column3", text="User ID")
    tree.column("#3", width=150)
    tree.heading("column4", text="Source")
    tree.column("#4", width=150)
    tree.heading("column5", text="Destination")
    tree.column("#5", width=150)
    tree.heading("column6", text="Movement Time")
    tree.column("#6", width=150)
    tree.heading("column7", text="Movement Date")
    tree.column("#7", width=150)

    def get_inv():
        i=0
        query = "SELECT * FROM inventory.movement WHERE userid=%s "
        cursor.execute(query, (user_id,))
        results=cursor.fetchall()
        for result in results:
            tree.insert("", "end", text=i, values=(result[0], result[1], result[2], result[3], result[4], result[5], result[6]))
            i+=1
        
    get_inv()

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))

file_path=file_path=r"C:\Users\nykkr\Dropbox\DBMS Project\InventoryManagementSystem\build\gui1.py"

def open_file():
    window.destroy()
    subprocess.run(['python', file_path], shell=True)

def log_out():
    with open("current_user.txt", "w") as f:
                f.write("")
    open_file()

button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=log_out,
    relief="flat"
)
button_1.configure(background="#EFDEA3")
button_1.place(
    x=10.0,
    y=947.0,
    width=191.0,
    height=61.0
)

image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    106.0,
    800.0,
    image=image_image_1
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=prof_click,
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
    command=log_click,
    relief="flat"
)
button_3.place(
    x=0.0,
    y=172.0,
    width=198.0,
    height=61.0
)


button_image_4 = PhotoImage(
    file=relative_to_assets("button_4.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=inv_click,
    relief="flat"
)

button_4.place(
    x=0.0,
    y=94.0,
    width=198.0,
    height=61.0
)

window.resizable(False, False)
window.mainloop()
