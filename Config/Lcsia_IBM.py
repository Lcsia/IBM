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
Canvas_X = 900
Canvas_Y = 700

global RGB_White, RGB_Black, Font_1
RGB_White = (255,255,255)
RGB_Black = (0,0,0)
RGB_Red = (255,50,50)
RGB_Gray = (50,50,50)
RGB_Green = (50,255,50)
Font_1 = 'Sans'

global Name, Tresh, Mail, Cal1, Cal2, Cal3
Name = 'Laurent-ac'
Tresh = .8
Mail = ''
Cal1 = 0
Cal2 = 0
Cal3 = 0


def Main_0():
    
    def Next():
        global Name
        Name = Entry_Main_1.get()
        Main.destroy()
        Main_2()
    
    Main = tkinter.Tk()
    Main.geometry(str(Canvas_X)+'x'+str(Canvas_Y)+'+10+10')
    Main.title('LCSIA-IBM@Talent')
    Main.config(bg = Tw.Rgb(RGB_White))
    Image_Main_1 = Tw.CImage(Main,RGB_White,220,-40,.6,'../Image/1.png')
    
    Bnt_Main_1 = Tw.CBnt(Main,1,RGB_White,RGB_Black,
                      RGB_White,RGB_White,
                      Font_1,20,300,620,
                      '              Log in               ',
                      Next)
    
    Text_Main_1 = Tw.CStr(Main,RGB_White,RGB_Black,Font_1,25,300,380,
                         'User:')
    Entry_Main_1 = Tw.CEntry(Main,18,'',Font_1,25,300,430)
    Entry_Main_1.insert(0, Name)
    
    Text_Main_2 = Tw.CStr(Main,RGB_White,RGB_Black,Font_1,25,300,500,
                         'Password:')
    Entry_Main_2 = Tw.CEntry(Main,18,'*',Font_1,25,300,550)
    Entry_Main_2.insert(0, '0000')
    
    

    Main.mainloop() 
    

def Main_2():
    
    def Rec():
         Bnt_Main_1.config(fg = Tw.Rgb(RGB_Black))
         Li.RecSp(floor(len(Text_1)/16),'Speech_1')
         Bnt_Main_1.config(fg = Tw.Rgb(RGB_Red))
         
    def Play():
        Li.Play('Speech_1')
        
    def Test():
        Text_2 = Li.Sp2Txt('Speech_1')
        Box_Main_1.config(state='normal',wrap='word')
        Box_Main_1.delete('1.0', 'end')
        Box_Main_1.insert('end',Text_2) 
        Box_Main_1.config(fg = Tw.Rgb(RGB_Gray))
        Box_Main_1.config(state='disabled',wrap='word')
        Test_p = Li.TxtCom(Text_1,Text_2)
        global Mail
        Mail += 'Reading = '+ str(Test_p) + '\n' + Text_2
#        Li.Mail(Name,Mail,'lcsia.test@gmail.com')
        if Test_p < Tresh:
            messagebox.showwarning('Text Match',  'Score\n' + str(Test_p) + '\n' + 'Try again!!!')
            Box_Main_1.config(state='normal',wrap='word')
            Box_Main_1.delete('1.0', 'end')
            Box_Main_1.insert('end',Text_1) 
            Box_Main_1.config(fg = Tw.Rgb(RGB_Black))
            Box_Main_1.config(state='disabled',wrap='word')
        else:
            messagebox.showinfo('Text Match',  'Score\n' + str(Test_p) + '\n' + 'Quizz Time!!!')
            Main.destroy()
            Main_3()
        

    
    Main = tkinter.Tk()
    Main.geometry(str(Canvas_X)+'x'+str(Canvas_Y)+'+10+10')
    Main.title('LCSIA-IBM@Talent')
    Main.config(bg = Tw.Rgb(RGB_White))
    
    Text_1 = Li.ReadTxt('../Teacher/Texto_1')
    Box_Main_1 = Tw.CBox(Main,60,18,Font_1,18,50,50)
    Box_Main_1.insert('end',Text_1) 
    Box_Main_1.config(state='disabled',wrap='word')

    
    Bnt_Main_1 = Tw.CBnt(Main,1,RGB_White,RGB_Red,
                      RGB_White,RGB_White,
                      Font_1,30,50,600,
                      '●',
                      Rec)
    
    Bnt_Main_2 = Tw.CBnt(Main,1,RGB_White,RGB_Black,
                      RGB_White,RGB_White,
                      Font_1,30,120,600,
                      '▶',
                      Play)
    
    Bnt_Main_2 = Tw.CBnt(Main,1,RGB_White,RGB_Black,
                      RGB_White,RGB_White,
                      Font_1,30,700,600,
                      'Enviar',
                      Test)

    Main.mainloop() 
    
