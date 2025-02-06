"""
Vamos FAZER UM PROGRAMA QUE LEIA 10 NUMEROS REAIS E OS ARMAZENAR EM UMA LISTA.
CALCULE E MOSTRE: 
A QUANTIDADE DE NUMEROS NEGATIVOS 
A SOMA DOS NUMEROS POSITIVOS
"""

#criando vetor
numero = []
#crianado uma estrutura do tipo para que vai receber 5 elementos , se quisesse  recebesse mais elementos é so trocar dentro dos parentese  
for i in range(10):
    #estamos  chamando aqui o float antes de input pois nossos dados são tipo real 
    numerounitaria = float(input("Digite a nota do aluno: "))
    # o append esta incrementando o vetor atras  do final da lista, o que define a estrutura de dados do tipo lisa é isso aqui
    numero.append(numerounitaria)

quantidade_negativos = 0
soma_positivos = 0 
# para passar dentro de todos os itens do vetor usamos:

for numerounitaria in numero:
    if numerounitaria <0 :#verificando se é negativo
        quantidade_negativos += 1 # é a mesma coisa que quantidade_negativo = quantidade_negativos + 1 
    if numerounitaria > 0 : #verifique se é positivo 
        soma_positivos += numerounitaria# é a mesma coisa que soma_positivos = somapositivos + numerounitario



print(f"quantidade de numeros negativos: {quantidade_negativos}, e a soma dos positivos é :{soma_positivos}")

