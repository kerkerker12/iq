import tkinter as tk

class AdminWindow(tk.Toplevel):
    def __init__(self):
        tk.Toplevel.__init__(self)
        self.geometry('700x500')
        self.title("Admin Window")
        # Add widgets and configurations for the Admin window
