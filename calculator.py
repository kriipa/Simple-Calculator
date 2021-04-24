from tkinter import *
root = Tk()
root.configure(bg="Grey")
#defining the title of the project
root.title("simple calculator")

#creating display on screen
value = StringVar()        #it manage the value of entry value
e = Entry (root, width=40,textvariable= value, borderwidth=12,justify = "right" )
e.grid(row=0, column=0, columnspan=5, ipadx=18, ipady=10)

#defining the functions
expression = " "
def button_click(item):
    global expression
    expression = expression + str(item)
    value.set(expression)
def button_clear():
    global expression
    expression = " "
    value.set(" ")
def button_eq():
    global expression
    result =str(eval(expression))
    value.set(result)
    expression = " "

#defining the buttons

button_1 = Button(root, text="1",borderwidth = 5,font=("Ariel",10,"bold"), command = lambda : button_click("1"))
button_2 = Button(root, text="2",borderwidth = 5,font=("Ariel",10,"bold"), command = lambda : button_click("2"))
button_3 = Button(root, text="3",borderwidth =5,font=("Ariel",10,"bold"), command = lambda : button_click("3"))

button_4 = Button(root, text="4",borderwidth = 5,font=("Ariel",10,"bold"), command = lambda : button_click("4"))
button_5 = Button(root, text="5",borderwidth = 5,font=("Ariel",10,"bold"), command = lambda : button_click("5"))
button_6 = Button(root, text="6",borderwidth = 5,font=("Ariel",10,"bold"), command = lambda : button_click("6"))

button_7 = Button(root, text="7",borderwidth = 5,font=("Ariel",10,"bold"), command = lambda : button_click("7"))
button_8 = Button(root, text="8",borderwidth = 5,font=("Ariel",10,"bold"), command = lambda : button_click("8"))
button_9 = Button(root, text="9",borderwidth = 5,font=("Ariel",10,"bold"), command = lambda : button_click("9"))

button_0 = Button(root, text="0",borderwidth = 5,font=("Ariel",10,"bold"), command = lambda : button_click("0"))
button_delete = Button(root, text=" C ",borderwidth = 5,font=("Ariel",10,"bold"),  fg= "white",bg="red", command = lambda : button_clear())
button_add = Button(root, text=" + ",borderwidth = 5,font=("Ariel",10,"bold"),  fg= "white",bg="grey", command = lambda : button_click("+"))
button_sub = Button(root, text=" - ",borderwidth = 5,font=("Ariel",10,"bold"),  fg= "white",bg="grey", command = lambda : button_click("-"))
button_mul = Button(root, text=" x ",borderwidth = 5,font=("Ariel",10,"bold"),  fg= "white",bg="grey", command = lambda : button_click("*"))
button_div = Button(root, text=" ÷ ",borderwidth = 5,font=("Ariel",10,"bold"),  fg= "white",bg="grey", command = lambda : button_click(" / "))
button_equal = Button(root, text=" = ",borderwidth = 5,font=("Ariel",10,"bold"), fg= "white",bg="black", command = lambda : button_eq())

#putting buttons on the screen
button_1.grid(row=4, column=0,padx=5, pady=5,ipadx = 20, ipady = 15)
button_2.grid(row=4, column=1,padx=5, pady=5,ipadx = 20, ipady = 15)
button_3.grid(row=4, column=2,padx=5, pady=5,ipadx = 20, ipady = 15)

button_4.grid(row=3, column=0,padx=5, pady=5,ipadx = 20, ipady = 15)
button_5.grid(row=3, column=1,padx=5, pady=5,ipadx = 20, ipady = 15)
button_6.grid(row=3, column=2,padx=5, pady=5,ipadx = 20, ipady = 15)

button_7.grid(row=2, column=0,padx=5, pady=5,ipadx = 20, ipady = 15)
button_8.grid(row=2, column=1,padx=5, pady=5,ipadx = 20, ipady = 15)
button_9.grid(row=2, column=2,padx=5, pady=5,ipadx = 20, ipady = 15)

button_0.grid(row=5, column=1,padx=3, pady=5,ipadx = 20, ipady = 15)
button_delete.grid(row=5, column=0, padx=5, pady=7,ipadx = 20, ipady = 15)
button_add.grid(row=3, column=3, padx=5, pady=7,ipadx = 20, ipady = 15)
button_sub.grid(row=2, column=3, padx=5, pady=7,ipadx = 20, ipady = 15)
button_mul.grid(row=5, column=2, padx=5, pady=7,ipadx = 20, ipady = 15)
button_div.grid(row=4, column=3, padx=5, pady=7,ipadx = 20, ipady = 15)
button_equal.grid(row=5, column=3, padx=5, pady=7,ipadx = 20, ipady = 15)

root.mainloop()  #mainloop runs the program multiple times
