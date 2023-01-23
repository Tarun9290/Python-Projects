# import relevant libraries
import tkinter as tk

# create a window and set title
window = tk.Tk() 
window.title("Tic-Tac-Toe") 

# create the buttons 
button1 = tk.Button(window, text="   ") 
button1.grid(row=1, column=0, sticky="snew", ipadx=40, ipady=40) 

button2 = tk.Button(window, text="   ") 
button2.grid(row=1, column=1, sticky="snew", ipadx=40, ipady=40) 

button3 = tk.Button(window, text="   ") 
button3.grid(row=1, column=2, sticky="snew", ipadx=40, ipady=40) 

button4 = tk.Button(window, text="   ") 
button4.grid(row=2, column=0, sticky="snew", ipadx=40, ipady=40) 

button5 = tk.Button(window, text="   ") 
button5.grid(row=2, column=1, sticky="snew", ipadx=40, ipady=40) 

button6 = tk.Button(window, text="   ") 
button6.grid(row=2, column=2, sticky="snew", ipadx=40, ipady=40) 

button7 = tk.Button(window, text="   ") 
button7.grid(row=3, column=0, sticky="snew", ipadx=40, ipady=40) 

button8 = tk.Button(window, text="   ") 
button8.grid(row=3, column=1, sticky="snew", ipadx=40, ipady=40) 

button9 = tk.Button(window, text="   ") 
button9.grid(row=3, column=2, sticky="snew", ipadx=40, ipady=40) 

# setting up the players 
player = 1 

# game logic 
def buttonclick(buttons): 
	global player 
	if buttons["text"] == "   " and player == 1: 
		buttons["text"] = " X "
		player = 2
	elif buttons["text"] == "   " and player == 2: 
		buttons["text"] = " O "
		player = 1
	check_if_win() 

# check for win function 
def check_if_win(): 
	if (button1['text'] == 'X' and button2['text'] == 'X' and button3['text'] == 'X' or
		button4['text'] == 'X' and button5['text'] == 'X' and button6['text'] == 'X' or
		button7['text'] == 'X' and button8['text'] == 'X' and button9['text'] == 'X' or
		button1['text'] == 'X' and button4['text'] == 'X' and button7['text'] == 'X' or
		button2['text'] == 'X' and button5['text'] == 'X' and button8['text'] == 'X' or
		button3['text'] == 'X' and button6['text'] == 'X' and button9['text'] == 'X' or
		button1['text'] == 'X' and button5['text'] == 'X' and button9['text'] == 'X' or
		button3['text'] == 'X' and button5['text'] == 'X' and button7['text'] == 'X'): 
				
		# player X wins
		window.destroy()
		result_window = tk.Tk() 
		result_window.title("Result") 
		result_label = tk.Label(result_window, text="Player X wins!") 
		result_label.pack()
		exit_button = tk.Button(result_window, text="Exit", command=result_window.destroy) 
		exit_button.pack() 
		
	elif (button1['text'] == 'O' and button2['text'] == 'O' and button3['text'] == 'O' or
		button4['text'] == 'O' and button5['text'] == 'O' and button6['text'] == 'O' or
		button7['text'] == 'O' and button8['text'] == 'O' and button9['text'] == 'O' or
		button1['text'] == 'O' and button4['text'] == 'O' and button7['text'] == 'O' or
		button2['text'] == 'O' and button5['text'] == 'O' and button8['text'] == 'O' or
		button3['text'] == 'O' and button6['text'] == 'O' and button9['text'] == 'O' or
		button1['text'] == 'O' and button5['text'] == 'O' and button9['text'] == 'O' or
		button3['text'] == 'O' and button5['text'] == 'O' and button7['text'] == 'O'): 
			
		# player O wins
		window.destroy()
		result_window = tk.Tk() 
		result_window.title("Result") 
		result_label = tk.Label(result_window, text="Player O wins!") 
		result_label.pack()
		exit_button = tk.Button(result_window, text="Exit", command=result_window.destroy) 
		exit_button.pack() 

# adding command to the buttons 
button1.configure(command=lambda: buttonclick(button1)) 
button2.configure(command=lambda: buttonclick(button2)) 
button3.configure(command=lambda: buttonclick(button3)) 
button4.configure(command=lambda: buttonclick(button4)) 
button5.configure(command=lambda: buttonclick(button5)) 
button6.configure(command=lambda: buttonclick(button6)) 
button7.configure(command=lambda: buttonclick(button7)) 
button8.configure(command=lambda: buttonclick(button8)) 
button9.configure(command=lambda: buttonclick(button9)) 

# running the window 
window.mainloop()