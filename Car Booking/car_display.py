from tkinter import *
import sqlite3
import pyttsx3

conn = sqlite3.connect('carbooking.db')
c = conn.cursor()

no = []
clients = []

sql = "SELECT * FROM appointments"
res = c.execute(sql)
for r in res:
    ids = r[0]
    name = r[1]
    no.append(ids)
    clients.append(name)

class Application:
    def __init__(self, windows):
        self.windows = windows

        self.x = 0
        
        # title
        self.title = Label(windows, text="Bookings", font=('arial 60 bold'), fg='green')
        self.title.place(x=350, y=0)

        self.replace = Button(windows, text="Next Booking", width=25, height=2, bg='steelblue', command=self.function)
        self.replace.place(x=500, y=600)

        self.none = Label(windows, text="", font=('arial 200 bold'))
        self.none.place(x=500, y=100)

        self.clients_name = Label(windows, text="", font=('arial 80 bold'))
        self.clients_name.place(x=300, y=400)
    def function(self):
        self.none.config(text=str(no[self.x]))
        self.clients_name.config(text=str(clients[self.x]))
        voice = pyttsx3.init()
        voices = voice.getProperty('voices')
        rate = voice.getProperty('rate')
        voice.setProperty('rate', rate-50)
        voice.say('Booking number ' + str(no[self.x]) + str(clients[self.x]))
        voice.runAndWait()
        self.x += 1
root = Tk()
b = Application(root)
root.geometry("1366x768+0+0")
root.resizable(False, False)
root.mainloop()
