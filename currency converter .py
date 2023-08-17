from currency_converter import CurrencyConverter
import tkinter as tk

a = CurrencyConverter()
root = tk.Tk()
root.geometry("600x400")

def clicked():
    amount = int(e1.get())
    Currency1 = e2.get()
    Currency2 = e3.get()
    data = a.convert(amount, Currency1, Currency2)
    l5.config(text=data)

l1 = tk.Label(root, text="Currency Converter", font="Times 30 bold")
l1.place(x=100, y=20)

l2 = tk.Label(root, text="Enter Amount Here:", font="Times 18 bold", background="light blue")
l2.place(x=50, y=80)

e1 = tk.Entry(root)
e1.place(x=300, y=90)

l3 = tk.Label(root, text="Enter Currency:", font="Times 18 bold", background="light blue")
l3.place(x=50, y=130)

e2 = tk.Entry(root)
e2.place(x=300, y=140)

l4 = tk.Label(root, text="Enter Required Currency:", font="Times 18 bold", background="light blue")
l4.place(x=20, y=180)

e3 = tk.Entry(root)
e3.place(x=300, y=190)

b1 = tk.Button(root, text="Convert", font="Times 20 bold ", background="grey", command=clicked)
b1.place(x=230, y=230)

l5 = tk.Label(root, text="", font="Times 15 bold")
l5.place(x=230, y=290)

root.mainloop()
