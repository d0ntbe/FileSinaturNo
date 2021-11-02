from zipfile import *
import os
import shutil
import Tkinter
import tkFileDialog
from Tkinter import *
import binascii


def Searching():
    fn = tkFileDialog.Open(tk, filetypes=[('*all files,', '.*')]).show()
    fl = open(fn, 'rb')

    file = fl
    text = file.read()
    text2 = file.read()
    dlina = text.__len__()

    if dlina < 305101690:
        textbox.insert(END, 'Size of file is ' + str(dlina) + " - " + hex(
            dlina) + '. \n So, I will work not very long! About 1 min...')
    else:
        textbox.insert(END, 'Size of file is big or equal = ' + str(
            dlina) + '. So, I will work more than 2-3 min...')

    if Checkbox1.get() == 1:


        rezultPK = ""
        rezultRar = ""
        rezultGZ = ""
        rezultTar = ""

        index = 0
        tobig = 0
     
        if Checkbox1.get() == 1:

            while index != -1:
                index = text.find('PK')
                rezultPK += str(index) + "\n"
                text2 = text.replace('PK', 'gg', 1)
                index = text2.find('PK')
                rezultPK += str(index) + "\n"
                text = text2.replace('PK', 'gg', 1)

                tobig = tobig + 1
             
            textbox.insert(END, '\n           PK files may be there: \n')
            textbox.insert(END, rezultPK)
            textbox.insert(END,'++++++ PK ++++++++END++++++++++ PK +++++++++\n')

            index = 0

            while index != -1:
                index = text.find('Rar')
                rezultRar += str(index) + "\n"
                text2 = text.replace('Rar', 'ggg', 1)
                index = text2.find('Rar')
                rezultRar += str(index) + "\n"
                text = text2.replace('Rar', 'ggg', 1)

                tobig = tobig + 1
            
            textbox.insert(END, '\n           Rar files may be there: \n')
            textbox.insert(END,rezultRar)
            textbox.insert(END, '+++++++ Rar ++++++++END+++++++++ Rar ++++++++++')

            index = 0

            while index != -1:
                index = text.find('\x1f\x8b\x08')
                rezultGZ += str(index) + "\n"
                text2 = text.replace('\x1f\x8b\x08', '\xff\xff\xff', 1)
                index = text2.find('\x1f\x8b\x08')
                rezultGZ += str(index) + "\n"
                text = text2.replace('\x1f\x8b\x08', '\xff\xff\xff', 1)

                tobig = tobig + 1
           
            textbox.insert(END, '\n           GZip files may be there: \n')
            textbox.insert(END, rezultGZ)
            textbox.insert(END, '+++++++ GZ ++++++++END+++++++++ GZ ++++++++++')

            index = 0

            while index != -1:
                index = text.find('.tar')
                rezultTar += str(index) + "\n"
                text2 = text.replace('.tar', 'ggwp', 1)
                index = text2.find('.tar')
                rezultTar += str(index) + "\n"
                text = text2.replace('.tar', 'ggwp', 1)

                tobig = tobig + 1
             
            textbox.insert(END, '\n           Tar files may be there: \n')
            textbox.insert(END, rezultTar)
            textbox.insert(END, '+++++++ TGZ ++++++++END+++++++++ TGZ ++++++++++')
    if Checkbox2.get() == 1:
        rezult7z = ""
        rezultARJ = ""
        rezultustar = ""

        index = 0
        tobig = 0

        while index != -1:
            index = text.find('7z')
            rezult7z += str(index) + "\n"
            text2 = text.replace('7z', 'gg', 1)
            index = text2.find('7z')
            rezult7z += str(index) + "\n"
            text = text2.replace('7z', 'gg', 1)

            tobig = tobig + 1
       
        textbox.insert(END, '\n           7Z files may be there: \n')
        textbox.insert(END, rezult7z)
        textbox.insert(END, '++++++ 7Z ++++++++END++++++++++ 7Z +++++++++\n')

        index = 0

        while index != -1:
            index = text.find('arj')
            rezultARJ += str(index) + "\n"
            text2 = text.replace('arj', 'ggg', 1)
            index = text2.find('arj')
            rezultARJ += str(index) + "\n"
            text = text2.replace('arj', 'ggg', 1)

            tobig = tobig + 1
       
        textbox.insert(END, '\n           arj files may be there: \n')
        textbox.insert(END, rezultARJ)
        textbox.insert(END, '++++++ ARJ ++++++++END++++++++++ ARJ +++++++++')

        index = 0

        while index != -1:
            index = text.find('ustar')
            rezultustar += str(index) + "\n"
            text2 = text.replace('ustar', 'ggggg', 1)
            index = text2.find('ustar')
            rezultustar += str(index) + "\n"
            text = text2.replace('ustar', 'ggggg', 1)

            tobig = tobig + 1
          
        textbox.insert(END, '\n           ustar files may be there: \n')
        textbox.insert(END, rezultustar)
        textbox.insert(END, '++++++ ustar ++++++++END++++++++++ ustar +++++++++')
    if Checkbox3.get() == 1:
        rezultDES = ""
        rezultAES = ""
       
        index = 0
        tobig = 0

        textbox.insert(END, '\n Now, looking for AES consts....\n ')
        textbox.insert(END, '\n        ++++++++ AES tables ++++++++\n ')

        while index != -1:
            index = text.find('\x63\x7c\x77\x7b')
            rezultAES += str(index) + "\n"
            text2 = text.replace('\x63\x7c\x77\x7b', 'ggwp', 1)
            index = text2.find('\x63\x7c\x77\x7b')
            rezultAES += str(index) + "\n"
            text = text2.replace('\x63\x7c\x77\x7b', 'ggwp', 1)

            tobig = tobig + 1
          

        textbox.insert(END, '\n           AES may be there: \n')
        textbox.insert(END, rezultAES)
        textbox.insert(END, '++++++ AES ++++++++END++++++++++ AES +++++++++\n')

        index = 0
        textbox.insert(END, '\n        ++++++++ DES tables ++++++++\n ')
        while index != -1:
            index = text.find('\x00\x82\x02\x00')
            rezultDES += str(index) + "\n"
            text2 = text.replace('\x00\x82\x02\x00', 'ggwp', 1)
            index = text2.find('\x00\x82\x02\x00')
            rezultDES += str(index) + "\n"
            text = text2.replace('\x00\x82\x02\x00', 'ggwp', 1)

            tobig = tobig + 1
            if tobig > 200:
                textbox.insert(END,
                               "ERROR! There are a lot of matches, i will do it toooooo loooong.... ")

        textbox.insert(END, '\n           Des tables are there: \n')
        textbox.insert(END, rezultDES)
        textbox.insert(END, '++++++ DES ++++++++END++++++++++ DES +++++++++')
    if Checkbox4.get() == 1:
        rezultHASH = ""
       
        index = 0
        tobig = 0

        textbox.insert(END, '\n Now, looking for HASH consts....\n ')
        textbox.insert(END, '\n        ++++++++ MD5,SHA ++++++++\n ')

        while index != -1:
            index = text.find('\x6e\xd9\xeb\xa1')
            rezultHASH += str(index) + "\n"
            text2 = text.replace('\x6e\xd9\xeb\xa1', 'ggwp', 1)
            index = text2.find('\x6e\xd9\xeb\xa1')
            rezultHASH += str(index) + "\n"
            text = text2.replace('\x6e\xd9\xeb\xa1', 'ggwp', 1)

            tobig = tobig + 1
          

        textbox.insert(END, '\n           HASH consts may be there: \n')
        textbox.insert(END, rezultHASH)
        textbox.insert(END, '++++++ HASH ++++++++END++++++++++ HASH +++++++++\n')
    if Checkbox5.get() == 1:
        rezultCRC = ""

        index = 0
        tobig = 0

        textbox.insert(END, '\n Now, looking for CRC consts....\n ')
        textbox.insert(END, '\n        ++++++++ CRC ++++++++\n ')

        while index != -1:
            index = text.find('\x00\x77\xee\x99')
            rezultCRC += str(index) + "\n"
            text2 = text.replace('\x00\x77\xee\x99', 'ggwp', 1)
            index = text2.find('\x00\x77\xee\x99')
            rezultCRC += str(index) + "\n"
            text = text2.replace('\x00\x77\xee\x99', 'ggwp', 1)

            tobig = tobig + 1
         
        textbox.insert(END, '\n           CRC consts may be there: \n')
        textbox.insert(END, rezultCRC)
        textbox.insert(END, '++++++ CRC ++++++++END++++++++++ CRC +++++++++\n')
    if Checkbox6.get() == 1:
        rezultZi = ""

        index = 0
        tobig = 0

        textbox.insert(END, '\n Now, looking for Adler consts....\n ')
        textbox.insert(END, '\n  ++++++++zip Adler algs consts ++++++++\n ')

        while index != -1:
            index = text.find('\x61\x00\x81\x00\xc1')
            rezultZi += str(index) + "\n"
            text2 = text.replace('\x61\x00\x81\x00\xc1', 'ggwps', 1)
            index = text2.find('\x61\x00\x81\x00\xc1')
            rezultZi += str(index) + "\n"
            text = text2.replace('\x61\x00\x81\x00\xc1', 'ggwps', 1)

            tobig = tobig + 1
         
        textbox.insert(END, '\n           Adler consts may be there: \n')
        textbox.insert(END, rezultZi)
        textbox.insert(END, '++++++ Adler ++++++++END++++++++++ Adler +++++++++\n')


