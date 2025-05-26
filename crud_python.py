# Rotinas CRUD

# Criar (Create)
with open ("dados.txt", "w") as arquivo:
  arquivo.write("dados")  
  
 # Ler (Read)
with open ("dados.txt", "r") as arquivo:
   for linha in arquivo: 
       print(linha.strip()) 

# Alterar (update)    
with open ("dados.txt", "r") as arquivo:    
    linhas = arquivo.readlines() #ler arquivo e joga na variavel
# faz a modificação
with open ("dados.txt", "w") as arquivo:
    for linha in linhas:
        if linha.strip() == "dados":
            arquivo.write("atualizado\n")    
        else:
            arquivo.write()
            
#excluir (Delete)
with open ("dados.txt", "r") as arquivo:
    linhas = arquivo.readlines()
    
#eliminar o arquivo
with open ("dados.txt", "w") as arquivo:
    for linha in linhas:
        if linha.strip() != "atualizado\n":
            arquivo.write(linha)