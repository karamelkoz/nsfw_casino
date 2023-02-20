#liblary
import random
import sqlite3
from sqlite3 import Cursor
from tkinter import *
from tkinter import ttk
from tkinter import filedialog


#хуячу базу данных цру
connection = sqlite3.connect('data.db')
cursor: Cursor = connection.cursor()
cursor.execute(" CREATE TABLE IF NOT EXISTS users(\n"
                   "        spin INT,\n"
                   "        cash BIGINT,\n"
                   "        zanos INT,\n"
                   "        ns INT\n"
                   "    )")
connection.commit()

#spin
def asino():
    for row in cursor.execute("SELECT spin, zanos, cash, ns FROM users"):
        spin = row[0]
        win = row[1]
    img1 = random.choice(listslots)
    img2 = random.choice(listslots)
    img3 = random.choice(listslots)
    if img1 == img2 and img1 == img3:
        cursor.execute("UPDATE users SET zanos = zanos + 1")
        connection.commit()

        totalwin.configure(text= 'Всего заносиков:' + ' ' + str(win))

    label1 = Label(image= img1)
    label1.place(relx= 0.37, rely= 0.2)
    label2 = Label(image= img2)
    label2.place(relx= 0.09,rely=0.2)
    label3 = Label(image= img3)
    label3.place(relx= 0.65, rely= 0.2)
    cursor.execute("UPDATE users SET spin = spin + 1")
    connection.commit()
    totalspin.configure(text= 'Всего спинов:' + '  ' + str(spin))
    if win >= 70:
        nsfw_check(True)
 

#view_symbol
def symbol():
    new_window = Toplevel(root)
    new_window.title('symbols')
    new_window['bg'] = 'gray14'
    new_window.geometry('700x400')
    new_window.resizable(width = False, height = False)
    label1 = Label(new_window, image = neko1)
    label1.place(relx = 0.1, rely = 0.2)
    label1 = Label(new_window, image = neko2)
    label1.place(relx = 0.4, rely = 0.2)
    label1 = Label(new_window, image = neko3)
    label1.place(relx = 0.7, rely = 0.2)

    label1_low = Label(new_window, text = 'ну короче \n Я не придумал \n Ничего', fg='white')
    label1_low['bg'] = 'gray14'
    label1_low.place(relx = 0.1, rely = 0.51)

    label2_low = Label(new_window, text = 'ну короче \n Я не придумал \n Ничего', fg='white')
    label2_low['bg'] = 'gray14'
    label2_low.place(relx = 0.4, rely = 0.51)

    label3_low = Label(new_window, text = 'ну короче \n Я не придумал \n Ничего', fg='white')
    label3_low['bg'] = 'gray14'
    label3_low.place(relx = 0.7, rely = 0.51)

#nsfw_func
def nsfw():
    #nsfw_award
    nsfw_window = Toplevel(root)
    nsfw_window.title('УБЕРИ МАМУ ОТ МОНИТОРА!!!!!!')
    nsfw_window['bg'] = 'gray14'
    nsfw_window.geometry('1122x799')
    nsfw_window.resizable(width = True, height = True)
    image1 = PhotoImage(file= random_nsfw_img())
    label = Label(nsfw_window, image= image1)
    nsfw_window.photo = image1
    label.place(relx = 0, rely = 0)



#main_menu
root = Tk()
root['bg'] = 'gray14'
root.title('спидорс.beta')
root.geometry('400x700')
root.resizable(width = False, height = False)

#счетчик
for row in cursor.execute("SELECT spin, zanos, ns, cash FROM users"):
    spin = row[0]
    win = row[1]
totalspin = Label(root, text= 'Всего спинов:'+ '  ' + str(spin),  background = 'gray14', foreground= 'white', font = 'arial 15')
totalspin.place(relx= 0.09, rely= 0.4)


totalwin = Label(root,text= "Всего заносиков:" + ' ' + str(win), background= 'gray14', foreground= 'white', font = 'arial 15')
totalwin.place(relx = 0.09, rely = 0.5)

#buttonimg
img = PhotoImage(file = 'image/222.png')
img = img.subsample(6, 6)
img_wtf = PhotoImage(file = 'image/wtf!.png')
img_wtf = img_wtf.subsample(2, 2)
img_nsfw = PhotoImage(file = 'image/nsfw.png')
img_nsfw = img_nsfw.subsample(2, 2)

#slots_img
neko1 = PhotoImage(file= 'image/neko1.png')
neko2 = PhotoImage(file= 'image/neko2.png')
neko3 = PhotoImage(file= 'image/neko3.png')
listslots = [neko1, neko2, neko3]



#nsfw
nsfwFlag = False
nsfw = Button(root, image =img_nsfw , command=nsfw)
nsfw['border'] = 0
nsfw['bg'] = 'gray14'

def random_nsfw_img():
    nsfw_award_list = ['nsfw/he2.png','nsfw/he3.png','nsfw/he4.png','nsfw/he5.png','nsfw/he6.png','nsfw/he7.png','nsfw/he8.png','nsfw/he9.png','nsfw/he10.png','nsfw/he11.png']
    nsfw_award_img = random.choices(nsfw_award_list, k = 10)[0]
    return str(nsfw_award_img)


def nsfw_check(Value):
  nsfwFlag = Value
  if (nsfwFlag):
    img_nsfw = PhotoImage(file = 'image/nsfw.png')
    img_nsfw = img_nsfw.subsample(2, 2)
    global nsfw
    nsfw.pack(ipadx = 0, ipady = 0, expand = 1)
    nsfw.place(x = 25, y = 540)
        
#button_spin
spin = Button(root, image = img, command = asino, borderwidth = 0)
spin['border'] = 0
spin['bg'] = 'gray14'
spin.pack(ipadx = 0, ipady = 0, expand = 1)
spin.place(x = 100, y = 400)

#button_symbol
symb = Button(root, image = img_wtf ,command = symbol, borderwidth = 0)
symb['border'] = 0
symb['bg'] = 'gray14'
symb.pack(anchor = S, ipadx = 0, ipady = 0, expand = 1)
symb.place(x = 275, y = 540)



root.mainloop()