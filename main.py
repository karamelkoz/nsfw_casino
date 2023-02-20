
#liblary
import random
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
#spin
def asino():
    global win
    img1 = random.choice(listslots)
    img2 = random.choice(listslots)
    img3 = random.choice(listslots)
    if img1 == img2 and img1 == img3:
        win += 1

        totalwin.configure(text= 'Всего заносиков:' + ' ' + str(win))

    label1 = Label(image= img1)
    label1.place(relx= 0.37, rely= 0.2)
    label2 = Label(image= img2)
    label2.place(relx= 0.09,rely=0.2)
    label3 = Label(image= img3)
    label3.place(relx= 0.65, rely= 0.2)
    global quantityspin
    quantityspin += 1
    f = open('config.txt','r+')
    totalspin.configure(text= 'Всего спинов:' + '  ' + str(quantityspin))

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




#main_menu
root = Tk()
root['bg'] = 'gray14'
root.title('спидорс.beta')
root.geometry('400x700')
root.resizable(width = False, height = False)


#счетчик
quantityspin = 0 
totalspin = Label(root, text= 'Всего спинов',  background = 'gray14', foreground= 'white', font = 'arial 15')
totalspin.place(relx= 0.09, rely= 0.4)

win = 1
totalwin = Label(root,text= "Всего заносиков" + ' ' + str(win), background= 'gray14', foreground= 'white', font = 'arial 15')
totalwin.place(relx = 0.09, rely = 0.5)

#buttonimg
img = PhotoImage(file = '222.png')
img = img.subsample(6, 6)
img_wtf = PhotoImage(file = 'wtf!.png')
img_wtf = img_wtf.subsample(2, 2)

#slots_img
neko1 = PhotoImage(file= 'neko1.png')
neko2 = PhotoImage(file= 'neko2.png')
neko3 = PhotoImage(file= 'neko3.png')
neko3 = PhotoImage(file= 'neko3.png')
neko4 = PhotoImage(file= 'neko3.png')

listslots = [neko1, neko2, neko3]


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