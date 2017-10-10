import numpy as np
import cv2
import tkinter as tk
from math import *
from PIL import Image, ImageTk
import random

def librasmais(event):
    root.destroy()
    #Set up GUI
    window = tk.Tk()  #Makes main window
    window.wm_title("LibrasMais")
    window.iconbitmap('libras2.ico')
    window.wm_state('zoomed')

    window.config(background="#004C99")

    #Graphics window
    frame2 = tk.Frame(window,bg="#004C99")
    frame2.pack()

    tk.Label(frame2,text='\n\n\n',bg="#004C99").grid(columnspan=3,row=0)
    
    #Capture video frames
    lmain = tk.Label(frame2)
    lmain.grid(row=1, columnspan=3, sticky='')
    cap = cv2.VideoCapture(0)
    
    def show_frame():
        _, frame = cap.read()

        cv2.rectangle(frame,(400,400),(100,100),(0,255,0),0)
        crop_img = frame[100:400, 100:400]
        grey = cv2.cvtColor(crop_img, cv2.COLOR_BGR2GRAY)
        value = (35, 35)
        blurred = cv2.GaussianBlur(grey, value, 0)
        _, thresh1 = cv2.threshold(blurred, 127, 255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
        image, contours, hierarchy = cv2.findContours(thresh1.copy(),cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
        max_area = -1
        for i in range(len(contours)):
            cnt=contours[i]
            area = cv2.contourArea(cnt)
            if(area>max_area):
                max_area=area
                ci=i
        cnt=contours[ci]
        x,y,w,h = cv2.boundingRect(cnt)
        cv2.rectangle(crop_img,(x,y),(x+w,y+h),(0,0,255),0)
        hull = cv2.convexHull(cnt)
        drawing = np.zeros(crop_img.shape,np.uint8)
        cv2.drawContours(drawing,[cnt],0,(0,255,0),0)
        cv2.drawContours(drawing,[hull],0,(0,0,255),0)
        hull = cv2.convexHull(cnt,returnPoints = False)
        defects = cv2.convexityDefects(cnt,hull)
        cv2.drawContours(thresh1, contours, -1, (0,255,0), 3)
        for i in range(defects.shape[0]):
            s,e,f,d = defects[i,0]
            start = tuple(cnt[s][0])
            end = tuple(cnt[e][0])
            far = tuple(cnt[f][0])
            a = sqrt((end[0] - start[0])**2 + (end[1] - start[1])**2)
            b = sqrt((far[0] - start[0])**2 + (far[1] - start[1])**2)
            c = sqrt((end[0] - far[0])**2 + (end[1] - far[1])**2)
            angle = acos((b**2 + c**2 - a**2)/(2*b*c)) * 57
            if angle <= 90:
                cv2.circle(crop_img,far,1,[0,0,255],-1)
            dist = cv2.pointPolygonTest(cnt,far,True)
            cv2.line(crop_img,start,end,[0,255,0],2)
            cv2.circle(crop_img,far,5,[0,0,255],-1)
        
        frame = cv2.flip(frame, 1)
        cv2image = cv2.cvtColor(crop_img, cv2.COLOR_BGR2RGBA)
        img = Image.fromarray(cv2image)
        imgtk = ImageTk.PhotoImage(image=img)
        lmain.imgtk = imgtk
        lmain.configure(image=imgtk)
        lmain.after(5, show_frame)

    tk.Label(frame2,text='\n\n\n',bg="#004C99").grid(columnspan=3,row=2)

    tk.Label(frame2,text=' Escolha o gesto que deseja treinar e aprender! \n ',font="Roboto",bg="#004C99",fg='white').grid(column=0,row=3, sticky='')
    tk.Label(frame2,text=' Fotografe sua mão e aguarde o resultado! \nSerá que você acertou?',font="Roboto",bg="#004C99",fg='white').grid(column=1,row=3, sticky='')
    tk.Label(frame2,text=' Quer conferir quais sinais você já acertou? \nConfira abaixo!',font="Roboto",bg="#004C99",fg='white').grid(column=2,row=3, sticky='')

    tk.Label(frame2,text='\n',bg="#004C99").grid(columnspan=3,row=4)

    rand=0
    def escolhe(event):
        rand = int(random.random())
        return rand    
    
    escolhe_botao = tk.Button(frame2, text="Escolher gesto", padx=3, pady=2, font="Roboto")
    escolhe_botao.bind('<ButtonRelease-1>',escolhe)
    escolhe_botao.grid(column=0, row=5, sticky='') 

    pratica_botao = tk.Button(frame2, text='Fotografar', padx=3, pady=2, font="Roboto")
    ##pratica_botao.bind('<ButtonRelease-1>',pratica)
    pratica_botao.grid(column=1, row=5, sticky='') 

    acertos_botao = tk.Button(frame2, text='Acertos', padx=3, pady=2, font="Roboto")
    ##acertos_botao.bind('<ButtonRelease-1>',acertos)
    acertos_botao.grid(column=2, row=5, sticky='')

    tk.Label(frame2,text=rand,font="Roboto",bg="#004C99",fg='white').grid(column=0,row=6, sticky='')

    show_frame()  #Display 2
    window.mainloop()  #Starts GUI


def pratica(event):
    root.destroy()

    pratica_janela = tk.Tk()
    pratica_janela.title('LibrasMais')
    pratica_janela.iconbitmap('libras2.ico')
    pratica_janela.config(background="#004C99")

    prat=tk.Frame(pratica_janela,bg='#004C99')
    prat.pack()

    def libra(event):
    
        show_libra = tk.PhotoImage(file='images/%s.png' % tk.Button['text'])
        show_libra_label = tk.Label(prat, image=show_libra,bg="#004C99")
        show_libra_label.grid(columnspan=10, row=6)

        tk.Label(prat,text='\n',bg="#004C99").grid(columnspan=10,row=7)
    
    clique = "\n\n\n    Clique em uma letra ou número:   \n\n\n"
    tk.Label(prat,text=clique,font='Roboto',bg="#004C99",fg='white').grid(columnspan=10,row=0,sticky='')

    but0 = tk.Button(prat,font='Roboto',padx=2,pady=2,text='0')
    but0.bind('<ButtonRelease-1>',libra)
    but0.grid(row=1,sticky='',column=0)

    but1 = tk.Button(prat,font='Roboto',padx=2,pady=2,text='1')
    but1.bind('<ButtonRelease-1>',libra)
    but1.grid(row=1,sticky='',column=1)

    but2 = tk.Button(prat,font='Roboto',padx=2,pady=2,text='2')
    but2.bind('<ButtonRelease-1>',libra)
    but2.grid(row=1,sticky='',column=2)

    but3 = tk.Button(prat,font='Roboto',padx=2,pady=2,text='3')
    but3.bind('<ButtonRelease-1>',libra)
    but3.grid(row=1,sticky='',column=3)

    but4 = tk.Button(prat,font='Roboto',padx=2,pady=2,text='4')
    but4.bind('<ButtonRelease-1>',libra)
    but4.grid(row=1,sticky='',column=4)

    but5 = tk.Button(prat,font='Roboto',padx=2,pady=2,text='5')
    but5.bind('<ButtonRelease-1>',libra)
    but5.grid(row=1,sticky='',column=5)

    but6 = tk.Button(prat,font='Roboto',padx=2,pady=2,text='6')
    but6.bind('<ButtonRelease-1>',libra)
    but6.grid(row=1,sticky='',column=6)

    but7 = tk.Button(prat,font='Roboto',padx=2,pady=2,text='7')
    but7.bind('<ButtonRelease-1>',libra)
    but7.grid(row=1,sticky='',column=7)

    but8 = tk.Button(prat,font='Roboto',padx=2,pady=2,text='8')
    but8.bind('<ButtonRelease-1>',libra)
    but8.grid(row=1,sticky='',column=8)

    but9 = tk.Button(prat,font='Roboto',padx=2,pady=2,text='9')
    but9.bind('<ButtonRelease-1>',libra)
    but9.grid(row=1,sticky='',column=9)

    butA = tk.Button(prat,font='Roboto',padx=2,pady=2,text='A')
    butA.bind('<ButtonRelease-1>',libra)
    butA.grid(row=2,sticky='',column=0)

    butB = tk.Button(prat,font='Roboto',padx=2,pady=2,text='B')
    butB.bind('<ButtonRelease-1>',libra)
    butB.grid(row=2,sticky='',column=1)

    butC = tk.Button(prat,font='Roboto',padx=2,pady=2,text='C')
    butC.bind('<ButtonRelease-1>',libra)
    butC.grid(row=2,sticky='',column=2)

    butD = tk.Button(prat,font='Roboto',padx=2,pady=2,text='D')
    butD.bind('<ButtonRelease-1>',libra)
    butD.grid(row=2,sticky='',column=3)

    butE = tk.Button(prat,font='Roboto',padx=2,pady=2,text='E')
    butE.bind('<ButtonRelease-1>',libra)
    butE.grid(row=2,sticky='',column=4)

    butF = tk.Button(prat,font='Roboto',padx=2,pady=2,text='F')
    butF.bind('<ButtonRelease-1>',libra)
    butF.grid(row=2,sticky='',column=5)

    butG = tk.Button(prat,font='Roboto',padx=2,pady=2,text='G')
    butG.bind('<ButtonRelease-1>',libra)
    butG.grid(row=2,sticky='',column=6)

    butH = tk.Button(prat,font='Roboto',padx=2,pady=2,text='H')
    butH.bind('<ButtonRelease-1>',libra)
    butH.grid(row=2,sticky='',column=7)

    butI = tk.Button(prat,font='Roboto',padx=2,pady=2,text='I')
    butI.bind('<ButtonRelease-1>',libra)
    butI.grid(row=2,sticky='',column=8)

    butJ = tk.Button(prat,font='Roboto',padx=2,pady=2,text='J')
    butJ.bind('<ButtonRelease-1>',libra)
    butJ.grid(row=2,sticky='',column=9)

    butK = tk.Button(prat,font='Roboto',padx=2,pady=2,text='K')
    butK.bind('<ButtonRelease-1>',libra)
    butK.grid(row=3,sticky='',column=0)

    butL = tk.Button(prat,font='Roboto',padx=2,pady=2,text='L')
    butL.bind('<ButtonRelease-1>',libra)
    butL.grid(row=3,sticky='',column=1)

    butM = tk.Button(prat,font='Roboto',padx=2,pady=2,text='M')
    butM.bind('<ButtonRelease-1>',libra)
    butM.grid(row=3,sticky='',column=2)

    butN = tk.Button(prat,font='Roboto',padx=2,pady=2,text='N')
    butN.bind('<ButtonRelease-1>',libra)
    butN.grid(row=3,sticky='',column=3)

    butO = tk.Button(prat,font='Roboto',padx=2,pady=2,text='O')
    butO.bind('<ButtonRelease-1>',libra)
    butO.grid(row=3,sticky='',column=4)

    butP = tk.Button(prat,font='Roboto',padx=2,pady=2,text='P')
    butP.bind('<ButtonRelease-1>',libra)
    butP.grid(row=3,sticky='',column=5)

    butQ = tk.Button(prat,font='Roboto',padx=2,pady=2,text='Q')
    butQ.bind('<ButtonRelease-1>',libra)
    butQ.grid(row=3,sticky='',column=6)

    butR = tk.Button(prat,font='Roboto',padx=2,pady=2,text='R')
    butR.bind('<ButtonRelease-1>',libra)
    butR.grid(row=3,sticky='',column=7)

    butS = tk.Button(prat,font='Roboto',padx=2,pady=2,text='S')
    butS.bind('<ButtonRelease-1>',libra)
    butS.grid(row=3,sticky='',column=8)

    butT = tk.Button(prat,font='Roboto',padx=2,pady=2,text='T')
    butT.bind('<ButtonRelease-1>',libra)
    butT.grid(row=3,sticky='',column=9)

    butU = tk.Button(prat,font='Roboto',padx=2,pady=2,text='U')
    butU.bind('<ButtonRelease-1>',libra)
    butU.grid(row=4,sticky='',column=0)

    butV = tk.Button(prat,font='Roboto',padx=2,pady=2,text='V')
    butV.bind('<ButtonRelease-1>',libra)
    butV.grid(row=4,sticky='',column=1)

    butW = tk.Button(prat,font='Roboto',padx=2,pady=2,text='W')
    butW.bind('<ButtonRelease-1>',libra)
    butW.grid(row=4,sticky='',column=2)

    butX = tk.Button(prat,font='Roboto',padx=2,pady=2,text='X')
    butX.bind('<ButtonRelease-1>',libra)
    butX.grid(row=4,sticky='',column=3)

    butY = tk.Button(prat,font='Roboto',padx=2,pady=2,text='Y')
    butY.bind('<ButtonRelease-1>',libra)
    butY.grid(row=4,sticky='',column=4)

    butZ = tk.Button(prat,font='Roboto',padx=2,pady=2,text='Z')
    butZ.bind('<ButtonRelease-1>',libra)
    butZ.grid(row=4,sticky='',column=5)

    tk.Label(prat,text='\n',bg="#004C99").grid(columnspan=10,row=5)

    libra()
    pratica_janela.mainloop()


## Janela raiz ##

root=tk.Tk()
root.title('LibrasMais')

root_frame = tk.Frame(root,bg="#004C99")
root_frame.pack()
root.iconbitmap('libras2.ico')

bg_image = tk.PhotoImage(file='logo_libras.png')
bg_label = tk.Label(root_frame, image=bg_image,bg="#004C99")
bg_label.grid(columnspan=2, row=1)

texto = "Caso deseje praticar os gestos com a câmera, clique em \"Praticar\".\nSerá aberta uma nova janela. Recomendamos que:\n1. Esteja em um local bem iluminado.\n2. Procure um fundo de cor sólida (uma porta ou parede por exemplo).\n3. Posicione sua mão e aguarde o programa a reconhecer.\n4. Estamos prontos! Clique em \"Fotografar\" e aguarde o resultado.\n\n Caso deseje apenas ver como fazer os gestos, clique em \"Gestos\" logo abaixo. \nSerá aberta uma nova janela.\n\nPodemos começar?"
tk.Label(root_frame,text=texto,font="Roboto",bg="#004C99",fg='white').grid(columnspan=2,row=0)

praticar = tk.Button(root_frame,text='Praticar', padx=3,pady=3,font="Roboto")
praticar.bind('<ButtonRelease-1>',librasmais)
praticar.grid(column=0,row=2)

gestos = tk.Button(root_frame,text='Gestos', padx=3, pady=3, font='Roboto')
gestos.bind('<ButtonRelease-1>',pratica)
gestos.grid(column=1,row=2)

tk.Label(root_frame,text=' ',bg="#004C99").grid(columnspan=2,row=3)

root.resizable(0,0)
root.mainloop()
