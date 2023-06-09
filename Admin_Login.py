import tkinter as tk
from PIL import ImageTk, Image
from tkinter import messagebox
from tkcalendar import Calendar
from tkinter import ttk
import models
import dbhandler
import sqlite3

class AdminLogin(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.parent = master
        self.config(height=600, width=1000)
       
        background_image = Image.open("login.png")
        background_image = background_image.resize((1000, 600), Image.ANTIALIAS)
        self.background_photo = ImageTk.PhotoImage(background_image)
        background_label = tk.Label(self, image=self.background_photo)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)

        self.username_entry = tk.Entry(self, font=("Arial", 12))
        self.username_entry.place(x=620, y=220)

        self.password_entry = tk.Entry(self, show="*", font=("Arial", 12))
        self.password_entry.place(x=620, y=300)
        
        self.login_image = Image.open("LOG IN.png")
        self.login_image = self.login_image.resize((200, 100), Image.ANTIALIAS)
        self.login_photo = ImageTk.PhotoImage(self.login_image)
        self.login_button = tk.Button(self, image=self.login_photo, command=self.login, borderwidth=0)
        self.login_button.place(x=650, y=350)
        
        self.back_image = Image.open("BACK.png")
        self.back_image = self.back_image.resize((200, 100), Image.ANTIALIAS)
        self.back_photo = ImageTk.PhotoImage(self.back_image)
        self.back_button = tk.Button(self, image=self.back_photo, command=self.cancel, borderwidth=0)
        self.back_button.place(x=650, y=450, width=200)

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


    def open_admin_page(self):
        self.parent.withdraw() 
        admin_page_window = tk.Toplevel(self.parent)  
        admin_page = AdminPage(admin_page_window)  
        admin_page.pack() 

class AdminPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.parent = master
        self.config(height=500, width=1000)
        
        #Background Frame
        self.bg_frame = tk.Frame(self, bg='#1C305C', height=600, width=1000)
        self.bg_frame.place(x=0, y=0)

        #Frame for Patient Details
        self.patient_details_frame = tk.Frame(self.bg_frame, bg='#3BBA9C', height=250, width=400, border=2)
        self.patient_details_frame.place(x=5, y=5)

        #Inside of Patient Details
        self.patient_details_label = tk.Label(self.patient_details_frame, text='Patient Details', font=('Book Antiqua', 14, 'bold'), bg="#3BBA9C")
        self.patient_details_label.place(x=3, y=3)

        #Patient Informations
        self.patient_Name_label = tk.Label(self.patient_details_frame, text='Patient Name', font=('Book Antiqua', 12, 'bold'), bg="#3BBA9C")
        self.patient_Name_label.place(x=20, y=30)
        self.patient_Name_entry = tk.Entry(self.patient_details_frame, font=('Book Antiqua', 11, 'bold'), width=25)
        self.patient_Name_entry.place(x=160, y=30)

        self.gender_label = tk.Label(self.patient_details_frame, text='Gender', font=('Book Antiqua', 12, 'bold'), bg="#3BBA9C")
        self.gender_label.place(x=20, y=60)   
        self.gender_combobox = ttk.Combobox(self.patient_details_frame, values=["Male", "Female"], state='readonly')
        self.gender_combobox.set("Select Gender")
        self.gender_combobox.configure(width=31)
        self.gender_combobox.place(x=160, y=60)

        self.age_label = tk.Label(self.patient_details_frame, text='Age', font=('Book Antiqua', 12, 'bold'), bg="#3BBA9C")
        self.age_label.place(x=20, y=90)
        self.age_entry = tk.Entry(self.patient_details_frame, font=('Book Antiqua', 11, 'bold'), width=25)
        self.age_entry.place(x=160, y=90)

        self.contact_number_label = tk.Label(self.patient_details_frame, text='Contact Number', font=('Book Antiqua', 12, 'bold'), bg="#3BBA9C")
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

        self.password_label = tk.Label(self.patient_details_frame, text='Password', font=('Book Antiqua', 12, 'bold'), bg="#D7F6EF")
        self.password_label.place(x=20, y=208)      
        self.password_entry = tk.Entry(self.patient_details_frame, font=('Book Antiqua', 11, 'bold'), width=25)
        self.password_entry.place(x=160, y=208)
        
        self.bg_frame1 = tk.Frame(self, bg='#F6E8D7', height=250, width=570, border=2)
        self.bg_frame1.place(x=415, y=5)

        self.appoint_doctor_label = tk.Label(self.bg_frame1, text='Appoint Doctor', font=('Book Antiqua', 14, 'bold'), bg="#F6E8D7")
        self.appoint_doctor_label.place(x=3, y=3)

        self.doctor_label = tk.Label(self.bg_frame1, text='DOCTORS', font=('Book Antiqua', 12, 'bold'), bg="#F6E8D7")
        self.doctor_label.place(x=279, y=30)   
        self.doctor_combobox = ttk.Combobox(self.bg_frame1, values=["Dr. CHA - Cardiologist", "Dr. Kim - Pediatrician", "Dr. Jennie - Neurologist", "Dr. Rose - Dermatologist", "Dr. Victor - Generals Surgeon", "Dr. Lisa - Dentist"], state='readonly')
        self.doctor_combobox.set("Select Doctor")
        self.doctor_combobox.configure(width=30)
        self.doctor_combobox.place(x=300, y=60)

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

        self.specification_label = tk.Label(self.bg_frame1,  text='Diagnosis For: ', font=('Book Antiqua', 12, 'bold'), bg="#F6E8D7")
        self.specification_label.place(x=20, y=150)
        self.specification_entry = tk.Entry(self.bg_frame1, font=('Book Antiqua', 11, 'bold'), width=25)
        self.specification_entry.place(x=40, y=180)

        self.add_button = tk.Button(self.bg_frame1, text='Add', fg='black',bg="#D7F6EF", width=10, height=1, command=self.add_patient)
        self.add_button.place(x=380, y=213)

        self.clear_button_show = tk.Button(self.bg_frame1, text='Clear', fg='black',bg="#D7F6EF", width=10, height=1, command=self.clear_button)
        self.clear_button_show.place(x=480, y=213)


        self.bg_frame2 = tk.Frame(self.bg_frame, bg='#FF5757', height=230, width=979, border=2)
        self.bg_frame2.place(x=5, y=265)

        self.search_option = tk.StringVar()
        self.search_option.set("ID")

        self.search_combobox = ttk.Combobox(self.bg_frame2, textvariable=self.search_option,
                                            values=["ID", "Name"], width=10)
        self.search_combobox.place(x=800, y=12)

        self.search_button = tk.Button(self.bg_frame2, text='Search', fg='black', bg="#F6E8D7",
                                        width=10, height=1, command=self.search_patient)
        self.search_button.place(x=700, y=10)

        self.Search_Patient_label = tk.Label(self.bg_frame2,  text='Search Patient', font=('Book Antiqua', 15, 'bold'), bg="#FF5757")
        self.Search_Patient_label.place(x=20, y=10)
        self.search_Patient_entry = tk.Entry(self.bg_frame2, font=('Book Antiqua', 12, 'bold'), width=30)
        self.search_Patient_entry.place(x=160, y=12)



        self.edit_button = tk.Button(self.bg_frame2, text='Edit Information', fg='black',bg="#F6E8D7", width=15, height=2, command=edit_patient)
        self.edit_button.place(x= 425, y= 5)

        self.delete_button = tk.Button(self.bg_frame2, text='Delete', fg='black',bg="#F6E8D7", width=15, height=2, command=self.delete_patient)
        self.delete_button.place(x=560, y=5)


        style = ttk.Style()
        style.theme_use("clam")
        style.configure("Treeview", background='#f8ecd4', foreground='black', fieldbackground='#f8ecd4')
        style.configure("Treeview.Heading", background='#f8ecd4', foreground='black')
        style.map('Treeview', background=[('selected', '#ff5454')])

        self.tree = ttk.Treeview(self.bg_frame2, columns=[
            "id",
            "name",
            "gender",
            "age",
            "contact",
            "email",
            "address",
            "password",
            "symptoms",
            "specification",
            "doctor",
            "appointment_date",
            "appointment_time"
        ])

        self.tree.column("#0", width=0, stretch=tk.NO)
        column_widths = [30, 73, 73, 30, 73, 116, 73, 94, 73, 94, 73, 73, 73]
        for i, column in enumerate(self.tree["columns"]):
            self.tree.column(column, width=column_widths[i])
            self.tree.heading(column, text=column.capitalize())

        self.tree.place(x=10, y=50, height=170)

        self.update_table()

    def search_patient(self):
        search_text = self.search_Patient_entry.get().strip()
        search_option = self.search_option.get()

        # Perform search based on the selected option
        if search_option == "ID":
                self.tree.delete(*self.tree.get_children())  # Clear the existing table data

                db_conn = dbhandler.DBHandler()
                patients = db_conn.search_patients_by_id(search_text)
                db_conn.close()

                for patient in patients:
                        self.tree.insert("", "end", values=(patient.id, patient.name, patient.gender, patient.age,
                                                                patient.contact, patient.email, patient.address, patient.password,
                                                                patient.symptoms, patient.specification, patient.doctor,
                                                                patient.appointment_date, patient.appointment_time))
        elif search_option == "Name":
                self.tree.delete(*self.tree.get_children())  # Clear the existing table data

                db_conn = dbhandler.DBHandler()
                patients = db_conn.search_patients_by_name(search_text)
                db_conn.close()

                for patient in patients:
                        self.tree.insert("", "end", values=(patient.id, patient.name, patient.gender, patient.age,
                                                                patient.contact, patient.email, patient.address, patient.password,
                                                                patient.symptoms, patient.specification, patient.doctor,
                                                                patient.appointment_date, patient.appointment_time))

    def add_patient(self):
        if not self.validate():
            return
        
        new_patient = models.patient()
        new_patient.patient_name = self.patient_Name_entry.get()
        new_patient.gender = self.gender_combobox.get()
        new_patient.age = self.age_entry.get()     
        new_patient.contact_number = self.contact_number_entry.get()
        new_patient.email = self.email_entry.get()
        new_patient.address = self.address_entry.get()
        new_patient.password = self.password_entry.get()
        new_patient.symptoms = self.symptoms_entry.get()
        new_patient.specification = self.specification_entry.get()
        new_patient.doctor = self.doctor_combobox.get()
        new_patient.appointment_date = self.enter_date_entry.get()
        new_patient.appointment_time = self.enter_time_entry.get()

        db_conn = dbhandler.DBHandler()
        db_conn.create_patient(new_patient)
        db_conn.close() 

        self.update_table()
        self.deleteentry()

    def getpatient(self):
        dbconn = dbhandler.DBHandler()
        self.patient_list = dbconn.read_patient()
        dbconn.close()

    def update_table(self) :

        self.tree.delete(*self.tree.get_children())
        self.getpatient()
        
        for patient in self.patient_list:
            row= (patient.id, patient.patient_name, patient.gender, patient.age, patient.contact_number, patient.email, patient.address, patient.password, patient.symptoms, patient.specification, patient.doctor, patient.appointment_date, patient.appointment_time)
            self.tree.insert('',tk.END, values = row)

    

    def deleteentry(self):
         
         self.patient_Name_entry.delete(0,tk.END)
         self.gender_combobox.set("Select Gender")
         self.age_entry.delete(0,tk.END)
         self.contact_number_entry.delete(0,tk.END)
         self.email_entry.delete(0,tk.END)
         self.address_entry.delete(0,tk.END)
         self.password_entry.delete(0,tk.END)
         self.symptoms_entry.delete(0,tk.END)
         self.specification_entry.delete(0,tk.END)
         self.enter_date_entry.delete(0,tk.END)
         self.enter_time_entry.delete(0,tk.END)
         self.doctor_combobox.set("Select Doctor")
    
    def delete_patient(self):
        
        selections= self.tree.selection()

        if len(selections)==0:
            messagebox.showwarning("Invalid","please select a patient in the table")
            return
        
        proceed=messagebox.askyesno("ask","are you sure you want to delete this user?")

        if not proceed:
            return
        
        for selected_patient in selections:
            selected_patient=self.tree.item(selected_patient)['values'][0]
            dbconn=dbhandler.DBHandler()
            dbconn.delete_patient(selected_patient)
            dbconn.close()
            
            self.update_table()
         

    def validate(self):
      
                if not self.patient_Name_entry.get():
                        messagebox.showerror("Error", "All entry must contain value")
                        return False
                if not self.patient_Name_entry.get().isalpha():
                        messagebox.showerror("Invalid input", "Please enter letters and spaces only.")
                        return False      
        
                if not self.age_entry.get():
                        messagebox.showerror("Error", "All entry must contain value")
                        return False
                if not self.age_entry.get().isnumeric():
                        messagebox.showerror("Invalid input", "Please enter numbers only.")
                        return False
        
                if not self.gender_combobox.get():
                        messagebox.showerror("Error", "You Must Select One")
                        return False
                
                if not self.contact_number_entry.get():
                        messagebox.showerror("Error", "All entry must contain value")
                        return False
                if not self.contact_number_entry.get().isnumeric():
                        messagebox.showerror("Invalid input", "Please enter numbers only")
                        return False  
                
                if not self.email_entry.get():
                        messagebox.showerror("Error", "All entry must contain value")
                        return False 
                
                if not self.address_entry.get():
                        messagebox.showerror("Error", "All entry must contain value")
                        return False
        
                if not self.password_entry.get():
                        messagebox.showerror("Error", "All entry must contain value")
                        return False 
                
                if not self.symptoms_entry.get():
                        messagebox.showerror("Error", "All entry must contain value")
                        return False
                
                if not self.specification_entry.get():
                        messagebox.showerror("Error", "All entry must contain value")
                        return False
                if not self.specification_entry.get():
                        messagebox.showerror("Error", "Invalid input. Please enter a specification for diagnosis")
                        return False  
                
                if not self.doctor_combobox.get():
                        messagebox.showerror("Error", "You Must Select One")
                        return False
                
                if not self.enter_date_entry.get():
                        messagebox.showerror("Error", "You must enter a date")
                        return False
                
                if not self.enter_time_entry.get():
                        messagebox.showerror("Error", "You must enter a time")
                        return False
        
                return True

    def clear_button(self):
        result = messagebox.askyesno("Clear Entry", "Are you sure you want to clear the entry?")
        if result:
                self.deleteentry()
        else: 
              return
  


