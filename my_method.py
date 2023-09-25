import os
import pdfkit

from tkinter import *
from tkinter.filedialog import askopenfilenames
from tkinter.messagebox import showerror
import os
import time

file_to_print = ""
paths_tuple = ()
path_this = ""


def print_files(files):
    for idx, file in enumerate(files):
        try:
            pdfkit.from_file(
                file,
                f"./pdfs/out{idx}.pdf",
                # verbose=True,
                options={"enable-local-file-access": True},
            )
            time.sleep(0.1)
            os.startfile(
                f"{path_this}/pdfs/out{idx}.pdf",
                "print",
            )
        except Exception as e:
            showerror("Error", message="printing Error", detail=e)


def select_files():
    global paths_tuple, path_this
    paths_tuple = askopenfilenames(
        parent=root, filetypes=[("Text Files", "*.htm"), ("Text Files", "*.html")]
    )
    # print(paths_tuple)
    path_this = os.getcwd()


root = Tk()
root.title("Simple print Example")
root.geometry("300x300")
l = Label(text="Select ur desired file to print", bg="gray")
l.pack(fill=X)
btn_select = Button(
    text="Select File", width=15, bg="dark green", command=select_files
).pack()
l1 = Label(text="")
l1.pack(fill=X)


btn = Button(
    root, text="Print", width=15, command=lambda: print_files(paths_tuple)
).pack()
root.mainloop()
