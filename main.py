from tkinter import *
from tkinter import ttk
import pymysql






class student:
       def __init__(self, root):
           self.root = root
           self.root.title("Student Management System")
           self.root.geometry("1600x900+0+0")

           title = Label(self.root, text="Student Management System",bd = 10,relief= "ridge",font= ("times new roman", 40,"bold"),bg = "black",fg="white")
           title.pack(side=TOP, fill=X)

           #========All Variables==================================


           self.Roll_No_var = StringVar()
           self.Name_var = StringVar()
           self.Email_var = StringVar()
           self.Gender_var = StringVar()
           self.Contact_var = StringVar()
           self.DOB_var = StringVar()




               #=====manage frame ==================================================
           manage_Frame = Frame(self.root, border=4, relief=RIDGE, bg="#1f1f2e")
           manage_Frame.place(x=20, y=100, width=450, height=700)

           m_title = Label(manage_Frame, text="Manage Students", bg="#1f1f2e", fg="white", font=("times new roman", 20, "bold"))
           m_title.grid(row=0, columnspan=2, pady=20)


           lbl_roll = Label(manage_Frame, text="Roll No.", bg="#1f1f2e", fg="white", font=("times new roman", 20, "bold"))
           lbl_roll.grid(row=1, column=0, pady=10, padx=20, sticky="w")

           txt_roll =Entry(manage_Frame, textvariable=self.Roll_No_var, font=("times new roman", 15, "bold"), bd=5, relief="ridge")
           txt_roll.grid(row=1, column=1, pady=10, padx=8, sticky="w")


           lbl_name= Label(manage_Frame, text="Name", bg="#1f1f2e", fg="white",font=("times new roman", 20, "bold"))
           lbl_name.grid(row=2, column=0, pady=10, padx=20, sticky="w")

           txt_name=Entry(manage_Frame,  textvariable=self.Name_var,font=("times new roman", 15, "bold"), bd=5, relief="ridge")
           txt_name.grid(row=2, column=1, pady=10, padx=8, sticky="w")




           lbl_email = Label(manage_Frame, text="Email", bg="#1f1f2e", fg="white",
                           font=("times new roman", 20, "bold"))
           lbl_email.grid(row=3, column=0, pady=10, padx=20, sticky="w")

           txt_email =Entry(manage_Frame,  textvariable= self.Email_var, font=("times new roman", 15, "bold"), bd=5, relief="ridge")
           txt_email.grid(row=3, column=1, pady=10, padx=8, sticky="w")

           lbl_gender= Label(manage_Frame, text="Gender", bg="#1f1f2e", fg="white", font=("times new roman", 20, "bold"))
           lbl_gender.grid(row=4, column=0, pady=10, padx=20, sticky="w")

           combo_gender=ttk.Combobox(manage_Frame, textvariable=self.Gender_var,font=("times new roman", 15, "bold"), state="readonly")
           combo_gender['values'] = ("Male", "Female", "Other")
           combo_gender.grid(row=4, column=1, padx=5, pady=10, sticky="w")

           lbl_contact= Label(manage_Frame, text="Contact", bg="#1f1f2e", fg="white", font=("times new roman", 20, "bold"))
           lbl_contact.grid(row=5, column=0, pady=10, padx=20, sticky="w")

           txt_contact =Entry(manage_Frame,  textvariable=self.Contact_var, font=("times new roman", 15, "bold"), bd=5, relief="ridge")
           txt_contact.grid(row=5, column=1, pady=10, padx=8, sticky="w")

           lbl_dob= Label(manage_Frame, text="D.O.B", bg="#1f1f2e", fg="white", font=("times new roman", 20, "bold"))
           lbl_dob.grid(row=6, column=0, pady=10, padx=20, sticky="w")

           txt_dob =Entry(manage_Frame, textvariable=self.DOB_var, font=("times new roman", 15, "bold"), bd=5, relief="ridge")
           txt_dob.grid(row=6, column=1, pady=10, padx=8, sticky="w")

           lbl_address= Label(manage_Frame, text="Address", bg="#1f1f2e", fg="white", font=("times new roman", 20, "bold"))
           lbl_address.grid(row=7, column=0, pady=10, padx=20, sticky="w")

           txt_address =Text(manage_Frame, height=3, width=15, font=("times new roman", 20, "bold"))
           txt_address.grid(row=7, column=1, pady=10, padx=20, sticky="w")

