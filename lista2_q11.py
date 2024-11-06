def receber_elementos():
   global lista
   while True:
      try:
         quantidade = int(input("Qual a quantidade de elementos da lista?"))
         while quantidade <= 0:
            quantidade = int(input("A quantidade deve ser maior que 0: "))
         lista = quantidade
         break
      except:
         print("Quantidade inválida!")

def gravar_nome():
   if len(nomes) < lista:
      nomes.append(input("Qual o nome da pessoa? "))
    #  nomes.append(nome)
      print("Incluido com sucesso!")
   else:
      print("A lista já está cheia!")

def pesquisar_nome():
   if len(nomes) != 0:
      nome = input("Qual o nome a pesquisar? ")
      if nomes.count(nome) > 0:
         print("O nome está na lista na posição %d." % nomes.index(nome))
      else:
         print("O nome não está na lista!")
   else:
      print("A lista está vazia!")

def listar_nomes():
   if len(nomes) != 0:
      print(nomes)
   else:
      print("A lista está vazia!")
def excluir_nome():
   if len(nomes) > 0:
      nome = input("Qual o nome a excluir? ")
      if nomes.count(nome) > 0:
         nomes.remove(nome)
         del nomes[nomes.index(nome)]
         print("O nome %s foi excluido com sucesso." % (nome))
      else:
         print("O nome não está na lista!")
   else:
      print("A lista está vazia!")
def alterar_nome():
   if len(nomes) > 0:
      nome = input("Qual o nome a alterar? ")
      #if nomes.count(nome) > 0:
      if nome in nomes:
         print("Nome anterior: %s." % (nome))
         novo_nome = input("Nome atual: ")
         nomes[nomes.index(nome)] = novo_nome
         print("Alteração realizada com sucesso")
      else:
         print("O nome não está na lista!")
   else:
      print("A lista está vazia!")

def menu():
   receber_elementos()
   while True:
      print("\n=========== MENU ============")
      print(" 1)Cadastrar nome")
      print(" 2)Pesquisar nome")
      print(" 3)Listar todos os nomes")
      print(" 4)Excluir nome")
      print(" 5)Alterar nome")
      print(" 0)Sair do programa")
      print("-----------------------------")
      try:
         opc = int(input("Digite sua opção: "))
         if opc == 0:
            break
         elif opc == 1:
            gravar_nome()
         elif opc == 2:
            pesquisar_nome()
         elif opc == 3:
            listar_nomes()
         elif opc == 4:
            excluir_nome()
         elif opc == 5:
            alterar_nome()
      except:
         print("Opção inválida. Digite novamente!")

max_lista = 0
nomes = []
menu()
