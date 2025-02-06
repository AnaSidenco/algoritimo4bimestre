#VAMOS SIMULAR COMO FUNCIONAR O ALGORITIMO DE UMA IMPRESSORA QUE PODE RECEBER IMPRESSÃO DE DIVERSOS COMPUTADORES, VAMOS PENSAR EM UMA FILA

class FilaDeImpressao:


    def configurar_inicial(self):
       self.fila= []
        #isso vai guardar a fila de impressao no vetor fila

    def adicionar_trabalho(self,trabalho):
        self.fila.append(trabalho)
        print(f"Trabalho '{trabalho}' adicionado a fila de impressão")

#remover o ytabalho da lista 
    def processar_trabalho(self):
        if not self.esta_vazia():
            trabalho = self.fila.pop(0)
            print(f"o trabalho '{trabalho}' esta sendo processado")
        else:
            print("A fila esta vazia!")
    
    def mostrar_fila(self):
        if self.esta_vazia():
            print("A fila está vazia!")
        else:
            print("Fila atual de impressão:") 
            for trabalho in self.fila:
                print(f"-{trabalho}")    
    def esta_vazia(self):
        return len(self.fila) == 0


    #funçoes de interação com o usuario 
def menu():
        fila_impressao= FilaDeImpressao()
        #criando uma instancia para a classe
        fila_impressao.configurar_inicial()
        #configurar os atributos de entrada/inicial 
        while True:
            #opção para o nosso usuario
            print("/n Opções:")
            print("1 Adiciona um trabalho na fila da impressao")
            print("2. imprimir o proximo trabalho da fila")
            print("3. mostrar a fila de impressao")
            print("4. sair")
            escolha = input("escolha uma opcao 1-4")
            #aqui vai ser lido a escolha do usuario

            if escolha == "1":
                trabalho = input("digite o nome do trabalho a ser impresso")
                #maquina da pessoa que esta imprimindo 
                fila_impressao.adicionar_trabalho(trabalho)
            elif escolha=="2":
                    fila_impressao.processar_trabalho()
            elif escolha=="3":
                    fila_impressao.mostrar_fila()
            elif escolha=="4":
                print("saindo do programa")
                break
            else:
                    print("opcao invalida")

menu()

    
    
    
  