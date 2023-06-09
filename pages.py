import tkinter as tk
from PIL import ImageTk, Image

class Profile_Selection(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.parent = master
        self.config(height=800, width=1000)
        
        background_image = Image.open("background.png")
        background_image = background_image.resize((1000, 800), Image.ANTIALIAS)
        self.background_photo = ImageTk.PhotoImage(background_image)
        background_label = tk.Label(self, image=self.background_photo)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)

        # admin button
        self.profile_icon = Image.open("adminlog.png")
        self.resize_picon = self.profile_icon.resize((250, 250))
        self.profile_icon = ImageTk.PhotoImage(self.resize_picon)
        self.admin_button = tk.Button(self, image=self.profile_icon, command=self.go_to_Admin_login)
        self.admin_button.grid(row=0, column=0, sticky='w', padx= 130, pady=200)
        self.admin_label = tk.Label(self, text="Admin", font="Garamond 25")
        self.admin_label.place(x=210, y=480)

        # patient button
        self.profile_icon3 = Image.open("patientlog.png")
        self.resize_picon3 = self.profile_icon3.resize((250, 250))
        self.profile_icon3 = ImageTk.PhotoImage(self.resize_picon3)
        self.patient_button = tk.Button(self, image=self.profile_icon3, command=self.go_to_patient_login)
        self.patient_button.grid(row=0, column=4, padx=130, pady=200)
        self.admin_label = tk.Label(self, text="Patient", font="Garamond 25")
        self.admin_label.place(x=740, y=480)

    def go_to_Admin_login(self):
        self.parent.change_window('Admin')

    def go_to_patient_login(self):
        self.parent.change_window('Patient')
