from tkinter import *
result = ""
def press(num):
    global result
    result = result + str(num)
    equation.set(result)
def equalpress():
    try:
        global result
        total = str(eval(result))
        equation.set(total)
        result = ""
        # if error is generate then handle
    except:
        equation.set(" error ")
        result = ""


def clear():
    global result
    result = ""
    equation.set("")


if __name__ == "__main__":

    root = Tk()
    root.configure(background="blue")
    root.title("CALCULATOR")
    root.geometry("450x270")
    equation = StringVar()
    result_field= Entry(root,bd=7,font=("",18), textvariable=equation)
    result_field.grid(padx=20,columnspan=4, ipadx=70)

    equation.set('enter your expression')


    button1 = Button(root, text=' 1 ', fg='black', bg='green', command=lambda: press(1), height=3, width=10)
    button1.grid(row=2, column=0)

    button2 = Button(root, text=' 2 ', fg='black', bg='green', command=lambda: press(2), height=3, width=10)
    button2.grid(row=2, column=1)

    button3 = Button(root, text=' 3 ', fg='black', bg='green', command=lambda: press(3), height=3, width=10)
    button3.grid(row=2, column=2)

    button4 = Button(root, text=' 4 ', fg='black', bg='green', command=lambda: press(4), height=3, width=10)
    button4.grid(row=3, column=0)

    button5 = Button(root, text=' 5 ', fg='black', bg='green', command=lambda: press(5), height=3, width=10)
    button5.grid(row=3, column=1)

    button6 = Button(root, text=' 6 ', fg='black', bg='green', command=lambda: press(6), height=3, width=10)
    button6.grid(row=3, column=2)

    button7 = Button(root, text=' 7 ', fg='black', bg='green', command=lambda: press(7), height=3, width=10)
    button7.grid(row=4, column=0)

    button8 = Button(root, text=' 8 ', fg='black', bg='green', command=lambda: press(8), height=3, width=10)
    button8.grid(row=4, column=1)

    button9 = Button(root, text=' 9 ', fg='black', bg='green', command=lambda: press(9), height=3, width=10)
    button9.grid(row=4, column=2)

    button0 = Button(root, text=' 0 ', fg='black', bg='green', command=lambda: press(0), height=3, width=10)
    button0.grid(row=5, column=0)

    clear = Button(root, text=' clear ', fg='black', bg='red', command=clear, height=3, width=10)
    clear.grid(row=2, column=3)

    divide = Button(root, text=' / ', fg='black', bg='yellow', command=lambda: press("/"), height=3, width=10)
    divide.grid(row=3, column=3)

    multiply = Button(root, text=' * ', fg='black', bg='yellow', command=lambda: press("*"), height=3, width=10)
    multiply.grid(row=4, column=3)

    substract = Button(root, text=' - ', fg='black', bg='yellow', command=lambda: press("-"), height=3, width=10)
    substract.grid(row=5, column=3)

    add = Button(root, text='+', fg='black', bg='yellow', command=lambda:press("+"), height=3, width=10)
    add.grid(row=5, column='2')

    equal = Button(root, text=' = ', fg='black', bg='pink', command=equalpress, height=3, width=10)
    equal.grid(row=5, column=1)



    # start the GUI
    root.mainloop()