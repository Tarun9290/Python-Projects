#ON-SCREEN KEYBOARD CODE IN PYTHON

import tkinter as tk

# create a tkinter window
window = tk.Tk()
window.title("On-Screen Keyboard")

# create a label to display key presses
label = tk.Label(window, text="")
label.pack()

# create buttons for each key
keys = [['1', '2', '3', '4', '5', '6', '7', '8', '9', '0'],
        ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p'],
        ['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', ';'],
        ['z', 'x', 'c', 'v', 'b', 'n', 'm', ',', '.', '/']]

# function to handle key presses
def key_press(key):
    current = label.cget("text")
    label.configure(text=current + key)

# create and add buttons to the window
for row in keys:
    key_frame = tk.Frame(window)
    key_frame.pack(side=tk.TOP)
    for key in row:
        key_button = tk.Button(key_frame, text=key, width=4, height=2, command=lambda key=key: key_press(key))
        key_button.pack(side=tk.LEFT)

# run the tkinter event loop
window.mainloop()
