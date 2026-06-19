# ---------------- HOSPITAL MANAGEMENT SYSTEM ---------------- #

patients = {}
doctors = {}
appointments = {}
billings = {}

# ---------------- LOGIN SYSTEM ---------------- #

username = input("Enter Username : ")
password = input("Enter Password : ")

if username == "admin" and password == "1234":

    print("\nLogin Successful...!")

    while True:

        print("\n" + "-" * 40)

        print("""
        1. Patient Registration
        2. View Patients
        3. Doctor Registration
        4. View Doctors
        5. Book Appointment
        6. Billing
        7. Search Patient
        8. Update Patient
        9. Delete Patient
        10. Exit
        """)

        choice = int(input("Enter Choice : "))

        # ---------------- PATIENT REGISTRATION ---------------- #

        if choice == 1:

            n = int(input("How many patients : "))

            for i in range(n):

                p_id = int(input("\nEnter Patient ID : "))
                name = input("Enter Name : ")
                age = int(input("Enter Age : "))
                gender = input("Enter Gender : ")
                disease = input("Enter Disease : ")

                patients[p_id] = {
                    "name": name,
                    "age": age,
                    "gender": gender,
                    "disease": disease
                }

            print("\nPatient Added Successfully")

        # ---------------- VIEW PATIENTS ---------------- #

        elif choice == 2:

            if patients:

                print("\nPATIENT DETAILS\n")

                for i in patients:

                    print("Patient ID :", i)
                    print("Name :", patients[i]["name"])
                    print("Age :", patients[i]["age"])
                    print("Gender :", patients[i]["gender"])
                    print("Disease :", patients[i]["disease"])
                    print("-" * 30)

            else:
                print("No Patients Available")

        # ---------------- DOCTOR REGISTRATION ---------------- #

        elif choice == 3:

            n = int(input("How many doctors : "))

            for i in range(n):

                d_id = int(input("\nEnter Doctor ID : "))
                name = input("Enter Doctor Name : ")
                specialist = input("Enter Specialization : ")
                fee = int(input("Enter Consultation Fee : "))

                doctors[d_id] = {
                    "name": name,
                    "specialist": specialist,
                    "fee": fee
                }

            print("\nDoctor Added Successfully")

        # ---------------- VIEW DOCTORS ---------------- #

        elif choice == 4:

            if doctors:

                print("\nDOCTOR DETAILS\n")

                for i in doctors:

                    print("Doctor ID :", i)
                    print("Doctor Name :", doctors[i]["name"])
                    print("Specialist :", doctors[i]["specialist"])
                    print("Fee :", doctors[i]["fee"])
                    print("-" * 30)

            else:
                print("No Doctors Available")

        # ---------------- APPOINTMENT BOOKING ---------------- #

        elif choice == 5:

            p_id = int(input("Enter Patient ID : "))
            d_id = int(input("Enter Doctor ID : "))
            time = input("Enter Appointment Time : ")

            if p_id in patients and d_id in doctors:

                appointments[p_id] = {
                    "patient_name": patients[p_id]["name"],
                    "doctor_name": doctors[d_id]["name"],
                    "time": time
                }

                print("\nAppointment Booked Successfully")

            else:
                print("Invalid Patient ID or Doctor ID")

        # ---------------- BILLING ---------------- #

        elif choice == 6:

            p_id = int(input("Enter Patient ID : "))

            if p_id in appointments:

                medicine_fee = int(input("Enter Medicine Fee : "))

                doctor_name = appointments[p_id]["doctor_name"]

                doctor_fee = 0

                for i in doctors:

                    if doctors[i]["name"] == doctor_name:
                        doctor_fee = doctors[i]["fee"]

                total = doctor_fee + medicine_fee

                billings[p_id] = {
                    "doctor_fee": doctor_fee,
                    "medicine_fee": medicine_fee,
                    "total": total
                }

                print("\n------ BILL ------")
                print("Patient Name :", appointments[p_id]["patient_name"])
                print("Doctor Fee :", doctor_fee)
                print("Medicine Fee :", medicine_fee)
                print("Total Bill :", total)

            else:
                print("Appointment Not Found")

        # ---------------- SEARCH PATIENT ---------------- #

        elif choice == 7:

            search = int(input("Enter Patient ID : "))

            if search in patients:

                print("\nPatient Found")
                print(patients[search])

            else:
                print("Patient Not Found")

        # ---------------- UPDATE PATIENT ---------------- #

        elif choice == 8:

            update_id = int(input("Enter Patient ID : "))

            if update_id in patients:

                new_name = input("Enter New Name : ")
                new_age = int(input("Enter New Age : "))
                new_disease = input("Enter New Disease : ")

                patients[update_id]["name"] = new_name
                patients[update_id]["age"] = new_age
                patients[update_id]["disease"] = new_disease

                print("Patient Updated Successfully")

            else:
                print("Patient Not Found")

        # ---------------- DELETE PATIENT ---------------- #

        elif choice == 9:

            delete_id = int(input("Enter Patient ID : "))

            if delete_id in patients:

                del patients[delete_id]

                print("Patient Deleted Successfully")

            else:
                print("Patient Not Found")

        # ---------------- EXIT ---------------- #

        elif choice == 10:

            print("Thank You")
            break

        else:
            print("Invalid Choice")

else:
    print("Invalid Username or Password")