tk = Tkinter.Tk()

panelFrame = Frame(tk,height = 15, width = 20, bg = 'gray')
textFrame = Frame(tk,height = 15, width = 20, bg = 'red')

panelFrame.pack(side = 'top', fill = 'x')
textFrame.pack(side = 'bottom', fill = 'both', expand = 1)

textbox = Text(textFrame,font='Courier 10', wrap = 'word')
scrollbar = Scrollbar(textFrame)

scrollbar['command'] = textbox.yview
textbox['yscrollcommand'] = scrollbar.set

textbox.pack(side = 'left', fill = 'both', expand = 1)
scrollbar.pack(side = 'right', fill = 'y')

#CheckBoxes

Checkbox1 = IntVar()
Checkbox2 = IntVar()
Checkbox3 = IntVar()
Checkbox4 = IntVar()
Checkbox5 = IntVar()
Checkbox6 = IntVar()

C1 = Checkbutton(tk,text = "PK,RAR,ZIP,GZ,TGZ", variable = Checkbox1, onvalue = 1, offvalue = 0, height = 5, width = 20 )
C2 = Checkbutton(tk,text = "7z,arj,ustar", variable = Checkbox2,onvalue = 1, offvalue = 0, height = 5, width = 20 )
C3 = Checkbutton(tk,text = "AES,DES", variable = Checkbox3,onvalue = 1, offvalue = 0, height = 5, width = 20 )
C4 = Checkbutton(tk,text = "MD5,SHA", variable = Checkbox4,onvalue = 1, offvalue = 0, height = 5, width = 20 )
C5 = Checkbutton(tk,text = "CRC", variable = Checkbox5,onvalue = 1, offvalue = 0, height = 5, width = 20 )
C6 = Checkbutton(tk,text = "Mark Adler", variable = Checkbox6,onvalue = 1, offvalue = 0, height = 5, width = 20 )


C1.pack(side = LEFT)
C2.pack(side = LEFT)
C3.pack(side = LEFT)
C4.pack(side = LEFT)
C5.pack(side = LEFT)
C6.pack(side = LEFT)

#Buttons

global fl

B1 = Tkinter.Button(tk,text = "SEARCH", command = Searching)
B1.pack(side = RIGHT)
tk.mainloop()



