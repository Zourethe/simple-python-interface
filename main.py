# Imports
import tkinter
import tkinter.font


# Variables
text = str('Press the button above')


# root definition
root = tkinter.Tk()
frame = tkinter.Frame(root, height = 500, width = 500)
frame.pack()


# Font definition
font = tkinter.font.Font(family = "Arial", size = 24)


# Action when the button is pressed
def execute():
    print("Output")


# Button definition
button = tkinter.Button(root, text = "Press me", font = font, command = execute, fg = '#0000FF')


# Label definition
label = tkinter.Label(root, text = text, font = font, fg = '#FF0000')


# Packs
button.pack(padx = 0, pady = 10, side = tkinter.TOP)
label.pack(padx = 0, pady = 0, side = tkinter.BOTTOM)


# Main loop start
root.title('Interface')
root.mainloop()