import os
import tkinter as tk
import requests
# import main

HEIGHT = 500
WIDTH = 500


def test_function(home_entry, file_name, junior, alphabet):
    print("This is the home entry:", home_entry)
    print("This is the file name:", file_name)
    print("Check box junior:", junior)
    print("Check box alphabet:", alphabet)


def hello(input1, input2):
    print("Hello World!")
    print("this is the first", input1)
    print("this is the second", input2)


root = tk.Tk()

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

# background_image = tk.PhotoImage(file='parkrun_logo.png')
# background_label = tk.Label(root, image=background_image)
# background_label.place(relwidth=1)

###
home_frame = tk.Frame(root, bg='#8b8d09', bd=5)
home_frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.2, anchor='n')

lat_label = tk.Label(home_frame, text="Latitude")
lat_label.place(relwidth=0.48, relheight=0.3)
lat_label = tk.Label(home_frame, text="Longitude")
lat_label.place(relx=0.52, relwidth=0.48, relheight=0.3)

lat_entry = tk.Entry(home_frame, font=40)
lat_entry.place(rely=0.35, relwidth=0.48, relheight=0.65)
long_entry = tk.Entry(home_frame, font=40)
long_entry.place(relx=0.52, rely=0.35, relwidth=0.48, relheight=0.65)

###
file_frame = tk.Frame(root, bg='#8b8d09', bd=5)
file_frame.place(relx=0.5, rely=0.35, relwidth=0.75, relheight=0.2, anchor='n')

file_label = tk.Label(file_frame, text="File name for parkruns done")
file_label.place(relwidth=1, relheight=0.3)

file_entry = tk.Entry(file_frame, font=40)
file_entry.place(rely=0.35, relwidth=1, relheight=0.65)


###
options_frame = tk.Frame(root, bg='#8b8d09', bd=5)
options_frame.place(relx=0.5, rely=0.6, relwidth=0.75, relheight=0.2, anchor='n')

options_label = tk.Label(options_frame, text="Things to show")
options_label.place(relwidth=1, relheight=0.3)

C_junior_int = tk.IntVar()
C_junior = tk.Checkbutton(options_frame, text="Junior", variable=C_junior_int, onvalue=1, offvalue=0)
C_junior.place(rely=0.35)

C_alphabet_int = tk.IntVar()
C_alphabet = tk.Checkbutton(options_frame, text="Alphabet", variable=C_alphabet_int, onvalue=1, offvalue=0)
C_alphabet.place(rely=0.35, relx=0.5)

###
button_frame = tk.Frame(root, bg='#8b8d09', bd=5)
button_frame.place(relx=0.5, rely=0.85, relwidth=0.75, relheight=0.1, anchor='n')

button = tk.Button(button_frame, text="Go", font=40,
                   command=lambda: test_function([lat_entry.get(), long_entry.get()],file_entry.get(),
                                                 C_junior_int.get(), C_alphabet_int.get()))
button.place(relwidth=1, relheight=1)

root.mainloop()