def edit_patient(self):
        if not self.validate():
            return

        selected_patient = self.tree.selection()
        if len(selected_patient) == 0:
            messagebox.showwarning("Invalid", "Please select a patient in the table")
            return

        selected_patient_id = self.tree.item(selected_patient)['values'][0]

        # Get the updated patient details from the input fields
        new_patient = models.Patient(
            id=selected_patient_id,
            patient_name=self.patient_name.get(),
            gender=self.gender.get(),
            age=self.age.get(),
            contact_number=self.contact_number.get(),
            email=self.email.get(),
            address=self.address.get(),
            password=self.password.get(),
            symptoms=self.symptoms.get(),
            specification=self.specification.get(),
            doctor=self.doctor.get(),
            appointment_date=self.appointment_date.get(),
            appointment_time=self.appointment_time.get()
        )

        db_conn = dbhandler.DBHandler()
        db_conn.edit_patient(new_patient)
        db_conn.close()

        self.update_table()

def update_table(self):
        # Clear the existing table data
        self.tree.delete(*self.tree.get_children())

        # Fetch the updated patient data from the database
        db_conn = dbhandler.DBHandler()
        patients = db_conn.get_all_patients()
        db_conn.close()

        # Populate the table with the updated patient data
        for patient in patients:
            self.tree.insert("", "end", values=(patient.id, patient.patient_name, patient.gender, patient.age,
                                                patient.contact_number, patient.email, patient.address, patient.password,
                                                patient.symptoms, patient.specification, patient.doctor,
                                                patient.appointment_date, patient.appointment_time))
