##LABORATORIO DE COMPORTAMIENTO SOCIAL E INTELIGENCIA ARTIFICIAL
#Laurent Avila Chauvet / Julio 2020
#DEMO - Reto IBM @Talent-Home

#Custom
import TWalden as Tw
import LcsiaIBM as Li

#Default
import tkinter
from tkinter import messagebox

#Variables

global Canvas_X, Canvas_Y
Canvas_X = 500
Canvas_Y = 700

global RGB_White, RGB_Black, Font_1
RGB_White = (255,255,255)
RGB_Black = (0,0,0)
Font_1 = 'Sans'

global Rec
Rec = 0

def Main():
    
    Text_1 = Li.Sp2Txt('Test')
    
    def BntRec():
        Li.RecSp(5,'Test')
    
    Main = tkinter.Tk()
    Main.geometry(str(Canvas_X)+'x'+str(Canvas_Y)+'+10+10')
    Main.title('LCSIA-IBM@Talent')
    Main.config(bg = Tw.Rgb(RGB_White))
    Image_Main_1 = Tw.CImage(Main,RGB_White,0,0,1,'Image_1.png')
    
#    Bnt_Main_1 = Tw.CBnt(Main,1,RGB_White,RGB_Black,
#                      RGB_White,RGB_White,
#                      Font_1,30,280,600,
#                      'Rec',
#                      BntRec)
    
    Text_Read = Tw.CStr(Main,RGB_White,
                        RGB_Black,
                        Font_1,12,10,30,
                        Text_1)
    Main.mainloop() 
    
Main()