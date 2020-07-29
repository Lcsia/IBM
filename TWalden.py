# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 16:33:41 2019

@author: Laurent
"""
import tkinter 
import csv
import os
import os.path
import shelve
from PIL import Image, ImageTk

def Rgb(RGB):
    return "#%02x%02x%02x" % RGB 

def CStr(Can,BG,FG,FT,Size,X,Y,txt):
    Lbl_Str = tkinter.Label(Can, 
                            bg=Rgb(BG), fg=Rgb(FG),
                            text = txt)
    Lbl_Str.config(font = (FT,Size))
    Lbl_Str.place(x=X, y =Y)
    return Lbl_Str

def CBox(Can,W,H,FT,Size,X,Y):
    Lbl_Box = tkinter.Text(Can, width = W, height = H)
    Lbl_Box.config(font = (FT,Size))
    Lbl_Box.place(x=X, y =Y)
    return Lbl_Box

def CEntry(Can,W,C,FT,Size,X,Y):
    Lbl_Entry = tkinter.Entry(Can, width = W, show = C)
    Lbl_Entry.config(font = (FT,Size))
    Lbl_Entry.place(x=X, y =Y)
    return Lbl_Entry

def CImage(Can,BG,X,Y,size,img):
    img = Image.open(img)
    size_1 = img.size
    width = int(size_1[0]*size)
    height = int(size_1[1]*size)
    img = img.resize((width, height),Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)
    Lbl_Image = tkinter.Label(Can, bg = Rgb(BG), image = img)
    Lbl_Image.place(x=X, y=Y) 
    return img

def CBnt(Can,BD,BG,FG,BA,FA,FT,Size,X,Y,txt,C):
    Lbl_Bnt = tkinter.Button(Can, bd=BD, bg = Rgb(BG), fg = Rgb(FG),
                             activebackground=Rgb(BA), highlightbackground=Rgb(FA),
                             text = txt, command = C)
    Lbl_Bnt.config(font = (FT,Size))
    Lbl_Bnt.place(x=X, y = Y)
    return Lbl_Bnt

def StartTask(Task): 
        os.startfile(Task.encode('unicode_escape').decode().replace('\\\\', '\\'))

def ReadCsv1(Dir):
    A = []
    with open(Dir) as csvDataFile:
        csvReader = csv.reader(csvDataFile)
        for row in csvReader:
            A.append(row[0])
    return A
    
def ReadCsv2(Dir):
    A = []
    B = []
    with open(Dir) as csvDataFile:
        csvReader = csv.reader(csvDataFile)
        for row in csvReader:
            A.append(row[0])
            B.append(row[1])
    return A,B

def TempOpen(Var):
    Var -= 1
    TVarA, TVarB = ReadCsv2('C:/LCApp/Config/Temp.csv')
    return TVarB[Var]
    
def TempSave(Var,Data):
    Var -= 1
    if Var == -1:
        TVarA, TVarB = ReadCsv2('C:/LCApp/Config/Temp.csv')
        TempT = open('Temp.csv','w')
        for i in range(0,len(TVarA)):
            TempT.write(str(TVarA[i]) + ',' + str(TVarB[i])  + '\n')
        TempT.close()
    else:
        TVarA, TVarB = ReadCsv2('C:/LCApp/Config/Temp.csv')
        TVarB[Var] = str(Data)
        TempT = open('Temp.csv','w')
        for i in range(0,len(TVarA)):
            TempT.write(str(TVarA[i]) + ',' + str(TVarB[i])  + '\n')
        TempT.close()
        
def PSave(Dir,Name,Data):
    Name = Dir + Name + '.csv'
    TempT = open(Name,'w')
    for i in range(0,len(Data)):
        TempT.write(str(Data[i]) + '\n')
    TempT.close()


    
    
    
    
    
    
    