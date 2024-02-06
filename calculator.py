import tkinter

root = tkinter.Tk()
root.title('CALCULATOR')
root.geometry('500x500')

display = tkinter.Label(root, text = "")
display.grid(row=0,column=1)

def pressed_button(btn):
    old_data= display.cget("text")
    invalid_operations = ['+','-','*','/','=']
    if btn=="0" and old_data=="":
        return
    elif btn=="0" and old_data!="" and old_data[-1] in invalid_operations:
        return
    elif old_data=="" and btn in invalid_operations:
        return
    elif old_data!="" and btn in invalid_operations and old_data[-1] in invalid_operations:
        return
    elif btn == "=":
        new_data=str(eval(old_data))
    elif btn== "C":
        new_data = old_data[:-1]
    elif btn== "AC":
        new_data = ""    
    else:
        new_data=old_data+str(btn)
    display.config(text=new_data)

count= 1
for i in range(1,4):
    for j in range(3):
        button = tkinter.Button(root, text=str(count),command=lambda k=count:pressed_button(k))
        button.grid(row=i,column=j)
        count +=1
operations = ['+','-','*','/']
for l in range(4):
        button = tkinter.Button(root, text=str(operations[l]),command=lambda k=operations[l]:pressed_button(k))
        button.grid(row=l+1,column=3)

tkinter.Button(root, text="0",command=lambda:pressed_button("0")).grid(row=4,column=1)
tkinter.Button(root, text="=",command=lambda:pressed_button("=")).grid(row=4,column=2)
tkinter.Button(root, text="C",command=lambda:pressed_button("C")).grid(row=4,column=0)
tkinter.Button(root, text="AC",command=lambda:pressed_button("AC")).grid(row=5,column=1)






root.mainloop()