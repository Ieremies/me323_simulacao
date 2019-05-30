from random import sample
from random import randint
import matplotlib.pyplot as plt
from statistics import median
from statistics import stdev

#criando a população
populacao = [0 for i in range(3000)]
for j in range(7000):
    populacao.append(1)

#realizando 2000 vezes amostras de 10 e 1000 da populção e colocando a proporção de 0 (candidato A) da amostra na respectiva lista de p_chapeu
p_chapeu_10 = []
p_chapeu_1000 = []

#repitimos 2000 vezes o processo
for j in range(2000):
    #para tamanho 10
    n = 10
    for i in range(n):
        #coloca na lista contagem de 0 na amostra de tamanho n da população dividida pelo tamanho da amostra (proporção)
        p_chapeu_10.append(sample(população, n).count(0) / len(n) )

    #para tamanho 1000
    n = 1000
    for i in range(n):
        #coloca na lista contagem de 0 na amostra de tamanho n da população dividida pelo tamanho da amostra (proporção)
        p_chapeu_1000.append(sample(população, n).count(0) / len(n) )

#GRÁFICO DO N = 10:
#define o tamanho do gráfico
plt.figure(figsize=(21,9))

#diz qual a lista pra ele se basear com bolinhas vermelhas
plt.plot(p_chapeu_10, 'ro')

#média da população para podermos comparar em linha azul pontilhada
plt.plot([0.3 for x in range(2000)], 'b--')

#média acumulada da amostra para em linha verde contínua
plt.plot([median(p_chapeu_10[:x]) for x in range(2000)], 'g-')

#dando nome as coisas
plt.ylabel('proporção candidato A')
plt.title("Amostra de tamanho 10")

#configurando os eixos
plt.axis([0.0, 2001, 0.0, 1.001]) #limites dos eixos
plt.xticks(range(0, 2001, 100)) #marcações do eixo x
plt.yticks([0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]) #marcações do eixo y

#deve ser pra mostrar o gráfico
plt.grid()
plt.show()

#imprimir as informações
print("AMOSTRA DE TAMANHO 10:")
print("     MÉDIA =", median(p_chapeu_10))
print("     DESVIO PADRÃO =", stdev(p_chapeu_10))

#=========================================================================================#

#GRÁFICO DO N = 1000:
#define o tamanho do gráfico
plt.figure(figsize=(21,9))

#diz qual a lista pra ele se basear com bolinhas vermelhas
plt.plot(p_chapeu_1000, 'ro')

#média da população para podermos comparar em linha azul pontilhada
plt.plot([0.3 for x in range(2000)], 'b--')

#média acumulada da amostra para em linha verde contínua
plt.plot([median(p_chapeu_1000[:x]) for x in range(2000)], 'g-')

#dando nome as coisas
plt.ylabel('proporção candidato A')
plt.title("Amostra de tamanho 1000")

#configurando os eixos
plt.axis([0.0, 2001, 0.0, 1.001]) #limites dos eixos
plt.xticks(range(0, 2001, 100)) #marcações do eixo x
plt.yticks([0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]) #marcações do eixo y

#deve ser pra mostrar o gráfico
plt.grid()
plt.show()

#imprimir as informações
print("AMOSTRA DE TAMANHO 1000:")
print("     MÉDIA =", median(p_chapeu_1000))
print("     DESVIO PADRÃO =", stdev(p_chapeu_1000))
