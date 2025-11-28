import os
import time 
from dataclasses import dataclass
os.system("cls || clear") # limpa o terminal em Windows e Linux

lista_clientes = []

@dataclass
class Cliente:
        #Atributos da classe
        #Atributos são variaveis que pertecem a classe
        nome: str
        email: str
        telefone:str
        
        #Metodo é o nome dado a uma função que pertence a clase
        #Metodo para mostrar as informarções dos clientes.
        def mostrar_dados(self):
            print(f"Nome: {self.nome} - \nE-mail {self.email} - \nTelefone {self.telefone}")


    #funçao para verificar se a lista esta vazia
def lista_vazia(lista_clientes):
    if not lista_clientes:
        print("\nNão há clientes cadastrados.")
        return True
    return False

def adicionar_cliente(lista_cliente):
        print("\n---Adicionar novo clinte --- ")
        nome = input("Digite seu nome: ")
        email = input("Digite seu E-mail: ")
        Telefone = input("Digite seu Telefone: ")

        novo_cliente = Cliente(nome=nome, email=email, telefone=Telefone)
        lista_cliente.append(novo_cliente)
        print(f"\nCliente {nome} adicionado com sucesso!")

    #Função para encontrar um cliente na lista
def encontrar_cliente_por_nome(lista_clientes, nome_buscar):
    nome_buscar_lower = nome_buscar.lower()
    for cliente in lista_clientes:
            if cliente.nome.lower() == nome_buscar_lower:
                return  cliente
    return None # None siginifica retornar vazio, sem conteudo.


    # Função para mostrar todos os clientes.
def mostrar_todos_clientes(lista_clientes):
    if lista_vazia(lista_clientes):
            return
    print("\n--- Lista de Clientes ---")
    for posicao, cliente in enumerate(lista_clientes):
            print(f"{cliente.mostrar_dados()}")

    #função para atualizar clientes.
def atualizar_clientes(lista_clientes):
    if lista_vazia(lista_clientes):
        return
    
    #mostrar lista para ajudar o usuario.
    mostrar_todos_clientes(lista_clientes)
    print("--- Atualizar dados do cliente ---")
    nome_buscar = input("\nDigite o nome que do cliente: ")
    cliente_para_atualizar = encontrar_cliente_por_nome(lista_clientes, nome_buscar)

    if cliente_para_atualizar:
        print("\nPessoa encontrada.")
        print("\nDigite os novos dados ou deixe em branco para manter o valor atural")

        print(f"Nome atual: {cliente_para_atualizar.nome}")
        novo_nome=input(f"Novo nome: ")
        print(f"E-mail atual: {cliente_para_atualizar.email}")
        novo_email=input(f"Novo E-mail:")
        print(f"\nTelefone atual: {cliente_para_atualizar.telefone}")
        novo_telefone=input(f"Novo Telefone: ") 

        if novo_nome:
             cliente_para_atualizar.nome = novo_nome
        if novo_email:
             cliente_para_atualizar.email = novo_email
        if novo_telefone:
             cliente_para_atualizar.telefone = novo_telefone
             
             print(f"\nDados do Cliente? {nome_buscar} atualizados com sucessos!")
        else:
             print(f"\nCliente com nome: {nome_buscar} não encontrado.")

#Mostrando Menu
while True:
     print("""
--- Gerenciador de Clientes ---
1- Adicionar 
2- Mostrar todos
3- Atualizar 
4- Excluir 
0- Sair
""")

     opcao= int(input("Digite uma das opções acima: "))

     match opcao:
            case 1:
               adicionar_cliente(lista_clientes)
            case 2:
               mostrar_todos_clientes(lista_clientes)
            case 3:
               atualizar_clientes(lista_clientes)
            case 4:
               excluir_cliente(lista_clientes)
            case 0:
               print("\nSaindo do programa...")
               break
            case _:
               print("\nOpção invalida. \nTente novamente")
     
     if opcao != 1 and opcao !=0:
       time.sleep(4)
     elif opcao == 1:
       time.sleep(1)
      
       #Limpa tela
     if opcao !=0:
      os.system("cls || clear")    
        
        
                

