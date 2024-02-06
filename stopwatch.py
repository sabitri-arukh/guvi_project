import tkinter

root = tkinter.Tk()
root.title('STOPWATCH')
root.geometry('400x400')

display = tkinter.Label(root, text = "00:00:00:000")
display.pack()

mseconds = 0
seconds= 0
minutes= 0
hours= 0
reset = False
stop = False


def reset_timer():
    global mseconds
    global seconds
    global minutes
    global hours
    global reset
    reset = True
    mseconds= 0
    seconds= 0
    minutes= 0
    hours= 0
    display.config(text="00:00:00:000")


def stop_timer():
    global stop
    stop = True

def start_timer():
    global mseconds
    global seconds
    global minutes
    global hours
    global reset
    global stop

    if stop:
        stop=False
        return

    mseconds=int(mseconds)
    seconds= int(seconds)
    minutes= int(minutes)
    hours= int(hours)

    mseconds += 1
    if mseconds==1000:
        mseconds=0 
        seconds += 1
    if seconds==60:
        seconds=0 
        minutes += 1
    if minutes==60:
        minutes=0
        hours +=1    
    if mseconds<10:
        mseconds= "00"+ str(mseconds)
    elif mseconds<100:
        mseconds="0"+ str(mseconds)
    if seconds<10:
        seconds= "0"+ str(seconds)
    if minutes<10:
        minutes= "0"+ str(minutes)
    if hours<10:
        hours= "0"+ str(hours)

    if reset:
        timer="00:00:00:000"
        mseconds= 0
        seconds= 0
        minutes= 0
        hours= 0
        stop=True
        reset=False
    else:
        timer=str(hours)+":"+str(minutes)+":"+str(seconds)+":"+str(mseconds)
    display.config(text=timer)
    
    root.after(1,start_timer)

button1 = tkinter.Button(root, text="Start",command=lambda j=mseconds, k=seconds ,l=minutes, m=hours: start_timer())
button1.pack()
button2 = tkinter.Button(root, text="Stop",command=stop_timer)
button2.pack()
button3 = tkinter.Button(root, text="Reset", command=reset_timer)
button3.pack()




root.mainloop()