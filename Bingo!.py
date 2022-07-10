#O grande prêmio do Bingo de São João será um carro zero-quilômetro. Todo mundo quer ser o primeiro a completar sua cartela, claro. São N cartelas identificadas de 1 até N que contêm, cada uma, K números distintos entre os números naturais de 1 até U, para K<U. Um número, claro, pode aparecer em mais de uma cartela e duas cartelas podem até ser iguais, ter o mesmo conjunto de números. Justamente por isso, veja que pode acontecer empate com mais de uma cartela sendo completada no mesmo instante.
#Neste problema, serão dados na entrada os conjuntos de números de todas as cartelas e a sequência de números sorteados, que será uma permutação dos naturais de 1 até U. Seu programa deve determinar qual ou quais cartelas vão ser completadas primeiro e ganhar o carro.
#Por exemplo, para N=4, K=5 e U=10, com as cartelas dadas pela tabela abaixo, se a sequência de números sorteados for [7,3,5,2,6,1,9,10,4,8], então haverá uma cartela vencedora, a número 3.


N, K, U = input().split()

cartelas = []
for contador in range(int(N)):
    cartelas += [input().split()]
    
gabarito = input().split()


def winner(cartelas, gabarito):
    resultado = []

    for cartela in cartelas:
        if cartela == []: gabarito = gabarito[:1] 
    if gabarito == []: 
        for indice in range(len(cartelas)):
            if cartelas[indice] == []:
                resultado += [indice+1]
        return resultado
    
    for indice in range(len(cartelas)):
        for indice2 in range(len(cartelas[indice])):
            if cartelas[indice][indice2] == gabarito[0]:
                del cartelas[indice][indice2]
                return winner(cartelas,gabarito)
            
    return winner(cartelas, gabarito[1:])

    
    
#cartelas = [['1', '9', '3', '2'], ['4', '5', '6', '7'], ['2', '3', '5', '4'], ['2', '6', '8', '1'], ['2', '5', '7', '9']]
#gabarito = ['1', '9', '7', '4', '5', '3', '2', '8', '6']

print(winner(cartelas,gabarito))

