from tkinter import *
import tkinter as tk
from tkinter import messagebox
import hashlib
from tkinter import ttk



def click5():
    def hash(input_text):
        hash_object = hashlib.sha256()
        hash_object.update(input_text.encode())
        hashed_bytes = hash_object.digest()
        hashed_text = ''.join(format(byte, '02x') for byte in hashed_bytes)
        return hashed_text
    def check():
        login = entry_login.get()
        password = entry_password.get()

        with open('txt', 'r') as file:
            for line in file:
                login1, password1 = line.strip().split(',')
                if login == login1 and hash(password) == password1:
                    root5.destroy()
                    messagebox.showinfo("Отлично", "Вы авторизовались!")
                    root7 = Tk()
                    root7.title('Home comfort')
                    root7.resizable(False, False)
                    return
            messagebox.showerror("Ошибка", "Неверный логин или пароль!")


    def click6():
        root5.destroy()
        root6 = Tk()
        root6.title('Home comfort')
        root6.resizable(False, False)

        def register():
            login = entry_login1.get()
            password = entry_password1.get()

            login1 = None

            with open('txt', 'r') as file:
                for line in file:
                    login1, _ = line.strip().split(',')
                    if login1 == login:
                        messagebox.showerror("Ошибка", "Пользователь с таким логином уже существует.")
                        return

            with open('txt', 'a') as file:
                hashed_password = hash(password)
                if login != '' and password != '' and login1 != login:  # Проверка на уникальность логина
                    root6.destroy()
                    messagebox.showinfo("Отлично", "Вы зарегистрировались!")
                    file.write(f"{login},{hashed_password}\n")
                    click5()
                else:
                    messagebox.showinfo("Ошибка", "Вы ввели некорректные данные.")

        label_login1 = tk.Label(root6, text="Логин:")
        label_login1.pack()
        entry_login1 = tk.Entry(root6)
        entry_login1.pack()
        label_password1 = tk.Label(root6, text="Пароль:")
        label_password1.pack()
        entry_password1 = tk.Entry(root6, show="*")
        entry_password1.pack()
        button_register1 = tk.Button(root6, text="Зарегестрироваться", command=register)
        button_register1.pack()
    root5 = tk.Tk()
    root5.title('Аккаунт')
    root5.resizable(width=False, height=False)
    label_login = tk.Label(root5, text="Логин:")
    label_login.pack()
    entry_login = tk.Entry(root5)
    entry_login.pack()
    label_password = tk.Label(root5, text="Пароль:")
    label_password.pack()
    entry_password = tk.Entry(root5, show="*")
    entry_password.pack()
    button_login = tk.Button(root5, text="Войти", command=check)
    button_register = tk.Button(root5, text="Зарегестрироваться", command=click6)
    button_login.pack()
    button_register.pack()
