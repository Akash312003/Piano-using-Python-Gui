from tkinter import *
import pygame


pygame.init()
root = Tk()


root.title("Music Box")
root.geometry("1352x700+0+0")
root.configure(background="white")


abc = Frame(root, bg="powder blue", bd=20, relief=RIDGE)
abc.grid()
abc1 = Frame(abc, bg="powder blue", bd=20, relief=RIDGE)
abc1.grid()
abc2 = Frame(abc, bg="powder blue", relief=RIDGE)
abc2.grid()
abc3 = Frame(abc, bg="powder blue", relief=RIDGE)
abc3.grid()

str = StringVar()
str.set("Just like Music")


def value_Cs():
    str.set("C#")
    sound = pygame.mixer.Sound("C:\\Users\\ganes\\OneDrive\\Desktop\\internpe\\Gui Piano\\Z_Music_Notes\\Music_Notes\\C_s.wav")
    sound.play()


def value_A():
    str.set("A")
    sound = pygame.mixer.Sound("C:\\Users\\ganes\\OneDrive\\Desktop\\internpe\\Gui Piano\\Z_Music_Notes\\Music_Notes\\A.wav")
    sound.play()

def value_B():
    str.set("B")
    sound = pygame.mixer.Sound("C:\\Users\\ganes\\OneDrive\\Desktop\\internpe\\Gui Piano\\Z_Music_Notes\\Music_Notes\\B.wav")
    sound.play()

def value_C():
    str.set("C")
    sound = pygame.mixer.Sound("C:\\Users\\ganes\\OneDrive\\Desktop\\internpe\\Gui Piano\\Z_Music_Notes\\Music_Notes\\C.wav")
    sound.play()

def value_Bb():
    str.set("Bb")
    sound = pygame.mixer.Sound("C:\\Users\\ganes\\OneDrive\\Desktop\\internpe\\Gui Piano\\Z_Music_Notes\\Music_Notes\\Bb.wav")
    sound.play()

def value_Gs():
    str.set("G#")
    sound = pygame.mixer.Sound("C:\\Users\\ganes\\OneDrive\\Desktop\\internpe\\Gui Piano\\Z_Music_Notes\\Music_Notes\\G_s.wav")
    sound.play()

def value_Ds():
    str.set("D#")
    sound = pygame.mixer.Sound("C:\\Users\\ganes\\OneDrive\\Desktop\\internpe\\Gui Piano\\Z_Music_Notes\\Music_Notes\\D_s.wav")
    sound.play()

def value_Fs():
    str.set("F#")
    sound = pygame.mixer.Sound("C:\\Users\\ganes\\OneDrive\\Desktop\\internpe\\Gui Piano\\Z_Music_Notes\\Music_Notes\\F_s.wav")
    sound.play()

def value_G():
    str.set("G")
    sound = pygame.mixer.Sound("C:\\Users\\ganes\\OneDrive\\Desktop\\internpe\\Gui Piano\\Z_Music_Notes\\Music_Notes\\G.wav")
    sound.play()

def value_D():
    str.set("D")
    sound = pygame.mixer.Sound("C:\\Users\\ganes\\OneDrive\\Desktop\\internpe\\Gui Piano\\Z_Music_Notes\\Music_Notes\\D.wav")
    sound.play()

def value_E1():
    str.set("E1")
    sound = pygame.mixer.Sound("C:\\Users\\ganes\\OneDrive\\Desktop\\internpe\\Gui Piano\\Z_Music_Notes\\Music_Notes\\E1.wav")
    sound.play()

def value_E():
    str.set("E")
    sound = pygame.mixer.Sound("C:\\Users\\ganes\\OneDrive\\Desktop\\internpe\\Gui Piano\\Z_Music_Notes\\Music_Notes\\E.wav")
    sound.play()

def value_F():
    str.set("F")
    sound = pygame.mixer.Sound("C:\\Users\\ganes\\OneDrive\\Desktop\\internpe\\Gui Piano\\Z_Music_Notes\\Music_Notes\\F.wav")
    sound.play()

def value_F1():
    str.set("F1")
    sound = pygame.mixer.Sound("C:\\Users\\ganes\\OneDrive\\Desktop\\internpe\\Gui Piano\\Z_Music_Notes\\Music_Notes\\F1.wav")
    sound.play()

def value_C1():
    str.set("C1")
    sound = pygame.mixer.Sound("C:\\Users\\ganes\\OneDrive\\Desktop\\internpe\\Gui Piano\\Z_Music_Notes\\Music_Notes\\C1.wav")
    sound.play()

def value_D1():
    str.set("D1")
    sound = pygame.mixer.Sound("C:\\Users\\ganes\\OneDrive\\Desktop\\internpe\\Gui Piano\\Z_Music_Notes\\Music_Notes\\D1.wav")
    sound.play()

def value_Cs1():
    str.set("C#1")
    sound = pygame.mixer.Sound("C:\\Users\\ganes\\OneDrive\\Desktop\\internpe\\Gui Piano\\Z_Music_Notes\\Music_Notes\\C_s1.wav")
    sound.play()

