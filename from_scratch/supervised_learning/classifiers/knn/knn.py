import matplotlib.pyplot as plt
import numpy as np
import operator
########################################
# Calcula distância entre dois exemplos
########################################
def distancia_euclidiana(a, b):
    soma = 0.0  # print('calculando distancia entre {} e {}'.format(a, b))
    for i in range(0, len(a)):  # para cada componente
        soma = soma + (a[i] - b[i])**2  # subtrai componentes
    return soma**(1/2.0)  # tira a raiz


########################################
# Mapeia uma classe a um número de ocorrências
########################################
def mapeia_labels(somelist):
    # cria um map do tipo x:0, para cada x na lista de entrada
    return {x: 0 for x in somelist}


########################################
# Mapeia uma classe a um número de ocorrências ( only to 2dimension)
########################################
def plota_raio_distancia(x, r, classe):
    # plota o raio
    circle1 = plt.Circle((x[0], x[1]), r, fill=False, color=classe, linestyle='--')
    fig = plt.gcf()
    ax = fig.gca()
    ax.add_artist(circle1)
    # plota o ponto em si
    plt.scatter(x[0], x[1], c=classe, marker='x', s=200)



########################################
# The KNN Classifier it-self
########################################
def classify(x, dataSet, labels ,k):
    dis = np.zeros(len(dataSet[:,0]))  # cria vetor com distâncias = 0
    for i in range(0, len(dis)):  # calcula distancias pra cada ponto com o x
        dis[i] = distancia_euclidiana(dataSet[i], x)
    # mapeia e ordena distancias
    dis = list(zip(dis, labels))  # mapa com (distancia para as classes)
    dis = sorted(dis)  # ordena distâncias (para pegar as menores)
    # pega os k mais proximos e faz a contagem das classes
    classes = mapeia_labels(labels)  # cria map com distancia/quantidade (ocorrencias)
    for i in range(0, k):  # k vizinhos
        classes[dis[i][1]] = classes[dis[i][1]] + 1  # [dis[i][1] é o nome da classe
    # pega o mais frequente
    classe = max(classes.items(), key=operator.itemgetter(1))[0]
    # plota o raio de distancia mais externo (k-1)
    #plota_raio_distancia(x, dis[k-1][0], classe)
    # retorna o mais frequente
    return classe
