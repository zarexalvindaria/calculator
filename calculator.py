"""Calculator application"""
import tkinter as tk


root = tk.Tk()
root.title("Calculator")
root.geometry("300x400")
root.iconbitmap("calc.ico")
root.resizable(0,0)

# Define colors and fonts
dark_green = "#93af22"
light_green = "#acc253"
white_green = "#edefe0"
button_font = ("Arial", 18)
display_font = ("Arial", 30)



# Run the window's main loop
root.mainloop()