def value_Ds1():
    str.set("C#1")
    sound = pygame.mixer.Sound("C:\\Users\\ganes\\OneDrive\\Desktop\\internpe\\Gui Piano\\Z_Music_Notes\\Music_Notes\\D_s1.wav")
    sound.play()


Label(abc1, text="Piano Musical Keys", font=("arial", 25, "bold"), padx=8, pady=8, bd=4, width=59, bg="powder blue",
      fg="white", height=1,
      justify=CENTER).grid(row=0, column=0, columnspan=11)

display = Entry(abc1, textvariable=str, font=("arial", 18, "bold"), width=35, bd=34, bg="powder blue", fg="black",
                justify=CENTER).grid(row=1, column=5, pady=1)


btnCs = Button(abc2, height=6, width=4, bd=4, text="C#", font=("arial", 18, "bold"), bg="black", fg="white",
               command=value_Cs)
btnCs.grid(row=0, column=0, padx=5, pady=5)
btnDs = Button(abc2, height=6, width=4, bd=4, text="D#", font=("arial", 18, "bold"), bg="black", fg="white",
               command=value_Ds)
btnDs.grid(row=0, column=1, padx=5, pady=5)

btnSpace1 = Button(abc2, state=DISABLED, height=6, width=2, bg="powder blue", relief=FLAT)
btnSpace1.grid(row=0, column=3, padx=0, pady=0)

btnFs = Button(abc2, height=6, width=4, bd=4, text="F#", font=("arial", 18, "bold"), bg="black", fg="white",
               command=value_Fs)
btnFs.grid(row=0, column=4, padx=5, pady=5)
btnGs = Button(abc2, height=6, width=4, bd=4, text="G#", font=("arial", 18, "bold"), bg="black", fg="white",
               command=value_Gs)
btnGs.grid(row=0, column=6, padx=5, pady=5)
btnBb = Button(abc2, height=6, width=4, bd=4, text="Bb", font=("arial", 18, "bold"), bg="black", fg="white",
               command=value_Bb)
btnBb.grid(row=0, column=8, padx=5, pady=5)

btnSpace5 = Button(abc2, state=DISABLED, height=6, width=2, bg="powder blue", relief=FLAT)
btnSpace5.grid(row=0, column=9, padx=0, pady=0)

btnCs1 = Button(abc2, height=6, width=4, bd=4, text="C#1", font=("arial", 18, "bold"), bg="black", fg="white",
                command=value_Cs1)
btnCs1.grid(row=0, column=10, padx=5, pady=5)
btnDs1 = Button(abc2, height=6, width=4, bd=4, text="D#1", font=("arial", 18, "bold"), bg="black", fg="white",
                command=value_Ds1)
btnDs1.grid(row=0, column=12, padx=5, pady=5)

btnC = Button(abc3, bd=4, width=4, height=6, text="C", bg="white", fg="black", font=("arial", 18, "bold"),
              command=value_C)
btnC.grid(row=0, column=0, padx=5, pady=5)
btnD = Button(abc3, bd=4, width=4, height=6, text="D", bg="white", fg="black", font=("arial", 18, "bold"),
              command=value_D)
btnD.grid(row=0, column=1, padx=5, pady=5)
btnE = Button(abc3, bd=4, width=4, height=6, text="E", bg="white", fg="black", font=("arial", 18, "bold"),
              command=value_E)
btnE.grid(row=0, column=2, padx=5, pady=5)
btnF = Button(abc3, bd=4, width=4, height=6, text="F", bg="white", fg="black", font=("arial", 18, "bold"),
              command=value_F)
btnF.grid(row=0, column=3, padx=5, pady=5)

btnG = Button(abc3, bd=4, width=4, height=6, text="G", bg="white", fg="black", font=("arial", 18, "bold"),
              command=value_G)
btnG.grid(row=0, column=4, padx=5, pady=5)
btnA = Button(abc3, bd=4, width=4, height=6, text="A", bg="white", fg="black", font=("arial", 18, "bold"),
              command=value_A)
btnA.grid(row=0, column=5, padx=5, pady=5)
btnB = Button(abc3, bd=4, width=4, height=6, text="B", bg="white", fg="black", font=("arial", 18, "bold"),
              command=value_B)
btnB.grid(row=0, column=6, padx=5, pady=5)
btnC1 = Button(abc3, bd=4, width=4, height=6, text="C1", bg="white", fg="black", font=("arial", 18, "bold"),
               command=value_C1)
btnC1.grid(row=0, column=7, padx=5, pady=5)

btnD1 = Button(abc3, bd=4, width=4, height=6, text="D1", bg="white", fg="black", font=("arial", 18, "bold"),
               command=value_D1)
btnD1.grid(row=0, column=8, padx=5, pady=5)
btnE1 = Button(abc3, bd=4, width=4, height=6, text="E1", bg="white", fg="black", font=("arial", 18, "bold"),
               command=value_E1)
btnE1.grid(row=0, column=9, padx=5, pady=5)
btnF1 = Button(abc3, bd=4, width=4, height=6, text="F1", bg="white", fg="black", font=("arial", 18, "bold"),
               command=value_F1)
btnF1.grid(row=0, column=10, padx=5, pady=5)

root.mainloop()
