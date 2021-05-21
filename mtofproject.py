from tkinter import Tk, Button, Label, DoubleVar, Entry
root=Tk()
root.title("Meter to Feet Conversion App ")
root.configure(background="orange")
root.geometry("320x220")
root.resizable(width=True, height=True)

def convert():
    val = float(mt_entry.get())
    feet = val * 3.28084
    ft_value.set("%.4f" % feet)
def clear():
    ft_value.set("")
    mt_value.set("")
mtoflabel = Label(root,text="Meter",bg="purple",fg="white",width=14)
mtoflabel.grid(column=0,row=0,padx=20,pady=20)



mt_value=DoubleVar()
mt_entry=Entry(root,textvariable=mt_value, width=14)
mt_entry.grid(column=1,row=0,pady=20)
mt_entry.delete(0,'end')


ftoflabel = Label(root,text="Feet",bg="purple",fg="white",width=14)
ftoflabel.grid(column=0,row=1,padx=30,pady=30)

ft_value=DoubleVar()
ft_entry=Entry(root,textvariable=ft_value, width=14)
ft_entry.grid(column=1,row=1,pady=30)
ft_entry.delete(0,'end')

convert_button = Button(root,text="Convert",bg="blue",fg="white",width=14, command=convert)
convert_button.grid(column=0,row=3,padx=20)

clear_button = Button(root,text="Clear",bg="black",fg="white",width=14, command=clear)
clear_button.grid(column=1,row=3,padx=20)


root.mainloop()
