import sqlite3
import models

class DBHandler:
    def __init__(self):
        self.db_name = 'database.db'
        self.patient_table = 'Patient_table'

        self.conn = sqlite3.connect(self.db_name)
        self.cursor = self.conn.cursor()

    def create_tables(self):

        self.cursor.execute(f"CREATE TABLE IF NOT EXISTS {self.patient_table} (id INTEGER PRIMARY KEY, name TEXT, gender TEXT, age INT, contact TEXT, email TEXT, address TEXT, password TEXT, symptoms TEXT, specification TEXT, doctor TEXT, appointment_date INT, appointment_time TEXT )")
    
        self.conn.commit()
        print("Database and tables created successfully.")

    def create_patient(self, patient: models.patient):

        insert_query = f"INSERT INTO {self.patient_table}(name, gender, age, contact, email, address, password, symptoms, specification, doctor, appointment_date, appointment_time) VALUES (?,?,?,?,?,?,?,?,?,?,?,?)"
        insert_values = (patient.patient_name, patient.gender, patient.age, patient.contact_number, patient.email, patient.address, patient.password, patient.symptoms, patient.specification, patient.doctor, patient.appointment_date, patient.appointment_time )
        self.cursor.execute(insert_query, insert_values)
        self.conn.commit()

    def delete_patient(self, id:int):
        query=f"DELETE FROM {self.patient_table} WHERE id =?"
        values=(id,)
        self.cursor.execute(query,values)
        self.conn.commit()
        
    def edit_patient(self, id:int):
        query=f"EDIT FROM {self.patient_table} WHERE id=?"
        values=(id,)
        self.cursor.execute(query,values)
        self.conn.commit()

    def read_patient(self):
        query = f"SELECT id, name, gender, age, contact, email, address, password, symptoms, specification, doctor, appointment_date, appointment_time FROM {self.patient_table}"
        self.cursor.execute(query)

        patients = []

        for row in self.cursor:
            new_patient = models.patient()
            new_patient.id = row[0]
            new_patient.patient_name = row[1]
            new_patient.gender = row[2]
            new_patient.age = row[3]
            new_patient.contact_number = row[4]
            new_patient.email = row[5]
            new_patient.address = row[6]
            new_patient.password = row[7]
            new_patient.symptoms = row[8]
            new_patient.specification = row[9]
            new_patient.doctor = row[10]
            new_patient.appointment_date = row[11]
            new_patient.appointment_time = row[12]
            patients.append(new_patient)

        return patients

    def close(self):
        self.conn.close()


# handler = DBHandler()
# handler.create_tables() 
