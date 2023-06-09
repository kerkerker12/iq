import tkinter as tk
import pages
import Admin_Login
import patient_login

class MainWindow(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.wm_title("Hospital Management System")

        self.frames = dict() 
        self.frames['Profile'] = pages.Profile_Selection(self) 
        self.frames['Admin'] =Admin_Login.AdminLogin(self) 
        self.frames['Patient'] = patient_login.PatientLogin(self) 
        self.change_window('Profile')
    def change_window(self, name):
        for frame in self.frames.values():
            frame.grid_forget()

        if name in self.frames:
            self.frames[name].grid()

root = MainWindow()
root.resizable(False, False)
root.mainloop()
