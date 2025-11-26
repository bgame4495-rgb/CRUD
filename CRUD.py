import os
os.system("cls")

#Crud usando lista.
#Create= criar/ salvar
#Read = buscar/selecionar
#update = atualizar / modificar
#Delete = excluir

#criando umaa lista.
lista_cliente = []

#Create
print("CREATE - Adicionar / inserir")
nome = "Marta"
lista_cliente.append(nome)
print(f"O nome: {nome} foi inserido com sucesso ")

#read 
print("\nREAD - Ler /Mostrar")
print (lista_cliente)

# update
print("\nUpdate - Atualizar / Alterar")
nome_para_atualizar = "Marta"
if nome_para_atualizar  in lista_cliente:
    novo_nome = "Marta Silva"
    indice = lista_cliente.index(nome_para_atualizar)
    lista_cliente[indice] = novo_nome
    print(f"O nome {nome_para_atualizar} foi atualizado para {novo_nome}")
else: 
    print(f"O nome {nome_para_atualizar} não foi encontrado")
print(lista_cliente)

# DELETE 
print("\nDelete - Excluir / Remover")
nome_para_excluir = "Marta"
if nome_para_excluir in lista_cliente:
    lista_cliente.remove(nome_para_excluir)
    print(f"{nome_para_excluir} foi excluido com sucesso!")
else:
    print(f"O nome: {nome_para_excluir} não foi encontrado")

print(lista_cliente) 
