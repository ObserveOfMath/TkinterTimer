import time
from tkinter import *
from tkinter import messagebox

stop = False

root = Tk()

root.geometry("300x250")
root.iconbitmap("icon.ico")
root.title("Tkinter Timer")

hour = StringVar()
minute = StringVar()
second = StringVar()

hour.set("00")
minute.set("00")
second.set("00")

hourEntry = Entry(root, width=3, font=("Arial",18,""),
    textvariable=hour).place(x=80, y=20)
minuteEntry = Entry(root, width=3, font=("Arial",18,""),
    textvariable=minute).place(x=130,y=20)
secondEntry= Entry(root, width=3, font=("Arial",18,""),
    textvariable=second).place(x=180,y=20)


def submit():

    global stop

    try:
        temp = int(hour.get())*3600 + int(minute.get())*60 + int(second.get())
    except:
        print("Please input the right value")

    while temp > -1:

        if not stop:
            mins,secs = divmod(temp,60) 
            hours=0

            if mins > 60:
                hours, mins = divmod(mins, 60)
             
            hour.set("{0:2d}".format(hours))
            minute.set("{0:2d}".format(mins))
            second.set("{0:2d}".format(secs))
            
            root.update()
            time.sleep(1)

            if (temp == 0):
                messagebox.showinfo("Break", "Time's up, take a break.")
             
            temp -= 1

        else:
            stop = False
            break

def stop_timer():
    global stop, hour, minute, second
    stop = True
    hour.set("00")
    minute.set("00")
    second.set("00")


submit = Button(root, text='Set Time Countdown',
    command=submit).place(x=90, y=120)

reset = Button(root, text='Reset Timer',
    command=stop_timer).place(x=115, y=90)

root.mainloop()