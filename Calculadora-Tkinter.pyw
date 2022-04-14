from tkinter import *

root = Tk()

root.title('Calculadora')
root.iconbitmap('Images/calculator-icon_34473 x64.ico')
#root.geometry('600x400')
root.config(bg='white')
entry = Entry(root, bg='black', fg='white', width=20)
entry.grid(row=0, column=0, columnspan=3, padx=10, pady=10, sticky=N+S+W+E)


def num_cLick(number):
    current = entry.get()
    entry.delete(0, END)
    entry.insert(0, str(current) + str(number))

def clear_click():
    entry.delete(0, END)

def equal_click():
    s_number = entry.get()
    entry.delete(0, END)
    if math == 'suma':
        entry.insert(0, f_num + int(s_number))
    elif math == 'resta':
        entry.insert(0, f_num - int(s_number))
    elif math == 'multiplicacion':
        entry.insert(0, f_num * int(s_number))
    elif math == 'division':
        entry.insert(0, f_num / int(s_number))

def sum_click():
    global f_num
    global math
    f_number = entry.get()
    math = 'suma'
    f_num = int(f_number)
    entry.delete(0, END)

def res_click():
    global f_num
    global math
    f_number = entry.get()
    math = 'resta'
    f_num = int(f_number)
    entry.delete(0, END)

def mul_click():
    global f_num
    global math
    f_number = entry.get()
    math = 'multiplicacion'
    f_num = int(f_number)
    entry.delete(0, END)

def div_click():
    global f_num
    global math
    f_number = entry.get()
    math = 'division'
    f_num = int(f_number)
    entry.delete(0, END)
#123
butt1 = Button(root, text='1', padx=20, pady= 20, command= lambda: num_cLick(1))
butt2 = Button(root, text='2', padx=20, pady= 20, command= lambda: num_cLick(2))
butt3 = Button(root, text='3', padx=20, pady= 20, command= lambda: num_cLick(3))

butt1.grid(row=3, column=0, sticky=W+E)
butt2.grid(row=3, column=1, sticky=W+E)
butt3.grid(row=3, column=2, sticky=W+E)
#456
butt4 = Button(root, text='4', padx=20, pady= 20, command=lambda:num_cLick(4))
butt5 = Button(root, text='5', padx=20, pady= 20, command=lambda:num_cLick(5))
butt6 = Button(root, text='6', padx=20, pady= 20, command=lambda:num_cLick(6))

butt4.grid(row=2, column=0, sticky=W+E)
butt5.grid(row=2, column=1, sticky=W+E)
butt6.grid(row=2, column=2, sticky=W+E)
#879
butt7 = Button(root, text='7', padx=20, pady= 20, command= lambda: num_cLick(7))
butt8 = Button(root, text='8', padx=20, pady= 20, command= lambda: num_cLick(8))
butt9 = Button(root, text='9', padx=20, pady= 20, command= lambda: num_cLick(9))

butt7.grid(row=1, column=0, sticky=W+E)
butt8.grid(row=1, column=1, sticky=W+E)
butt9.grid(row=1, column=2, sticky=W+E)

butt0 = Button(root, text='0', padx=20, pady= 20, command=lambda:num_cLick(0))
butt0.grid(row=4, column=0, sticky=W+E)

butt_equal = Button(root, text='=', padx=20, pady= 20, command=equal_click)
butt_equal.grid(row=4, column=1, columnspan=2 , sticky=W+E)

#+-*/
butt_sum = Button(root, text='+', padx=20, pady= 20, command=sum_click)
butt_res = Button(root, text='-', padx=20, pady= 20, command=res_click)
butt_mul = Button(root, text='*', padx=20, pady= 20, command=mul_click)
butt_div = Button(root, text='/', padx=20, pady= 20, command=div_click)

butt_sum.grid(row=1, column=3, sticky=W+E)
butt_res.grid(row=2, column=3, sticky=W+E)
butt_mul.grid(row=3, column=3, sticky=W+E)
butt_div.grid(row=4, column=3, sticky=W+E)
#C
butt_c = Button(root, text='C', padx=20, pady=20, command=clear_click)

butt_c.grid(row=0, column=3, sticky=W+E)



root.mainlop(o)