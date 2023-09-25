import os


from tkinter import *
from tkinter.filedialog import askopenfilenames
from tkinter.messagebox import showerror
import os
import time
import subprocess

path_this = ""
paths_tuple = ()


def start_command_sub(*command):
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    # return process.communicate()
    # print(stdout.decode() + stderr.decode())
    return stdout.decode() + stderr.decode()


def to_print(files):
    for idx, file in enumerate(files):
        try:
            start_command_sub(
                "wkhtmltopdf",
                "--enable-local-file-access",
                f"{file}",
                f"{path_this}/pdfs/out{idx}.pdf",
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


btn = Button(root, text="Print", width=15, command=lambda: to_print(paths_tuple)).pack()
root.mainloop()
