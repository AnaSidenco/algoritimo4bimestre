"""
FAÇA UM PROGRAMA QUE VAI LER 5 NOTAS E ARMAZENAR EM UMA LISTA 
Imprimir media geral da turma
"""
#criando vetor
nota = []
#crianado uma estrutura do tipo para que vai receber 5 elementos , se quisesse  recebesse mais elementos é so trocar dentro dos parentese  
for i in range(5):
    #estamos  chamando aqui o float antes de input pois nossos dados são tipo real 
    notaunitaria = float(input("Digite a nota do aluno: "))
    # o append esta incrementando o vetor atras  do final da lista, o que define a estrutura de dados do tipo lisa é isso aqui
    nota.append(notaunitaria)
    
# criando a variavel media
media = 0 

#o item no vai ser quem vai passar em todos os itens do vetor, e vai colocalos dentro da media, que ira somando item por item ate finalizar  valor 
for no in nota: 
    media = media + no

media = media/5

print (f"media geral: {media}")