def Main_3():
    
    def Rec_1():
         Box_Main_1_1.delete('1.0', 'end')
         Bnt_Main_1.config(fg = Tw.Rgb(RGB_Black))
         Li.RecSp2(4,'Quizz_1')
         Resp_1 = Li.Sp2Txt('Quizz_1')
         Box_Main_1_1.insert('end',Resp_1) 
         Box_Main_1_1.config(fg = Tw.Rgb(RGB_Gray))
         Bnt_Main_1.config(fg = Tw.Rgb(RGB_Red))
         Box_Main_1_2.delete('1.0', 'end')
         if Li.TestAsk(Quizz[1],Resp_1) >= Tresh:
             Box_Main_1_2.config(fg = Tw.Rgb(RGB_Green))
             Box_Main_1_2.insert('end','✔') 
         else:
             Box_Main_1_2.config(fg = Tw.Rgb(RGB_Red))
             Box_Main_1_2.insert('end','X')
         global Mail, Cal1
         Mail += '\n' + 'Response 1 = '+ str(Li.TestAsk(Quizz[1],Resp_1)) + '\n' + Resp_1
         Cal1 = Li.TestAsk(Quizz[1],Resp_1)
         
    def Play_1():
        Li.Play('Quizz_1')
    
    def Rec_2():
         Box_Main_2_1.delete('1.0', 'end')
         Bnt_Main_2.config(fg = Tw.Rgb(RGB_Black))
         Li.RecSp2(4,'Quizz_2')
         Resp_2 = Li.Sp2Txt('Quizz_2')
         Box_Main_2_1.insert('end',Resp_2) 
         Box_Main_2_1.config(fg = Tw.Rgb(RGB_Gray))
         Bnt_Main_2.config(fg = Tw.Rgb(RGB_Red))
         Box_Main_2_2.delete('1.0', 'end')
         if Li.TestAsk(Quizz[3],Resp_2) >= Tresh:
             Box_Main_2_2.config(fg = Tw.Rgb(RGB_Green))
             Box_Main_2_2.insert('end','✔') 
         else:
             Box_Main_2_2.config(fg = Tw.Rgb(RGB_Red))
             Box_Main_2_2.insert('end','X') 
         global Mail, Cal2
         Mail += '\n' + 'Response 2 = '+ str(Li.TestAsk(Quizz[3],Resp_2)) + '\n' + Resp_2
         Cal2 = Li.TestAsk(Quizz[3],Resp_2)
         
    def Play_2():
        Li.Play('Quizz_2')
    
    def Rec_3():
         Box_Main_3_1.delete('1.0', 'end')
         Bnt_Main_3.config(fg = Tw.Rgb(RGB_Black))
         Li.RecSp2(4,'Quizz_3')
         Resp_3 = Li.Sp2Txt('Quizz_3')
         Box_Main_3_1.insert('end',Resp_3) 
         Box_Main_3_1.config(fg = Tw.Rgb(RGB_Gray))
         Bnt_Main_3.config(fg = Tw.Rgb(RGB_Red))
         Box_Main_3_2.delete('1.0', 'end')
         if Li.TestAsk(Quizz[5],Resp_3) >= Tresh:
             Box_Main_3_2.config(fg = Tw.Rgb(RGB_Green))
             Box_Main_3_2.insert('end','✔') 
         else:
             Box_Main_3_2.config(fg = Tw.Rgb(RGB_Red))
             Box_Main_3_2.insert('end','X') 
         global Mail, Cal3
         Mail += '\n' + 'Response 3 = '+ str(Li.TestAsk(Quizz[5],Resp_3)) + '\n' + Resp_3
         Cal3 = Li.TestAsk(Quizz[5],Resp_3)
         
    def Play_3():
        Li.Play('Quizz_3')
        
    def Send():
        global Mail
        Mail = Li.Rep(Mail)
        Li.Mail(Name + ' = ' + str(round((Cal1 + Cal2 + Cal3)/3,3)),Mail,'lcsia.test@gmail.com')
        Main.destroy()
        print('ok')
    
    Main = tkinter.Tk()
    Main.geometry(str(Canvas_X)+'x'+str(Canvas_Y)+'+10+10')
    Main.title('LCSIA-IBM@Talent')
    Main.config(bg = Tw.Rgb(RGB_White))
    
    
    Quizz = Li.ReadTxt('../Teacher/Preguntas_1').split('-')
    
    Box_Main_1 = Tw.CBox(Main,60,18,Font_1,20,150,60)
    Box_Main_1.insert('end',Quizz[0]) 
    Box_Main_1.config(state='disabled',wrap='word',relief='flat')
    Box_Main_1_1 = Tw.CBox(Main,50,3,Font_1,20,50,120) 
    Box_Main_1_1.config(wrap='word')
    Box_Main_1_2 = Tw.CBox(Main,50,3,Font_1,20,830,150) 
    Box_Main_1_2.config(wrap='word', relief='flat')
    Box_Main_1_2.insert('end','') 
    
    Bnt_Main_1 = Tw.CBnt(Main,1,RGB_White,RGB_Red,
                      RGB_White,RGB_White,
                      Font_1,20,50,50,
                      '●',
                      Rec_1)
    Bnt_Main_1_1 = Tw.CBnt(Main,1,RGB_White,RGB_Black,
                      RGB_White,RGB_White,
                      Font_1,20,100,50,
                      '▶',
                      Play_1)
    
    Box_Main_2 = Tw.CBox(Main,60,18,Font_1,20,150,60+170)
    Box_Main_2.insert('end',Quizz[0+2]) 
    Box_Main_2.config(state='disabled',wrap='word',relief='flat')
    Box_Main_2_1 = Tw.CBox(Main,50,3,Font_1,20,50,120+200) 
    Box_Main_2_1.config(wrap='word')
    Box_Main_2_2 = Tw.CBox(Main,50,3,Font_1,20,830,150+200) 
    Box_Main_2_2.config(wrap='word', relief='flat')
    Box_Main_2_2.insert('end','') 
    
    Bnt_Main_2 = Tw.CBnt(Main,1,RGB_White,RGB_Red,
                      RGB_White,RGB_White,
                      Font_1,20,50,50+200,
                      '●',
                      Rec_2)
    Bnt_Main_2_1 = Tw.CBnt(Main,1,RGB_White,RGB_Black,
                      RGB_White,RGB_White,
                      Font_1,20,100,50+200,
                      '▶',
                      Play_2)
    
    Box_Main_3 = Tw.CBox(Main,60,18,Font_1,20,150,60+380)
    Box_Main_3.insert('end',Quizz[2+2]) 
    Box_Main_3.config(state='disabled',wrap='word',relief='flat')
    Box_Main_3_1 = Tw.CBox(Main,50,3,Font_1,20,50,120+400) 
    Box_Main_3_1.config(wrap='word')
    Box_Main_3_2 = Tw.CBox(Main,50,3,Font_1,20,830,150+400) 
    Box_Main_3_2.config(wrap='word', relief='flat')
    Box_Main_3_2.insert('end','') 
    
    Bnt_Main_3 = Tw.CBnt(Main,1,RGB_White,RGB_Red,
                      RGB_White,RGB_White,
                      Font_1,20,50,50+400,
                      '●',
                      Rec_3)
    Bnt_Main_3_1 = Tw.CBnt(Main,1,RGB_White,RGB_Black,
                      RGB_White,RGB_White,
                      Font_1,20,100,50+400,
                      '▶',
                      Play_3)
    
    Bnt_Main_4 = Tw.CBnt(Main,1,RGB_White,RGB_Black,
                  RGB_White,RGB_White,
                  Font_1,20,770,620,
                  'Enviar',
                  Send)
    
    
    Main.mainloop() 
    
Main_0()