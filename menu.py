from tkinter import *
import tkinter as tk
from tkinter import messagebox
import hashlib
from tkinter import ttk
import webbrowser

def start():
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
            def back():
                root6.destroy()
                click5()

            btn4 = Button(height=1, width=10, command=back, padx=5, pady=5, text='Previous page', bd=10, fg='#fff',
                          bg='#000', underline=0, activebackground='#fff', activeforeground='#fff', cursor='hand2')
            btn4.pack()

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
        def back():
            root5.destroy()
            start()

        btn4 = Button(height=1, width=10, command=back, padx=5, pady=5, text='Main page', bd=10, fg='#fff',
                      bg='#000', underline=0, activebackground='#fff', activeforeground='#fff', cursor='hand2')
        btn4.pack()

    def root17():
        def click3():
            root7.destroy()
            root3 = Tk()
            root3.title('Home comfort')
            root3.geometry('600x400')
            root3.resizable(False, False)
            def exit():
                root3.destroy()
                root17()
            def delete_account():
                login = entry_login.get()
                with open('txt', 'r') as file:
                    lines = file.readlines()
                with open('txt', 'w') as file:
                    account_deleted = False
                    for line in lines:
                        login1, _ = line.strip().split(',')
                        if login1 == login:
                            messagebox.showinfo("Удаление", "Аккаунт удален!")
                            account_deleted = True
                        else:
                            file.write(line)
                    if account_deleted:
                        root3.destroy()
                        root17()
                    else:
                        messagebox.showinfo("Удаление", "Неверный логин!")

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
            scrollbar = ttk.Scrollbar(root3, orient="horizontal", command=listbox.xview)
            scrollbar.pack(side=tk.BOTTOM, fill=X)
            listbox["xscrollcommand"] = scrollbar.set
            btn4 = Button(height=4, width=10, command=delete_account, padx=5, pady=5, text='delete_account', bd=2, fg='#fff',
                          bg='#000', underline=0, activebackground='#fff', activeforeground='#fff', cursor='hand2')
            btn5 = Button(height=2, width=10, command=exit, padx=5, pady=5, text='Previous page', bd=2,
                          fg='#fff',
                          bg='#000', underline=0, activebackground='#fff', activeforeground='#fff', cursor='hand2')
            btn5.place(x=50, y=340)
            btn4.place(x=50, y=250)
            label_login = tk.Label(root3, text="Логин:")
            label_login.place(x=60, y=10)
            entry_login = tk.Entry(root3)
            entry_login.place(x=30, y=30)

        root7 = Tk()
        root7.title('Home comfort')
        root7.resizable(False, False)
        def click13():
            root7.destroy()
            with open('The_database.json', 'r+') as file:
                file.truncate(0)
                file.seek(0)
            messagebox.showinfo('Увольнение', 'Вы уволили всех')
            root17()
        def click12():
            root7.destroy()
            with open('txt', 'w') as file:
                file.write('')
            with open('The_database.json', 'r+') as file:
                file.truncate(0)
                file.seek(0)
            with open('user_data.json', 'r+') as file:
                file.truncate(0)
                file.seek(0)
            messagebox.showinfo('Банкротство', 'Вы обонкрочены')
            exit()
        def click11():
            root7.destroy()

        w = 1360
        s = 500
        root7.geometry('%dx%d+%d+%d' % (w, s, x - 300, y))
        root7.configure(bg="#00FFFF")
        btn = Button(height=15, width=30, command=click3, padx=5, pady=5, text='User delete', bd=5, fg='#000', bg='#cda4de',
                     underline=0, activebackground='#000', activeforeground='#000', cursor='hand2')
        btn.place(x=10, y=120)
        btn2 = Button(height=15, width=30, command=click13, padx=5, pady=5, text='Fire everyone', bd=5, fg='#000', bg='#cda4de',
                      underline=0, activebackground='#000', activeforeground='#000', cursor='hand2')
        btn2.place(x=560, y=120)
        btn3 = Button(height=15, width=30, command=click8, padx=5, pady=5, text='Admin mode', bd=5, fg='#000', bg='#cda4de',
                      underline=0, activebackground='#000', activeforeground='#000', cursor='hand2')
        btn3.place(x=285, y=120)
        btn6 = Button(height=15, width=30, command=click8, padx=5, pady=5, text='Admin mode', bd=5, fg='#000', bg='#cda4de',
                      underline=0, activebackground='#000', activeforeground='#000', cursor='hand2')
        btn6.place(x=835, y=120)
        btn5 = Button(height=15, width=30, command=click12, padx=5, pady=5, text='Go bankrupt and fire everyone', bd=5, fg='#000', bg='#cda4de',
                      underline=0, activebackground='#000', activeforeground='#000', cursor='hand2')
        btn5.place(x=1110, y=120)
        def back():
            root7.destroy()
            start()
        btn4 = Button(height=5, width=20, command=back, padx=5, pady=5, text='Main page', bd=10, fg='#fff',
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
                        root17()
                        return
                messagebox.showerror("Ошибка", "Неверный логин или пароль!")

        root8 = Tk()
        root8.resizable(False, False)
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
        def back():
            root8.destroy()
            start()
        btn4 = Button(height=1, width=6, command=back, padx=5, pady=5, text='Main page', bd=10, fg='#fff',
                      bg='#000', underline=0, activebackground='#fff', activeforeground='#fff', cursor='hand2')
        btn4.pack()


    mainroot = Tk()
    mainroot.title('Home comfort')
    mainroot.resizable(False, False)
    mainroot.configure(bg="aqua")


    def click9():
        mainroot.destroy()
        click5()


    def click10():
        mainroot.destroy()
    def open_link(event):
        url = "https://web.telegram.org/k/#@ItprrogerTestbot"
        webbrowser.open(url)
    def click15():
        mainroot.destroy()

        root125 = tk.Tk()
        root125.resizable(False,False)
        root125.title('Home comfort')
        def back():
            root125.destroy()
            start()

        label1 = tk.Label(root125, text="Зарегистрируйтесь здесь")
        label1.pack()
        # Текст, при клике на который откроется ссылка
        label = tk.Label(root125, text="Нажмите сюда, чтобы перейти на телеграмм бота для регистрации", fg="blue", cursor="hand2")
        label.pack(pady=20)

        # Привязываем событие клика мышью к функции открытия ссылки
        label.bind("<Button-1>", open_link)
        btn4 = Button(height=1, width=6, command=back, padx=5, pady=5, text='Main page', bd=10, fg='#fff',
                      bg='#000', underline=0, activebackground='#fff', activeforeground='#fff', cursor='hand2')
        btn4.pack()


    w = 804
    h = 500
    ws = mainroot.winfo_screenwidth()
    hs = mainroot.winfo_screenheight()
    x = (ws / 2) - (w / 2)
    y = (hs / 2) - (h / 2)
    mainroot.geometry('%dx%d+%d+%d' % (w, h, x, y))
    btn = Button(height=15, width=30, command=click8, padx=5, pady=5, text='Admin mode', bd=5, fg='#fff', bg='#cda4de',
                 underline=0, activebackground='#fff', activeforeground='#fff', cursor='hand2')
    btn.place(x=10, y=120)
    btn2 = Button(height=15, width=30, command=click9, padx=5, pady=5, text="Customer mode", bd=5, fg='#fff', bg='#cda4de',
                  underline=0, activebackground='#fff', activeforeground='#fff', cursor='hand2')
    btn2.place(x=560, y=120)
    btn3 = Button(height=15, width=30, command=click15, padx=5, pady=5, text='Application submission mode', bd=5, fg='#fff',
                  bg='#cda4de', underline=0, activebackground='#fff', activeforeground='#fff', cursor='hand2')
    btn3.place(x=285, y=120)
    btn4 = Button(height=5, width=20, command=click10, padx=5, pady=5, text='Exit', bd=10, fg='#fff',
                  bg='#000', underline=0, activebackground='#fff', activeforeground='#fff', cursor='hand2')
    btn4.place(x=320, y=390)
    mainroot.mainloop()
start()
