#import modules
import tkinter as tk
import customtkinter as ctk

#define functions
def switch_screen():
    print("temp")

#set up base
ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

start_window = ctk.CTk()
start_window.geometry("1920x1080")

frame = ctk.CTkFrame(master=start_window)
frame.pack(pady=20, padx=60, fill="both", expand=True)

start_window.title("Farming Simulator")

#Widget Configuration
play_button = ctk.CTkButton(master=start_window, text="Play",)
play_button.place(relx=.5, rely=.5, anchor=ctk.CENTER)

start_title = ctk.CTkLabel(master=start_window, text="Farming Simulator", fg_color="transparent")
start_title.place(relx=.5, rely=.1, anchor=ctk.CENTER)

#Set frames

#Run Program
start_window.mainloop()