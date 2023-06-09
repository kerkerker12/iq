import tkinter as tk

class PatientWindow(tk.Toplevel):
    def __init__(self):
        tk.Toplevel.__init__(self)
        self.geometry('700x500')
        self.title("Patient Window")
        # Add widgets and configurations for the Patient window
