#entrada de dados


nome = input('Qual o seu nome? ')
idade = int (input('Qual a sua idade? '))
peso = float (input('Qual o seu peso? '))
print (f"{nome} tem {idade } e pesa {peso: .1f} kilos")


#variavel dentro da entrada de dados
nome = input('Qual o seu nome? ')
idade = int (input(f"Qual a sua idade {nome} ?"))
print(f"{nome} tem {idade} anos")

from cProfile import label
from tkinter import *
from tkinter import messagebox
from tkinter import Label

def hello():
    #showerror, showinfo, showwaring, askyesno, esquequestion, asktrycancel, askyesnocancel
   messagebox.showinfo("Agente somos programaderos", "Oferecimento organizações tabajara")

def logout():
    resposta = messagebox.askyesno("Sair", "Want Logout?")
    if resposta:
     menu_inicial.destroy()

menu_inicial = Tk()
menu_inicial.title("Meu preimeiro software")
menu_inicial.geometry("500x500+580+200")
menu_inicial.resizable(width=FALSE, height=FALSE)
menu_inicial ['bg'] = "DarkGray"
menu_inicial.iconbitmap("")

label1 = Label(menu_inicial, text= "Menu", bg= "LightGray", fg="blue", font= "Arial 40 bold")
label1.pack()

botao = Button(menu_inicial, text= "Login", bg= "LightGray", fg= "Blue", font= "Arial 20 bold", command=hello)
botao.pack()
botaosair = Button(menu_inicial, text= "Logout", bg= "LightGray", fg= "Blue", font= "Arial 20 bold", command=logout)
botaosair.pack()
menu_inicial.mainloop()
