from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
import mysql.connector
from tkinter import messagebox

from mysql.connector.errors import DatabaseError


class Criminal:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x800+0+0")
        self.root.title("CRIMINAL MANAGEMENT SYSTEM")

        # Variables

        self.var_case_id = StringVar()
        self.var_criminal_no = StringVar()
        self.var_name = StringVar()
        self.var_nickname = StringVar()
        self.var_father_name = StringVar()
        self.var_arrest_date = StringVar()
        self.var_date_of_crime = StringVar()
        self.var_address = StringVar()
        self.var_age = StringVar()
        self.var_occupation = StringVar()
        self.var_birthMark = StringVar()
        self.var_crime_type = StringVar()
        self.var_gender = StringVar()
        self.var_wanted = StringVar()
        self.var_total_amount = StringVar()

        lbltitle = Label(self.root, text="CRIMINAL MANAGEMENT SYSTEM", bd=8, relief=RIDGE,
                         bg="black", fg="white", font=("times new roman", 50, "bold"), padx=2, pady=-2)
        lbltitle.pack(side=TOP, fill=X)

        # police logo Image

        img_logo = Image.open("images\logo1.jpg")
        img_logo = img_logo.resize((60, 60), Image.ANTIALIAS)
        self.photo_logo = ImageTk.PhotoImage(img_logo)
        self.logo = Label(self.root, image=self.photo_logo)
        self.logo.place(x=100, y=15, width=60, height=60)

        # Image Frame

        img_frame = Frame(self.root, bd=2, relief=RIDGE, bg="black")
        img_frame.place(x=2.5, y=100, width=1530, height=135)

        # Images

        img1 = Image.open("images\police2.jpg")
        img1 = img1.resize((500, 150), Image.ANTIALIAS)
        self.photo1 = ImageTk.PhotoImage(img1)

        self.img_1 = Label(img_frame, image=self.photo1)
        self.img_1.place(x=12, y=0, width=490, height=130)

        img2 = Image.open("images\police3.jpg")
        img2 = img2.resize((500, 150), Image.ANTIALIAS)
        self.photo2 = ImageTk.PhotoImage(img2)

        self.img_2 = Label(img_frame, image=self.photo2)
        self.img_2.place(x=517, y=0, width=490, height=130)

        img3 = Image.open("images\police4.jpg")
        img3 = img3.resize((500, 150), Image.ANTIALIAS)
        self.photo3 = ImageTk.PhotoImage(img3)

        self.img_3 = Label(img_frame, image=self.photo3)
        self.img_3.place(x=1024, y=0, width=490, height=130)

        # Main Frame

        Main_frame = Frame(self.root, bd=2, relief=RIDGE, bg="white")
        Main_frame.place(x=10, y=243, width=1515, height=545)

        # Upper Frame
        upper_frame = LabelFrame(Main_frame, bd=2, relief=RIDGE, text="Criminal Information", font=(
            "times new roman", 12, "bold"), fg="darkgreen", bg="white")
        upper_frame.place(x=10, y=5, width=1490, height=265)

        #Labels & Entry

        # Case ID

        caseid = Label(upper_frame, text="Case ID:", font=(
            "times new roman", 12, "bold"), bg="white")
        caseid.grid(row=0, column=0, padx=2, sticky=W)

        caseentry = ttk.Entry(upper_frame, textvariable=self.var_case_id, width=25, font=(
            "times new roman", 12, "bold"))
        caseentry.grid(row=0, column=1, padx=2, sticky=W)

        # Criminal NO

        lbl_criminal_no = Label(upper_frame, text="Criminal NO:", font=(
            "times new roman", 12, "bold"), bg="white")
        lbl_criminal_no.grid(row=0, column=2, sticky=W, padx=2, pady=7)

        txt_criminal_no = ttk.Entry(upper_frame, textvariable=self.var_criminal_no, width=25, font=(
            "times new roman", 12, "bold"))
        txt_criminal_no.grid(row=0, column=3, sticky=W, padx=2, pady=7)

        # Criminal Name

        lbl_Name = Label(upper_frame, text="Criminal Name:", font=(
            "times new roman", 12, "bold"), bg="white")
        lbl_Name.grid(row=1, column=0, sticky=W, padx=2, pady=7)

        txt_Name = ttk.Entry(upper_frame, textvariable=self.var_name, width=25, font=(
            "times new roman", 12, "bold"))
        txt_Name.grid(row=1, column=1, sticky=W, padx=2, pady=7)

        # Criminal Nickname

        lbl_nickname = Label(upper_frame, text="Criminal Nickname:", font=(
            "times new roman", 12, "bold"), bg="white")
        lbl_nickname.grid(row=1, column=2, sticky=W, padx=2, pady=7)

        txt_nickname = ttk.Entry(upper_frame, textvariable=self.var_nickname, width=25, font=(
            "times new roman", 12, "bold"))
        txt_nickname.grid(row=1, column=3, padx=2, pady=7)

        # Father Name

        lbl_fathername = Label(upper_frame, text="Criminal Father Name:", font=(
            "times new roman", 12, "bold"), bg="white")
        lbl_fathername.grid(row=2, column=0, sticky=W, padx=2, pady=7)

        txt_fathername = ttk.Entry(upper_frame, textvariable=self.var_father_name, width=25, font=(
            "times new roman", 12, "bold"))
        txt_fathername.grid(row=2, column=1, padx=2, pady=7)

        # Arrest Date

        lbl_arrestdate = Label(upper_frame, text="Arrest Date:", font=(
            "times new roman", 12, "bold"), bg="white")
        lbl_arrestdate.grid(row=2, column=2, sticky=W, padx=2, pady=7)

        txt_nickname = ttk.Entry(upper_frame, textvariable=self.var_arrest_date, width=25, font=(
            "times new roman", 12, "bold"))
        txt_nickname.grid(row=2, column=3, padx=2, pady=7)

        # Crime Date

        lbl_dateofcrime = Label(upper_frame, text="Date of Crime:", font=(
            "times new roman", 12, "bold"), bg="white")
        lbl_dateofcrime.grid(row=3, column=0, sticky=W, padx=2, pady=7)

        txt_dateofcrime = ttk.Entry(upper_frame, textvariable=self.var_date_of_crime, width=25, font=(
            "times new roman", 12, "bold"))
        txt_dateofcrime.grid(row=3, column=1, sticky=W, padx=2, pady=7)

        # Address

        lbl_address = Label(upper_frame, text="Address:", font=(
            "times new roman", 12, "bold"), bg="white")
        lbl_address.grid(row=3, column=2, sticky=W, padx=2, pady=7)

        txt_address = ttk.Entry(upper_frame, textvariable=self.var_address, width=25, font=(
            "times new roman", 12, "bold"))
        txt_address.grid(row=3, column=3, padx=2, pady=7)

        # Age

        lbl_age = Label(upper_frame, text="Age:", font=(
            "times new roman", 12, "bold"), bg="white")
        lbl_age.grid(row=4, column=0, sticky=W, padx=2, pady=7)

        txt_age = ttk.Entry(upper_frame, textvariable=self.var_age,
                            width=25, font=("times new roman", 12, "bold"))
        txt_age.grid(row=4, column=1, padx=2, pady=7)

        # Occupation

        lbl_occupation = Label(upper_frame, text="Occupation:", font=(
            "times new roman", 12, "bold"), bg="white")
        lbl_occupation.grid(row=4, column=2, sticky=W, padx=2, pady=7)

        txt_occupation = ttk.Entry(upper_frame, textvariable=self.var_occupation, width=25, font=(
            "times new roman", 12, "bold"))
        txt_occupation.grid(row=4, column=3, padx=2, pady=7)

        # BirthMark

        lbl_birthmark = Label(upper_frame, text="Birth Mark:", font=(
            "times new roman", 12, "bold"), bg="white")
        lbl_birthmark.grid(row=0, column=4, sticky=W, padx=2, pady=7)

        txt_birthmark = ttk.Entry(upper_frame, textvariable=self.var_birthMark, width=25, font=(
            "times new roman", 12, "bold"))
        txt_birthmark.grid(row=0, column=5, sticky=W, padx=2, pady=7)

        # Crime Type

        lbl_crimetype = Label(upper_frame, text="Crime Type:", font=(
            "times new roman", 12, "bold"), bg="white")
        lbl_crimetype.grid(row=1, column=4, sticky=W, padx=2, pady=7)

        txt_crimetype = ttk.Entry(upper_frame, textvariable=self.var_crime_type, width=25, font=(
            "times new roman", 12, "bold"))
        txt_crimetype.grid(row=1, column=5, padx=2, pady=7)

        # Gender

        lbl_gender = Label(upper_frame, text="Gender:", font=(
            "times new roman", 12, "bold"), bg="white")
        lbl_gender.grid(row=2, column=4, sticky=W, padx=2, pady=7)

        # Wanted

        lbl_wanted = Label(upper_frame, text="Most Wanted:", font=(
            "times new roman", 12, "bold"), bg="white")
        lbl_wanted.grid(row=3, column=4, sticky=W, padx=2, pady=7)

        # Total amount of income

        lbl_total_amount = Label(upper_frame, text="Total Income:", font=(
            "times new roman", 12, "bold"), bg="white")
        lbl_total_amount.grid(row=4, column=4, sticky=W, padx=2, pady=7)

        txt_total_amount = ttk.Entry(upper_frame, textvariable=self.var_total_amount, width=25, font=(
            "times new roman", 12, "bold"))
        txt_total_amount.grid(row=4, column=5, sticky=W, padx=2, pady=7)

        # Radio Button For Gender

        radio_frame_gender = Frame(upper_frame, bd=2, relief=RIDGE, bg="white")
        radio_frame_gender.place(x=845, y=80, width=150, height=30)

        male = Radiobutton(radio_frame_gender, variable=self.var_gender, text="Male",
                           value="male", font=("times new roman", 9, "bold"), bg="white")
        male.grid(row=0, column=0, pady=2, padx=5, sticky=W)

        famale = Radiobutton(radio_frame_gender, variable=self.var_gender, text="Famale",
                             value="famale", font=("times new roman", 9, "bold"), bg="white")
        famale.grid(row=0, column=1, pady=2, padx=5, sticky=W)

        # Radio Button For wanted

        radio_frame_wanted = Frame(upper_frame, bd=2, relief=RIDGE, bg="white")
        radio_frame_wanted.place(x=845, y=120, width=140, height=30)

        yes = Radiobutton(radio_frame_wanted, variable=self.var_wanted, text="Yes",
                          value="yes", font=("times new roman", 9, "bold"), bg="white")
        yes.grid(row=0, column=0, pady=2, padx=5, sticky=W)

        no = Radiobutton(radio_frame_wanted, variable=self.var_wanted, text="No",
                         value="no", font=("times new roman", 9, "bold"), bg="white")
        no.grid(row=0, column=1, pady=2, padx=5, sticky=W)

        # Buttons

        button_frame = Frame(upper_frame, bd=2, relief=RIDGE, bg="white")
        button_frame.place(x=10, y=195, width=580, height=41)

        # Record Add Button

        btn_add = Button(button_frame, command=self.add_data, text="Record Save", font=(
            "times new roman", 13, "bold"), width=13, bg="green", fg="white")
        btn_add.grid(row=0, column=0, padx=2, pady=2)

        # Update Button

        btn_update = Button(button_frame, command=self.update_data, text="Update", font=(
            "times new roman", 13, "bold"), width=13, bg="purple", fg="white")
        btn_update.grid(row=0, column=1, padx=2, pady=2)

        # Delete Button

        btn_delete = Button(button_frame, command=self.delete_data, text="Delete", font=(
            "times new roman", 13, "bold"), width=13, bg="red", fg="white")
        btn_delete.grid(row=0, column=2, padx=2, pady=2)

        # Clear Button

        btn_clear = Button(button_frame, command=self.clear_data, text="Clear", font=(
            "times new roman", 13, "bold"), width=13, bg="orange", fg="white")
        btn_clear.grid(row=0, column=3, padx=2, pady=2)

        # Background right side image

        img_crime = Image.open("images\control0.jpg")
        img_crime = img_crime.resize((500, 232), Image.ANTIALIAS)
        self.photocrime = ImageTk.PhotoImage(img_crime)

        self.img_crime = Label(upper_frame, image=self.photocrime)
        self.img_crime.place(x=1085, y=0, width=390, height=232)

        # Down Frame
        down_frame = LabelFrame(Main_frame, bd=2, relief=RIDGE, text="Criminal Information Table", font=(
            "times new roman", 12, "bold"), fg="darkgreen", bg="white")
        down_frame.place(x=10, y=275, width=1490, height=255)

        # Search Frame
        search_frame = LabelFrame(down_frame, bd=2, relief=RIDGE, text="Search Criminal Record", font=(
            "times new roman", 12, "bold"), fg="darkgreen", bg="white")
        search_frame.place(x=10, y=0, width=1465, height=62)

        # Search Label

        search_by = Label(search_frame, text="Search By", font=(
            "times new roman", 12, "bold"), width=12, bg="navyblue", fg="white")
        search_by.grid(row=0, column=0, sticky=W, padx=5)

        # ComboBox
        self.var_com_search = StringVar()
        combo_search_box = ttk.Combobox(search_frame, textvariable=self.var_com_search, font=(
            "times new roman", 12, "bold"), width=15, state="readonly")
        combo_search_box["value"] = ("Select Option", "Case_ID", "Criminal_NO")
        combo_search_box.current(0)
        combo_search_box.grid(row=0, column=1, sticky=W, padx=5)

        self.var_search = StringVar()
        search_txt = ttk.Entry(search_frame, textvariable=self.var_search, width=20, font=(
            "times new roman", 12, "bold"))
        search_txt.grid(row=0, column=2, padx=5)

        # Search Button

        btn_search = Button(search_frame, command=self.search_data, text="Search", font=(
            "times new roman", 13, "bold"), width=15, bg="darkgreen", fg="white")
        btn_search.grid(row=0, column=3, padx=5)

        # Show_All Button

        btn_show = Button(search_frame, command=self.fetch_data, text="Show All", font=(
            "times new roman", 13, "bold"), width=15, bg="skyblue", fg="white")
        btn_show.grid(row=0, column=4, padx=5)

        # Label __ Crime Agency

        crimeagency = Label(search_frame, text="National Crime Agency", font=(
            "times new roman", 21, "bold"), bg="white", fg="crimson")
        crimeagency.grid(row=0, column=5, sticky=W, padx=150)

        # Table Frame

        table_frame = Frame(down_frame, bd=5, relief=RIDGE)
        table_frame.place(x=8, y=65, width=1467, height=160)

        # Scrollbar

        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.criminal_table = ttk.Treeview(table_frame, column=("1", "2", "3", "4", "5", "6", "7", "8",
                                           "9", "10", "11", "12", "13", "14", "15"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.criminal_table.xview)
        scroll_y.config(command=self.criminal_table.yview)

        self.criminal_table.heading("1", text="Case_ID")
        self.criminal_table.heading("2", text="Criminal_NO")
        self.criminal_table.heading("3", text="Criminal_Name")
        self.criminal_table.heading("4", text="Criminal_Nickname")
        self.criminal_table.heading("5", text="Criminal_Father_Name")
        self.criminal_table.heading("6", text="Arrest_Date")
        self.criminal_table.heading("7", text="Date_of_Crime")
        self.criminal_table.heading("8", text="Address")
        self.criminal_table.heading("9", text="Age")
        self.criminal_table.heading("10", text="Occupation")
        self.criminal_table.heading("11", text="Birth_Mark")
        self.criminal_table.heading("12", text="Crime_Type")
        self.criminal_table.heading("13", text="Gender")
        self.criminal_table.heading("14", text="Wanted")
        self.criminal_table.heading("15", text="Total_Income")

        self.criminal_table["show"] = "headings"
        # Widths
        self.criminal_table.column("1", width=130)
        self.criminal_table.column("2", width=130)
        self.criminal_table.column("3", width=130)
        self.criminal_table.column("4", width=130)
        self.criminal_table.column("5", width=130)
        self.criminal_table.column("6", width=130)
        self.criminal_table.column("7", width=130)
        self.criminal_table.column("8", width=130)
        self.criminal_table.column("9", width=130)
        self.criminal_table.column("10", width=130)
        self.criminal_table.column("11", width=130)
        self.criminal_table.column("12", width=130)
        self.criminal_table.column("13", width=130)
        self.criminal_table.column("14", width=130)
        self.criminal_table.column("15", width=130)

        self.criminal_table.pack(fill=BOTH, expand=1)

        self.criminal_table.bind("<ButtonRelease>", self.get_cursor)

        self.fetch_data()

    # AddFunction

    def add_data(self):
        if self.var_case_id.get() == "":
            messagebox.showerror("Error", "All Fields are required")
        else:
            try:
                conn = mysql.connector.connect(
                    host="localhost", username="root", password="", database="agency")
                my_cursor = conn.cursor()
                my_cursor.execute("insert into criminal values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (

                    self.var_case_id.get(),
                    self.var_criminal_no.get(),
                    self.var_name.get(),
                    self.var_nickname.get(),
                    self.var_father_name.get(),
                    self.var_arrest_date.get(),
                    self.var_date_of_crime.get(),
                    self.var_address.get(),
                    self.var_age.get(),
                    self.var_occupation.get(),
                    self.var_birthMark.get(),
                    self.var_crime_type.get(),
                    self.var_gender.get(),
                    self.var_wanted.get(),
                    self.var_total_amount.get()

                ))

                conn.commit()
                self.fetch_data()
                self.clear_data()
                conn.close()
                messagebox.showinfo(
                    "Success", "Criminal record has been added")
            except Exception as es:
                messagebox.showerror("Error", f"Due to{str(es)}")

    # Fetch Data

    def fetch_data(self):
        conn = mysql.connector.connect(
            host="localhost", username="root", password="", database="agency")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from criminal")
        data = my_cursor.fetchall()
        if len(data) != 0:
            self.criminal_table.delete(*self.criminal_table.get_children())
            for i in data:
                self.criminal_table.insert("", END, values=i)
            conn.commit()
        conn.close()

    # Get Cursor

    def get_cursor(self, event=""):
        cursur_row = self.criminal_table.focus()
        content = self.criminal_table.item(cursur_row)
        Data = content["values"]

        self.var_case_id.set(Data[0])
        self.var_criminal_no.set(Data[1])
        self.var_name.set(Data[2])
        self.var_nickname.set(Data[3])
        self.var_father_name.set(Data[4])
        self.var_arrest_date.set(Data[5])
        self.var_date_of_crime.set(Data[6])
        self.var_address.set(Data[7])
        self.var_age.set(Data[8])
        self.var_occupation.set(Data[9])
        self.var_birthMark.set(Data[10])
        self.var_crime_type.set(Data[11])
        self.var_gender.set(Data[12])
        self.var_wanted.set(Data[13])
        self.var_total_amount.set(Data[14])

    # Update

    def update_data(self):
        if self.var_case_id.get() == "":
            messagebox.showerror("Error", "All Fields are required.")

        else:
            try:
                update = messagebox.askyesno(
                    "Update", "Are you want to update this criminal record?")
                if update > 0:
                    conn = mysql.connector.connect(
                        host="localhost", username="root", password="", database="agency")
                    my_cursor = conn.cursor()
                    my_cursor.execute("update criminal set Criminal_NO=%s, Criminal_Name=%s, Criminal_Nickname=%s, Criminal_Father_Name=%s, Arrest_Date=%s, Date_of_Crime=%s, Address=%s, Age=%s, Occupation=%s, Birth_Mark=%s, Crime_Type=%s, Gender=%s, Wanted=%s, Total_Income=%s where Case_ID=%s", (
                        self.var_criminal_no.get(),
                        self.var_name.get(),
                        self.var_nickname.get(),
                        self.var_father_name.get(),
                        self.var_arrest_date.get(),
                        self.var_date_of_crime.get(),
                        self.var_address.get(),
                        self.var_age.get(),
                        self.var_occupation.get(),
                        self.var_birthMark.get(),
                        self.var_crime_type.get(),
                        self.var_gender.get(),
                        self.var_wanted.get(),
                        self.var_total_amount.get(),
                        self.var_case_id.get()

                    ))
                else:
                    if not update:
                        return
                conn.commit()
                self.fetch_data()
                self.clear_data()
                conn.close()
                messagebox.showinfo(
                    "Success", "Criminal record successfully updated.")
            except Exception as es:
                messagebox.showerror("Error", f"Due to{str(es)}")

    # Delete

    def delete_data(self):
        if self.var_case_id.get() == "":
            messagebox.showerror("Error", "All Fields are required.")

        else:
            try:
                Delete = messagebox.askyesno(
                    "Delete", "Are you want to delete this criminal record?")
                if Delete > 0:
                    conn = mysql.connector.connect(
                        host="localhost", username="root", password="", database="agency")
                    my_cursor = conn.cursor()
                    sql = "delete from criminal where Case_ID=%s"
                    value = (self.var_case_id.get(),)
                    my_cursor.execute(sql, value)
                else:
                    if not Delete:
                        return
                conn.commit()
                self.fetch_data()
                self.clear_data()
                conn.close()
                messagebox.showinfo(
                    "Success", "Criminal record successfully Deleted.")
            except Exception as es:
                messagebox.showerror("Error", f"Due to{str(es)}")

    # Clear

    def clear_data(self):
        self.var_case_id.set("")
        self.var_criminal_no.set("")
        self.var_name.set("")
        self.var_nickname.set("")
        self.var_father_name.set("")
        self.var_arrest_date.set("")
        self.var_date_of_crime.set("")
        self.var_address.set("")
        self.var_age.set("")
        self.var_occupation.set("")
        self.var_birthMark.set("")
        self.var_crime_type.set("")
        self.var_gender.set("")
        self.var_wanted.set("")
        self.var_total_amount.set("")

    # Search

    def search_data(self):
        if self.var_com_search.get() == "":
            messagebox.showerror("Error", "All Fields are required.")
        else:
            try:
                conn = mysql.connector.connect(
                    host="localhost", username="root", password="", database="agency")
                my_cursor = conn.cursor()
                my_cursor.execute("select * from criminal where " + str(
                    self.var_com_search.get())+" LIKE'%"+str(self.var_search.get()+"%'"))
                rows = my_cursor.fetchall()
                if len(rows) != 0:
                    self.criminal_table.delete(
                        *self.criminal_table.get_children())
                    for i in rows:
                        self.criminal_table.insert("", END, values=i)
                conn.commit()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error", f"Due to{str(es)}")


if __name__ == "__main__":
    root = Tk()
    obj = Criminal(root)
    root.mainloop()


# This code is by Ikramul
