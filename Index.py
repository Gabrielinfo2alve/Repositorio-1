from tkinter import *

from tkinter import messagebox

from tkinter import ttk
import sqlite3



import Databaser







#Criação de Janela 

jan = Tk()

jan.title("Enchanté! Idiomas")

jan.geometry("600x300")

jan.configure(background="white")

jan.resizable(width=False, height=False)



#Carregamento de logotipo

Logo = PhotoImage(file="C:/Users/Gabriel e Yêssa/Desktop/Codigos/Flutter/flutter/.vscode/flutter_application_1/App com video DevcodeBR/icons/logobranca2.png")


#Frames da Janela de inicio 


LeftFrame = Frame(jan, width=200, height=300, bg="black", relief="raise")

LeftFrame.pack(side=LEFT)


RightFrame = Frame(jan, width=395, height=300, bg="White", relief="raise")

RightFrame.pack(side=RIGHT)


LogoLabel = Label(LeftFrame, image=Logo, bg="black")

LogoLabel.place(x=25, y=120)


#Usuario 


UserLabel = Label(RightFrame, text="Usuario ->", font=("Century Gothic", 10), bg="white", fg="Black")

UserLabel.place(x=10, y=105)

UserEntry = ttk.Entry(RightFrame, width=30)

UserEntry.place(x=145, y=105)



#Senha


SenhaLabel = Label(RightFrame, text="Senha  ->", font=("Century Gothic", 10), bg="white", fg="Black")

SenhaLabel.place(x=10, y=150)

SenhaEntry = ttk.Entry(RightFrame,width=30)

SenhaEntry.place(x=145, y=150)


#Botões Iniciais 


LoginButton = ttk.Button(RightFrame, text="Login", width=10)

LoginButton.place(x=145, y=240)


#Registro Pelo Adm


def Register():

    LoginButton.place(x=5000)

    RegisterButton.place(x=5000)

    #Informações de Cadastro

    NomeLabel = Label(RightFrame, text= "Nome Completo ->", font=("Century Gothic", 10), bg="White", fg="Black")  

    NomeLabel.place(x=10, y=10)

    #Campo Preencher Nome Completo

    NomeEntry = ttk.Entry(RightFrame, width=40)

    NomeEntry.place(x=145, y=12)


    EmailLabel = Label(RightFrame, text= "Email ->", font=("Century Gothic", 10), bg="White", fg="Black")  

    EmailLabel.place(x=10, y=55)

    #Campo Preencher Email

    EmailEntry = ttk.Entry(RightFrame, width=40)

    EmailEntry.place(x=145, y=57)


    CPFLabel = Label(RightFrame, text= "CPF ->", font=("Century Gothic", 10), bg="White", fg="Black")  

    CPFLabel.place(x=10, y=190)

    #Campo Preencher Email

    CPFEntry = ttk.Entry(RightFrame, width=20)

    CPFEntry.place(x=145, y=192)


    def RegistrandoBasedeDados():

        Name = NomeEntry.get()
        Email = EmailEntry.get()

        User = UserEntry.get()

        Senha = SenhaEntry.get()

        CPF = CPFEntry.get()
        
    

        Databaser.cursor.execute("""

        INSERT INTO Users(Name , Email, User, Senha, CPF

) VALUES(?,?,?,?,?)

        """,(Name, Email, User, Senha, CPF))
        (sqlite3.connect('DBappAlunos2.db')).commit()
        Databaser.conn.commit()

        messagebox.showinfo(title="Register Info", message="Registrado com Sucesso")


    #Botão de Registro dentro da aba de Registro 

    Register = ttk.Button(RightFrame, text="Registrar", width=16, command=RegistrandoBasedeDados)

    Register.place(x=240, y=240)


    def BackToLogin():

        #Removendo todos os widgets da aba de login para retornar para pagina de registro

        NomeEntry.place(x=5000)

        NomeLabel.place(x=5000)

        EmailEntry.place(x=5000)

        EmailLabel.place(x=5000)
       


        #Voltando para a pagina trasendo os Botões novamente

        LoginButton.place(x=145)

        RegisterButton.place(x=5000)

        CPFEntry.place(x=5000)

        CPFLabel.place(x=5000)

        Back.place(x=5000)
         


     #Botão de voltar para pagina de login

    Back = ttk.Button(RightFrame, text="Voltar", width=18, command=BackToLogin)

    Back.place(x=120,y=240)
    


RegisterButton = ttk.Button(RightFrame, text="Registrar", width=18, command=Register)

RegisterButton.place(x=240, y=240)



jan.mainloop()

