# O rei de um reino muito distante deu uma grande festa para reunir todas as gerações dos seus descendentes: 
#filhos e filhas, netos e netas, bisnetos e bisnetas, e assim por diante. 
#Ele, que gosta muito de estatística, agora quer saber, para cada geração que porcentagem de descendentes daquela geração compareceu à festa. 
#Você foi contratado para escrever um programa de computador que calcule a porcentagem de todas as gerações!


#A primeira linha da entrada contém dois inteiros N e M, respectivamente, o número de descententes e o número de participantes da festa.
#A segunda linha contem N número, representando os pais ou mães dos N descendentes, em ordem crescente:
#o primeiro número indica o pai ou mãe do descendente número 1, o segundo do número 2, e assim por diante.
#A terceira linha contém M números, identificando todos os descendentes que compareceram a festa.

#O programa deve imprimir uma linha com uma lista de números reais, com precisão de duas casas decimais, indicando a porcentagem, para cada geração
#dos descendentes daquela geração quecompareceram à festa. O primeiro número deve ser a porcentagem de filhos e filhas, o segundo dos netos e netas, e assim por diante.

#Exemplo:
#Input: 
#9 5
#7 3 0 9 0 3 5 6 7
#3 2 8 1 9
#Output:
#50.00 33.33 100.00 0.00

n = int(input()[0])
pais = list(input())[::2]
presença = list(input())[::2]

descendentes = [str(x) for x in range(n+1)]
arvore = [[0]]

def filhos(valor):
    filhes = []
    for numero in valor[0]:
        for indice in range(len(pais)):
            if pais[indice] == str(numero):
                filhes += [indice+1]
    if filhes == []: return valor
    valor += [filhes]
    return [valor[0]] + filhos(valor[1:])


def CalcularPresença(vetor):
    total = len(vetor[0])
    resultado = []
    for elemento in vetor[0]:
        for presentes in presença:
            if str(elemento) == presentes:
                resultado += [1]
    porcentagem = (len(resultado)/total)*100
    porcentagem = "%.2f" % porcentagem
    if len(vetor[0]) == 1: return [porcentagem]
    return [porcentagem] + CalcularPresença(vetor[1:])
        
Arvore = filhos([[0]])
print(CalcularPresença(Arvore[1:]))
