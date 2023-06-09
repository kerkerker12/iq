import tkinter as tk
from PIL import ImageTk, Image
from tkinter import messagebox
from tkcalendar import Calendar
from tkinter import ttk

class PatientLogin(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.parent = master
        self.config(height=450, width=1000)

        background_image = Image.open("patient login.png")
        background_image = background_image.resize((800, 500), Image.ANTIALIAS)
        self.background_photo = ImageTk.PhotoImage(background_image)
        background_label = tk.Label(self, image=self.background_photo)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)

        self.username_entry = tk.Entry(self, font=("Arial", 12))
        self.username_entry.place(x=218, y=293)

        self.password_entry = tk.Entry(self, show="*", font=("Arial", 12))
        self.password_entry.place(x=218, y=366)
        
        self.login_image = Image.open("LOG IN.png")
        self.login_image = self.login_image.resize((70, 70), Image.ANTIALIAS)
        self.login_photo = ImageTk.PhotoImage(self.login_image)
        self.login_button = tk.Button(self, image=self.login_photo, command=self.login, borderwidth=0)
        self.login_button.place(x=420, y=400)

    def login(self):
        if self.username_entry.get() == '' or self.password_entry.get() == '':
            messagebox.showerror("Login", "Some credentials are invalid. Please try again.")
        elif self.username_entry.get() == "1" and self.password_entry.get() == "1":
            messagebox.showinfo("Login", "Login successful!")
            self.open_admin_page()
        else:
            messagebox.showerror("Login", "Invalid username or password")

        self.back_image = Image.open("BACK.png")
        self.back_image = self.back_image.resize((70, 70), Image.ANTIALIAS)
        self.back_photo = ImageTk.PhotoImage(self.back_image)
        self.back_button = tk.Button(self, image=self.back_photo, command=self.cancel, borderwidth=0)
        self.back_button.place(x=278, y=400)

        self.register_image = Image.open("REGISTER.png")
        self.register_image = self.register_image.resize((70, 70), Image.ANTIALIAS)
        self.register_photo = ImageTk.PhotoImage(self.register_image)
        self.register_button = tk.Button(self, image=self.register_photo, command=self.register, borderwidth=0)
        self.register_button.place(x=350, y=400)



def login(self):
        if self.username_entry.get() == '' or self.password_entry.get() == '':
            messagebox.showerror("Login", "Some credentials are invalid. Please try again.")
        elif self.username_entry.get() == "1" and self.password_entry.get() == "1":
            messagebox.showinfo("Login", "Login successful!")
            self.open_admin_page()
        else:
            messagebox.showerror("Login", "Invalid username or password")

