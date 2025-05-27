from tkinter import *

menu_inicial2 = Tk()
menu_inicial2.title("Tela de Login")
menu_inicial2.geometry("400x400+600+200")
menu_inicial2.resizable(width=False, height=False)

label2 = Label(menu_inicial2, text= "Usuario: ", fg="DarkBlue", font=("Arial", 16, "bold"))
label2.grid(column=0, row=0, padx=10, pady=10, sticky=W)

txtUsuario = Entry(menu_inicial2, font=("Arial", 16, "bold"))
txtUsuario.grid(column=1, row=0, padx=10, pady=10, sticky=W)

label3 = Label(menu_inicial2, text="Senha: ", fg="DarkBlue", font=("Arial", 16, "bold"))
label3.grid(column=0, row=1, padx=10, pady=10, sticky=W)

txtSenha = Entry(menu_inicial2, font=("Arial", 16, "bold"))
txtSenha.grid(column=1, row=1, padx=10, pady=10, sticky=W)








menu_inicial2.mainloop()