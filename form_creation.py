import tkinter
import re

root = tkinter.Tk()
root.title('FORM TITLE')
root.geometry('500x500')

def registered():
    name = entry1.get()
    email = entry2.get()
    pattern= '^[a-z0-9\._]+@[a-z]+\.[a-z]{2,5}$'
    email_check = re.match(pattern,email)
    mob_no = entry3.get()
    msg = text.get("1.0",tkinter.END)
    if email_check:
        label5.config(text="Form is submitted")
    else:
        label5.config(text="Form is failed to submitted")    
label1 = tkinter.Label(root, text= "Enter Your Full Name")
label1.pack()
entry1 = tkinter.Entry(root, width=30)
entry1.pack()

label2 = tkinter.Label(root, text= "Email address")
label2.pack()
entry2 = tkinter.Entry(root, width=30)
entry2.pack()

label3 = tkinter.Label(root, text= "Mobile number")
label3.pack()
entry3= tkinter.Entry(root, width=30)
entry3.pack()

label4 = tkinter.Label(root, text= "Message")
label4.pack()
text = tkinter.Text(root, width=30, height=5)
text.pack()

button = tkinter.Button(root, text="Submit", command=registered)
button.pack()

label5 = tkinter.Label(root, text= "")
label5.pack()




root.mainloop()