def cancel(self):
        self.parent.change_window('Profile')
            
         #Background Frame
        self.bg_frame = tk.Frame(self, bg='#99D6D2', height=300, width=1000)
        self.bg_frame.place(x=0, y=0)

        #Frame for Patient Details
        self.patient_details_frame = tk.Frame(self.bg_frame, bg='#D7F6EF', height=250, width=400, border=2)
        self.patient_details_frame.place(x=5, y=5)

            #Inside of Patient Details
        self.patient_details_label = tk.Label(self.patient_details_frame, text='Patient Details', font=('Book Antiqua', 14, 'bold'), bg="#D7F6EF")
        self.patient_details_label.place(x=3, y=3)

            #Patient Informations
        self.patient_Name_label = tk.Label(self.patient_details_frame, text='Patient Name', font=('Book Antiqua', 12, 'bold'), bg="#D7F6EF")
        self.patient_Name_label.place(x=20, y=30)
        self.patient_Name_entry = tk.Entry(self.patient_details_frame, font=('Book Antiqua', 11, 'bold'), width=25)
        self.patient_Name_entry.place(x=160, y=30)

        self.gender_label = tk.Label(self.patient_details_frame, text='Gender', font=('Book Antiqua', 12, 'bold'), bg="#D7F6EF")
        self.gender_label.place(x=20, y=60)
        self.gender_entry = tk.Entry(self.patient_details_frame, font=('Book Antiqua', 11, 'bold'), width=25)
        self.gender_entry.place(x=160, y=60)

        self.age_label = tk.Label(self.patient_details_frame, text='Age', font=('Book Antiqua', 12, 'bold'), bg="#D7F6EF")
        self.age_label.place(x=20, y=90)
        self.age_entry = tk.Entry(self.patient_details_frame, font=('Book Antiqua', 11, 'bold'), width=25)
        self.age_entry.place(x=160, y=90)

        self.contact_number_label = tk.Label(self.patient_details_frame, text='Contact Number', font=('Book Antiqua', 12, 'bold'), bg="#D7F6EF")
        self.contact_number_label.place(x=20, y=120)      
        self.contact_number_entry = tk.Entry(self.patient_details_frame, font=('Book Antiqua', 11, 'bold'), width=25)
        self.contact_number_entry.place(x=160, y=120)

        self.email_label = tk.Label(self.patient_details_frame, text='Email', font=('Book Antiqua', 12, 'bold'), bg="#D7F6EF")
        self.email_label.place(x=20, y=150)      
        self.email_entry = tk.Entry(self.patient_details_frame, font=('Book Antiqua', 11, 'bold'), width=25)
        self.email_entry.place(x=160, y=150)

        self.address_label = tk.Label(self.patient_details_frame, text='Address', font=('Book Antiqua', 12, 'bold'), bg="#D7F6EF")
        self.address_label.place(x=20, y=179)      
        self.address_entry = tk.Entry(self.patient_details_frame, font=('Book Antiqua', 11, 'bold'), width=25)
        self.address_entry.place(x=160, y=179)
            
        self.bg_frame1 = tk.Frame(self, bg='#F6E8D7', height=250, width=570, border=2)
        self.bg_frame1.place(x=415, y=5)

        self.appoint_doctor_label = tk.Label(self.bg_frame1, text='Appoint Doctor', font=('Book Antiqua', 14, 'bold'), bg="#F6E8D7")
        self.appoint_doctor_label.place(x=3, y=3)

        self.title_label = tk.Label(self.bg_frame1, text='DOCTORS', font=('Book Antiqua', 12, 'bold'), bg="#F6E8D7")
        self.title_label.place(x=279, y=30)   
        self.title_combobox = ttk.Combobox(self.bg_frame1, values=["Cardiologist", "Pediatrician", "Neurologist", "Dermatologist", "Surgeon", "Dentist"])
        self.title_combobox.place(x=300, y=60)
        self.symptoms_label = tk.Label(self.bg_frame1,  text='Symptoms', font=('Book Antiqua', 12, 'bold'), bg="#F6E8D7")
        self.symptoms_label.place(x=20, y=30)
        self.symptoms_entry = tk.Entry(self.bg_frame1,  text='Select Specializations', font=('Book Antiqua', 11, 'bold'), width=25)
        self.symptoms_entry.place(x=40, y=60)

        self.enter_date_label = tk.Label(self.bg_frame1,  text='Enter Date (DD/MM/YYYY)', font=('Book Antiqua', 12, 'bold'), bg="#F6E8D7")
        self.enter_date_label.place(x=20, y=90)
        self.enter_date_entry = tk.Entry(self.bg_frame1,  text='DATE', font=('Book Antiqua', 11, 'bold'), width=25)
        self.enter_date_entry.place(x=40, y=120)
        
        self.enter_time_label = tk.Label(self.bg_frame1,  text='Enter Time (HH:MM:SS)', font=('Book Antiqua', 12, 'bold'), bg="#F6E8D7")
        self.enter_time_label.place(x=279, y=90)
        self.enter_time_entry = tk.Entry(self.bg_frame1,  text='TIME', font=('Book Antiqua', 11, 'bold'), width=25)
        self.enter_time_entry.place(x=300, y=120)

        self.submit_button = tk.Button(self.bg_frame1, text='SUBMIT', fg='black',bg="#D7F6EF", width=15, height=2)
        self.submit_button.place(x=75, y=170)

        self.clear_button = tk.Button(self.bg_frame1, text='CLEAR', fg='black',bg="#D7F6EF", width=15, height=2)
        self.clear_button.place(x=225, y=170)

        self.back_button = tk.Button(self.bg_frame1, text='BACK', fg='black',bg="#D7F6EF", width=15, height=2, command=self.cancel)
        self.back_button.place(x=375, y=170)

def cancel(self):
        self.parent.change_window('Profile')


