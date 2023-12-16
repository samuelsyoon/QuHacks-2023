import tkinter as tk
import customtkinter as ctk

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

base = ctk.CTk()
base.geometry("760x900")

frame = ctk.CTkFrame(master=base)
frame.pack(pady=20, padx=60, fill="both", expand=True)

base.mainloop()