import os
import time 
from dataclasses import dataclass
os.system("cls || clear") # limpa o terminal em Windows e Linux

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

