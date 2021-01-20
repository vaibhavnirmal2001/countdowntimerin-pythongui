import time
from tkinter import *
from tkinter import messagebox


root = Tk()


root.geometry("400x250")


root.title("Countdown Timer")

hour = StringVar()
minute = StringVar()
second = StringVar()


hour.set("00")
minute.set("00")
second.set("00")


hourEntry = Entry(root, width=3, font=("Arial", 18, ""),
                  textvariable=hour,borderwidth="10")
hourEntry.place(x=80, y=20)

minuteEntry = Entry(root, width=3, font=("Arial", 18, ""),
                    textvariable=minute,borderwidth="10")
minuteEntry.place(x=180, y=20)

secondEntry = Entry(root, width=3, font=("Arial", 18, ""),
                    textvariable=second,borderwidth="10")
secondEntry.place(x=280, y=20)


def submit():
    try:

        temp = int(hour.get()) * 3600 + int(minute.get()) * 60 + int(second.get())
    except:
        print("Please input the right value")
    while temp > -1:


        mins, secs = divmod(temp, 60)


        hours = 0
        if mins > 60:


            hours, mins = divmod(mins, 60)

        hour.set("{0:2d}".format(hours))
        minute.set("{0:2d}".format(mins))
        second.set("{0:2d}".format(secs))


        root.update()
        time.sleep(1)


        if (temp == 0):
            messagebox.showinfo("Time Countdown", "Time's up ")


        temp -= 1



btn = Button(root, text='Start Countdown', bd='5',
             command=submit, fg="black",bg="white", font=("Helvetica 26 bold", 10 ),relief=GROOVE, padx=40,pady=20,borderwidth="20")
btn.place(x=70, y=120)
root.configure(background="black")

root.mainloop()