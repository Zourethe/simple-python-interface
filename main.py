'''
                                                    Simple Python Interface
    
    This is the main file of the script, the one that will load the main frame of
    the interface.

    Author: Zourethe
    Date: July, 17, 2023
'''

# Imports.
import tkinter
import tkinter.font

# Variables.
text = str('Press the button above')
root = tkinter.Tk()
frame = tkinter.Frame(root, height = 500, width = 500)
font = tkinter.font.Font(family = "Arial", size = 24)
button = tkinter.Button(root, text = "Press me", font = font, command = execute, fg = '#0000FF')
label = tkinter.Label(root, text = text, font = font, fg = '#FF0000')

# Execute method.
def execute():
    print("Output")

# Packs.
frame.pack()
button.pack(padx = 0, pady = 10, side = tkinter.TOP)
label.pack(padx = 0, pady = 0, side = tkinter.BOTTOM)

# Main loop start.
root.title('Interface')
root.mainloop()
