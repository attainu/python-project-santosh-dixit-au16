
from tkinter import *
import tkinter.messagebox 
import sqlite3

conn = sqlite3.connect('carbooking.db')
c = conn.cursor()

class Application:
    def __init__(self, windows):
        self.windows = windows

        self.title = Label(windows, text="Bookings ", fg='black', font=('arial 40 bold'))
        self.title.place(x=150, y=20)


        self.n = Label(windows, text="Enter Owner's Name", font=('arial 18 bold'))
        self.n.place(x=0, y=100)


        self.nametextentry = Entry(windows, width=30)
        self.nametextentry.place(x=280, y=92)

        self.find = Button(windows, text="Search", width=12, height=1, bg='navajo white', command=self.search)
        self.find.place(x=350, y=132)
    def search(self):
        self.input = self.nametextentry.get()


        sql = "SELECT * FROM appointments WHERE name LIKE ?"
        self.res = c.execute(sql, (self.input,))
        for self.row in self.res:
            self.n1 = self.row[1]
            self.a = self.row[2]
            self.gen = self.row[3]
            self.loc = self.row[4]
            self.t = self.row[6]
            self.phoneNumber = self.row[5]
        self.name_update = Label(self.windows, text="Owner's Name", font=('arial 18 bold'))
        self.name_update.place(x=0, y=160)

        self.age_update = Label(self.windows, text="Age", font=('arial 18 bold'))
        self.age_update.place(x=0, y=200)

        self.gender_update = Label(self.windows, text="Gender", font=('arial 18 bold'))
        self.gender_update.place(x=0, y=240)

        self.location_update = Label(self.windows, text="Location", font=('arial 18 bold'))
        self.location_update.place(x=0, y=280)

        self.time_update = Label(self.windows, text="Entry Time", font=('arial 18 bold'))
        self.time_update.place(x=0, y=320)

        self.phoneNumber_update = Label(self.windows, text="Phone Number", font=('arial 18 bold'))
        self.phoneNumber_update.place(x=0, y=360)

        self.textEntry1 = Entry(self.windows, width=30)
        self.textEntry1.place(x=300, y=170)
        self.textEntry1.insert(END, str(self.n1))

        self.textEntry2 = Entry(self.windows, width=30)
        self.textEntry2.place(x=300, y=210)
        self.textEntry2.insert(END, str(self.a))

        self.textEntry3 = Entry(self.windows, width=30)
        self.textEntry3.place(x=300, y=250)
        self.textEntry3.insert(END, str(self.gen))

        self.textEntry4 = Entry(self.windows, width=30)
        self.textEntry4.place(x=300, y=290)
        self.textEntry4.insert(END, str(self.loc))

        self.textEntry5 = Entry(self.windows, width=30)
        self.textEntry5.place(x=300, y=330)
        self.textEntry5.insert(END, str(self.t))

        self.textEntry6 = Entry(self.windows, width=30)
        self.textEntry6.place(x=300, y=370)
        self.textEntry6.insert(END, str(self.phoneNumber))

        self.edit = Button(self.windows, text="Update?", width=20, height=2, fg='white', bg='black', command=self.update)
        self.edit.place(x=400, y=410)

        self.dlte = Button(self.windows, text="Delete?", width=20, height=2, fg='white', bg='black', command=self.delete)
        self.dlte.place(x=150, y=410)
    def update(self):
        self.variable1 = self.textEntry1.get() #updated name
        self.variable2 = self.textEntry2.get() #updated age
        self.variable3 = self.textEntry3.get() #updated gender
        self.variable4 = self.textEntry4.get() #updated location
        self.variable5 = self.textEntry5.get() #updated phone
        self.variable6 = self.textEntry6.get() #updated time

        query = "UPDATE appointments SET name=?, age=?, gender=?, location=?, phone=?, scheduled_time=? WHERE name LIKE ?"
        c.execute(query, (self.variable1, self.variable2, self.variable3, self.variable4, self.variable5, self.variable6, self.nametextentry.get(),))
        conn.commit()
        tkinter.messagebox.showinfo("Updated", "Successfully Updated.")
    def delete(self):
        sql2 = "DELETE FROM appointments WHERE name LIKE ?"
        c.execute(sql2, (self.nametextentry.get(),))
        conn.commit()
        tkinter.messagebox.showinfo("Success", "Deleted Successfully")
        self.textEntry1.destroy()
        self.textEntry2.destroy()
        self.textEntry3.destroy()
        self.textEntry4.destroy()
        self.textEntry5.destroy()
        self.textEntry6.destroy()
# creating the object
root = Tk()
b = Application(root)
root.geometry("1366x768+0+0")
root.resizable(False, False)
root.mainloop()
