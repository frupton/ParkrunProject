import os
import tkinter as tk
import requests
# import main

HEIGHT = 500
WIDTH = 500
MAIN_COLOUR = '#8b8d09'
BACKGROUND_COLOUR = '#3E3E78'


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
root.title("parkrun program")

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

backing_frame = tk.Frame(root, bg=BACKGROUND_COLOUR, bd=5)
backing_frame.place(relx=0.5, rely=0.5, relwidth=1, relheight=1, anchor='c')

# FRAMES SET UP
home_frame = tk.Frame(backing_frame, bg=MAIN_COLOUR, bd=5)
home_frame.place(relx=0.5, rely=0.03, relwidth=0.85, relheight=0.2, anchor='n')

file_frame = tk.Frame(backing_frame, bg=MAIN_COLOUR, bd=5)
file_frame.place(relx=0.5, rely=0.25, relwidth=0.85, relheight=0.16, anchor='n')

options_frame = tk.Frame(backing_frame, bg=MAIN_COLOUR, bd=5)
options_frame.place(relx=0.5, rely=0.43, relwidth=0.85, relheight=0.2, anchor='n')

radiobutton_frame = tk.Frame(backing_frame, bg=MAIN_COLOUR)
radiobutton_frame.place(relx=0.5, rely=0.65, relwidth=0.85, relheight=0.2, anchor='n')

button_frame = tk.Frame(backing_frame, bg=MAIN_COLOUR, bd=5)
button_frame.place(relx=0.5, rely=0.87, relwidth=0.85, relheight=0.1, anchor='n')

# INSIDE HOME FRAME
header_label = tk.Label(home_frame, text="What is your home location?", bg=MAIN_COLOUR)
header_label.place(relwidth=1)
lat_label = tk.Label(home_frame, text="Latitude", bg=MAIN_COLOUR)
lat_label.place(rely=0.2, relwidth=0.48, relheight=0.3)
lat_label = tk.Label(home_frame, text="Longitude", bg=MAIN_COLOUR)
lat_label.place(rely=0.2, relx=0.52, relwidth=0.48, relheight=0.3)

lat_entry = tk.Entry(home_frame, font=40, bd=0)
lat_entry.place(rely=0.5, relwidth=0.48, relheight=0.5)
long_entry = tk.Entry(home_frame, font=40, bd=0)
long_entry.place(relx=0.52, rely=0.5, relwidth=0.48, relheight=0.5)

# INSIDE FILE FRAME
file_label = tk.Label(file_frame, text="File name for parkruns done", bg=MAIN_COLOUR)
file_label.place(relwidth=1, relheight=0.3)

file_entry = tk.Entry(file_frame, font=40, bd=0)
file_entry.place(rely=0.35, relwidth=1, relheight=0.65)

# INSIDE OPTIONS FRAME
options_label = tk.Label(options_frame, text="Things to show", bg=MAIN_COLOUR)
options_label.place(relwidth=1, relheight=0.3)

C_junior_int = tk.IntVar()
C_junior = tk.Checkbutton(options_frame, text="Junior parkruns", variable=C_junior_int, onvalue=1, offvalue=0,
                          bg=MAIN_COLOUR)
C_junior.place(rely=0.35)

C_alphabet_int = tk.IntVar()
C_alphabet = tk.Checkbutton(options_frame, text="alphabet challenge", variable=C_alphabet_int, onvalue=1, offvalue=0,
                            bg=MAIN_COLOUR)
C_alphabet.place(rely=0.35, relx=0.5)

# INSIDE RADIOBUTTON FRAME
options_label = tk.Label(radiobutton_frame, text="Choose display option", bg=MAIN_COLOUR)
options_label.place(relwidth=1, relheight=0.25)

show_var = tk.IntVar()
R1 = tk.Radiobutton(radiobutton_frame, text="all parkruns", variable=show_var, value=1, bg=MAIN_COLOUR)
R1.place(rely=0.3, relheight=0.2)

R2 = tk.Radiobutton(radiobutton_frame, text="parkruns done highlighted", variable=show_var, value=2, bg=MAIN_COLOUR)
R2.place(rely=0.5, relheight=0.2)

R3 = tk.Radiobutton(radiobutton_frame, text="only parkruns done", variable=show_var, value=3, bg=MAIN_COLOUR)
R3.place(rely=0.7, relheight=0.2)

R4 = tk.Radiobutton(radiobutton_frame, text="only junior parkruns", variable=show_var, value=4, bg=MAIN_COLOUR)
R4.place(rely=0.3, relx= 0.5, relheight=0.2)

# INSIDE GO BUTTON FRAME
button = tk.Button(button_frame, text="Go", font=40,
                   command=lambda: test_function([lat_entry.get(), long_entry.get()], file_entry.get(),
                                                 C_junior_int.get(), C_alphabet_int.get()))
button.place(relwidth=1, relheight=1)

root.mainloop()
