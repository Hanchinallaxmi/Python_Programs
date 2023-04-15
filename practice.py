import tkinter as tk

main=tk.Tk(className="emi calculator")

main.geometry("400*400")



label1=tk.label(main,text= "python")
txt1=tk.Entry(main)
btn1=tk.Button(main,text="submit")
label1.grid(row=0,colomn=0)
txt1.grid(row=0,coloumn=1)
btn1.grid(row=1,coloumn=1)  
main.mainloop()

