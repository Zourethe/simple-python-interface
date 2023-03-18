# Imports
import tkinter
import tkinter.font


# Frame definition
frame = tkinter.Tk()


# Font definition
font = tkinter.font.Font(family = "Arial")


# Action when the button is pressed
def execute():
    print("Output")


# Button definition
button = tkinter.Button(frame, text = "Test", font = font, command = execute)


# Packs
button.pack(padx = 0, pady = 10, side = tkinter.TOP)


# Main loop start
frame.mainloop()