def root7():
    def click3():
        root7.destroy()
        root3 = Tk()
        root3.title('Home comfort')
        root3.geometry('600x400')
        root3.resizable(False, False)

        # Создаем пустой Frame для создания пространства слева от списка
        left_space = ttk.Frame(root3, width=200)
        left_space.pack(side=LEFT, fill=Y)

        staff = []
        with open('txt', 'r') as file:
            for line in file:
                head, sep, tail = line.strip().partition(',')
                staff.append(head)

        staff_list = StringVar(value=staff)
        listbox = Listbox(root3, listvariable=staff_list)
        listbox.pack(side=LEFT, fill=BOTH, expand=1)

        scrollbar = ttk.Scrollbar(root3, orient="vertical", command=listbox.yview)
        scrollbar.pack(side=RIGHT, fill=Y)
        listbox["yscrollcommand"] = scrollbar.set
        
    root7 = Tk()
    root7.title('Home comfort')
    root7.resizable(False, False)
    def click11():
        root7.destroy()
    w = 1360
    s = 500
    root7.geometry('%dx%d+%d+%d' % (w, s, x-300, y))
    root7.configure(bg="#00FFFF")
    btn = Button(height=15, width=30, command=click3, padx=5, pady=5, text='Admin mode', bd=5, fg='#000', bg='#cda4de',
                 underline=0, activebackground='#000', activeforeground='#000', cursor='hand2')
    btn.place(x=10, y=120)
    btn2 = Button(height=15, width=30, command=click8, padx=5, pady=5, text='Admin mode', bd=5, fg='#000', bg='#cda4de',
                 underline=0, activebackground='#000', activeforeground='#000', cursor='hand2')
    btn2.place(x=560, y=120)
    btn3 = Button(height=15, width=30, command=click8, padx=5, pady=5, text='Admin mode', bd=5, fg='#000', bg='#cda4de',
                 underline=0, activebackground='#000', activeforeground='#000', cursor='hand2')
    btn3.place(x=285, y=120)
    btn6 = Button(height=15, width=30, command=click8, padx=5, pady=5, text='Admin mode', bd=5, fg='#000', bg='#cda4de',
                 underline=0, activebackground='#000', activeforeground='#000', cursor='hand2')
    btn6.place(x=835, y=120)
    btn5 = Button(height=15, width=30, command=click8, padx=5, pady=5, text='Admin mode', bd=5, fg='#000', bg='#cda4de',
                 underline=0, activebackground='#000', activeforeground='#000', cursor='hand2')
    btn5.place(x=1110, y=120)
    btn4 = Button(height=5, width=20, command=click11, padx=5, pady=5, text='Exit', bd=10, fg='#fff',
                  bg='#000', underline=0, activebackground='#fff', activeforeground='#fff', cursor='hand2')
    btn4.place(x=595, y=390)
def click8():
    mainroot.destroy()
    def hash(input_text):
        hash_object = hashlib.sha256()
        hash_object.update(input_text.encode())
        hashed_bytes = hash_object.digest()
        hashed_text = ''.join(format(byte, '02x') for byte in hashed_bytes)
        return hashed_text
    def check1():
        login = entry_login.get()
        password = entry_password.get()
        with open('admin ', 'r') as file:
            for line in file:
                login1, password1 = line.strip().split(',')
                if login == login1 and hash(password) == password1:
                    root8.destroy()
                    messagebox.showinfo("Отлично", "Вы авторизовались!")
                    root7()
                    return
            messagebox.showerror("Ошибка", "Неверный логин или пароль!")
    root8 = Tk()
    root8.resizable(False,False)
    label_login = tk.Label(root8, text="Логин:")
    label_login.pack()
    entry_login = tk.Entry(root8)
    entry_login.pack()
    label_password = tk.Label(root8, text="Пароль:")
    label_password.pack()
    entry_password = tk.Entry(root8, show="*")
    entry_password.pack()
    button_login = tk.Button(root8, text="Войти", command=check1)
    button_login.pack()

mainroot = Tk()
mainroot.title('Home comfort')
mainroot.resizable(False, False)
mainroot.configure(bg="aqua")
def click9():
    mainroot.destroy()
    click5()
def click10():
    mainroot.destroy()
w = 804
h = 500
ws = mainroot.winfo_screenwidth()
hs = mainroot.winfo_screenheight()
x = (ws/2) - (w/2)
y = (hs/2) - (h/2)
mainroot.geometry('%dx%d+%d+%d' % (w, h, x, y))
btn = Button(height=15, width=30, command=click8, padx=5, pady=5, text='Admin mode', bd=5, fg='#fff', bg='#cda4de',
             underline=0, activebackground='#fff', activeforeground='#fff', cursor='hand2')
btn.place(x=10, y=120)
btn2 = Button(height=15, width=30, command=click9, padx=5, pady=5, text="Customer mode", bd=5, fg='#fff', bg='#cda4de',
              underline=0, activebackground='#fff', activeforeground='#fff', cursor='hand2')
btn2.place(x=560, y=120)
btn3 = Button(height=15, width=30, command=None, padx=5, pady=5, text='Application submission mode', bd=5, fg='#fff',
              bg='#cda4de', underline=0, activebackground='#fff', activeforeground='#fff', cursor='hand2')
btn3.place(x=285, y=120)
btn4 = Button(height=5, width=20, command=click10, padx=5, pady=5, text='Exit', bd=10, fg='#fff',
              bg='#000', underline=0, activebackground='#fff', activeforeground='#fff', cursor='hand2')
btn4.place(x=320, y=390)
mainroot.mainloop()
