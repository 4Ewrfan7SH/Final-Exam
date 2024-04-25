from tkinter import *
from tkinter import messagebox
from time import sleep
from FinalCode_DB import Database
# DB ---------------

db = Database('J:/python/database/test.db')

# Funcs --------------------------

def clear_entry():
    message = messagebox.askyesno('خالی کردن ورودی ها','ایا از خالی کردن جعبه متن ها اطمینان دارید ؟ ?')
    if message == True:
        en_name.delete(0,END)
        en_family.delete(0,END)
        en_packname.delete(0,END)
        en_packpassword.delete(0,END)
        en_password.delete(0,END)
        en_name.focus_set()

def clear():
    en_name.delete(0,END)
    en_family.delete(0,END)
    en_packname.delete(0,END)
    en_packpassword.delete(0,END)
    en_password.delete(0,END)
    en_name.focus_set()

def show_list():
    lst_box.delete(0,END)
    record = db.fetch()
    for i in record:
        lst_box.insert(END,i)

def insert():
    if len(en_name.get()) == 0 or (en_name.get()).isdigit():
        messagebox.showerror('خطا' , 'جعبه متن نام را پر کنید(A-Z)!')

    elif len(en_family.get()) == 0 or (en_family.get()).isdigit():
        messagebox.showerror('خطا' , 'جعبه متن نام خانوادگی را پر کنید(A-Z)!')
    
    elif len(en_password.get()) == 0 or (en_password.get()).isalpha():
        messagebox.showerror('خطا','جعبه متن رمز ورود را پر کنید(0-9)')

    else:
        lst_box.insert(0,f'{en_name.get()}-{en_family.get()}-{en_packname.get()}-{en_password.get()}')
        db.insert(en_name.get(),en_family.get(),en_packname.get(),en_password.get())
        clear()
        show_list()

def select_item(event):
    global selected_item
    index = lst_box.curselection()
    selected_item = lst_box.get(index)
    clear()
    en_name.insert(END,selected_item[1])
    en_family.insert(END,selected_item[2])
    en_packname.insert(END,selected_item[3])
    en_password.insert(END,selected_item[4])

def remove():
    message = messagebox.askyesno('حذف داده','ایا برای حذف اطمینان دارید ؟?')
    if message == True:
        db.remove(selected_item[0])
        clear()
        show_list()

def login():
    try:
        if en_packpassword.get() != '' :
            packpassword = db.system_password(en_packpassword.get())
            list_password = [i for i in packpassword[0]]
            if int(en_packpassword.get()) == int(list_password[4]):
                messagebox.showinfo('ورود موفق',f'به سامانه خوش امدید ')
            elif en_packpassword.get() == '' : 
                messagebox.showerror('خطا' , 'شما هنوز ثبت نام نکرده اید یا به درستی رمز را وارد نکردید')
    except IndexError :
        messagebox.showerror('خطا','شما هنوز ثبت نام نکرده اید یا به درستی رمز را وارد نکردید')

def exit():
    message = messagebox.askyesno('خروج' , 'ایا برای خروج اطمینان دارید ؟')
    if message == True :
        sleep(0.4)
        root.destroy()

# Win ---------------------------

root = Tk()
root.geometry('600x500')
root.resizable(0,0)
root.title('Package')
root['bg'] = '#3D9755'

# Frame -------------------

frame = Frame(root,width=700 , height=120 , bg= '#FFFFFF')
frame.place(relx=0.5 , rely=0.1 , anchor='c')

# Buttons -----------------

btn_viewall = Button(root,text='مشاهده همه' , font='tahoma 10' , width=14 ,command=show_list)
btn_viewall.place(relx=0.88 , y= 150 , anchor='c')

btn_insert = Button(root,text='اضافه کردن' , font='tahoma 10' , width=14 , command=insert)
btn_insert.place(relx=0.88 , y= 190 , anchor='c')

btn_clear = Button(root,text='خالی کردن ورودیها' , font='tahoma 10' , width=14 , command=clear_entry)
btn_clear.place(relx=0.88 , y = 230 , anchor='c')

btn_remove = Button(root,text='حذف کردن' , font='tahoma 10' , width=14 , command=remove)
btn_remove.place(relx=0.88 , y=270 , anchor='c')

btn_exit = Button(root,text='خروج' , font='tahoma 10' , width=14 , command=exit)
btn_exit.place(relx= 0.88 , y= 310 , anchor='c')

btn_login = Button(root,text='ورود به سامانه' , font='tahoma 10' , width=14 , command=login)
btn_login.place(relx= 0.88 , rely=0.94 , anchor='c')

# Listbox -----------------

lst_box = Listbox(root,width=50 , height=13 , font='arial 11')
lst_box.place(relx=0.4 , rely=0.48 , anchor='c')
lst_box.bind('<<ListboxSelect>>',select_item)

# Entrys ------------------

en_name = Entry(root,font='arial 10' , width=14 , bg='#FFFFFD')
en_name.place(relx=0.7 , rely=0.05 , anchor='c')

en_family = Entry(root,font='arial 10' , width=14 , bg='#FFFFFD')
en_family.place(relx= 0.22 , rely= 0.05 , anchor='c')

en_packname = Entry(root,font='arial 10' , width=14 , bg='#FFFFFD')
en_packname.place(relx=0.7 , rely=0.15 , anchor='c')

en_password = Entry(root,font='arial 10' , width=14 , bg='#FFFFFD')
en_password.place(relx=0.22 , rely=0.15 , anchor='c')

en_packpassword = Entry(root,font='arial 10' , width=45 , bg='#FFFFFD') 
en_packpassword.place(relx=0.3 , rely=0.94 , anchor='c')

# Label ------------------------

lbl_name = Label(root,text=':نام',font='arial 14' , bg='#FFFFFF')
lbl_name.place(relx=0.81 , rely=0.045 , anchor='c')

lbl_family = Label(root,text=':نام خانوادگی',font='arial 14' , bg='#FFFFFF')
lbl_family.place(relx=0.38 , rely=0.045 , anchor='c')

lbl_packname = Label(root,text=':نام دوره',font='arial 14' , bg='#FFFFFF')
lbl_packname.place(relx=0.84 , rely=0.145 , anchor='c')

lbl_password = Label(root,text=':رمز ورود',font='arial 14' , bg='#FFFFFF')
lbl_password.place(relx=0.37 , rely=0.145 , anchor='c')

lbl_packpassword = Label(root,text=':رمز ورود',font='arial 14' , bg='#3D9755')
lbl_packpassword.place(relx=0.63 , rely=0.94 , anchor='c')


#----------------
root.mainloop() # shafiei