#===========Button Frame==================

           btn_Frame = Frame(manage_Frame, border=4, bg="#1f1f2e")
           btn_Frame.place(x=10, y=540, width=430)

           Addbtn=Button(btn_Frame, text="Add", width=5, command= self.add_students).grid(row=0, column=0, padx=10, pady=10)
           updatebtn=Button(btn_Frame, text="Update", width=5).grid(row=0, column=1, padx=10, pady=10)
           delbtn=Button(btn_Frame, text="Delete", width=5).grid(row=0, column=2, padx=10, pady=10)
           clearbtn=Button(btn_Frame, text="Clear", width=5).grid(row=0, column=3, padx=10, pady=10)

           # =====detail frame ==================================================

           detail_Frame=Frame(self.root, bd=4, relief=RIDGE, bg="#1f1f2e")
           detail_Frame.place(x=500, y=100, width=1000, height=700)

           lbl_search=Label(detail_Frame, text="Search By", bg="#1f1f2e", fg="white", font=("times new roman", 20, "bold"))
           lbl_search.grid(row=0, column=0, padx=20, pady=10, sticky="w")

           combo_search=ttk.Combobox(detail_Frame, width=10, font=("times new roman", 15, "bold"), state="readonly")
           combo_search['values'] = ("Roll", "Name", "Contact")
           combo_search.grid(row=0, column=1, padx=20, pady=10, sticky="w")

           txt_search=Entry(detail_Frame, font=("times new roman", 15, "bold"), bd=5, relief="ridge")
           txt_search.grid(row=0, column=2, pady=10, padx=8, sticky="w")

           searchbtn=Button(detail_Frame, text="Search", width=5).grid(row=0, column=3, padx=10, pady=10)
           showallbtn=Button(detail_Frame, text="Show All", width=5).grid(row=0, column=4, padx=10, pady=10)




           #======table frame=====================================================

           table_Frame=Frame(detail_Frame, bd=4, relief=RIDGE, bg="white")
           table_Frame.place(x=10, y=70, width=965, height=600)


           scroll_x=Scrollbar(table_Frame, orient=HORIZONTAL)
           scroll_y=Scrollbar(table_Frame, orient=VERTICAL)

           student_table=ttk.Treeview(table_Frame, column=("Roll", "Name", "Gender", "Email",  "Contact", "DOB", "Address"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
           scroll_x.pack(side=BOTTOM, fill=X)
           scroll_y.pack(side=RIGHT, fill=Y)
           scroll_x.config(command=student_table.xview)
           scroll_y.config(command=student_table.yview)
           student_table.heading("Roll", text="Roll No.")
           student_table.heading("Name", text="Name")
           student_table.heading("Email", text="Email")
           student_table.heading("Gender", text="Gender")
           student_table.heading("Contact", text="Contact")
           student_table.heading("DOB", text="D.O.B")
           student_table.heading("Address", text="Address")
           student_table['show'] = "headings"
           student_table.column("Roll", width=100)
           student_table.column("Name", width=150)
           student_table.column("Email", width=300)
           student_table.column("Gender", width=100)
           student_table.column("Contact", width=200)
           student_table.column("DOB", width=100)
           student_table.column("Address", width=300)
           student_table.pack(fill=BOTH, expand=1)


       def add_students(self):
             con=pymysql.connect(host="localhost", user="root", password="", database="stm")
             cur=con.cursor()
             cur.execute("insert into students values(%s, %s,%s, %s,%s, %s,%s,)", (self.Roll_No_var.get(),
                                                                                   self.Name_var.get(),
                                                                                   self.Email_var.get(),
                                                                                   self.Gender_var.get(),
                                                                                   self.Contact_var.get(),
                                                                                   self.DOB_var.get('1.0',END),

                                                                                   ))


             con.commit()
             con.close()



root= Tk()
ob = student(root)
root.mainloop()
