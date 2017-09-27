import random

entrada = [[0 for i in range(4)] for j in range(300)]
count=0
for i in entrada:
    if count < (len(entrada)/2):
        i[0] = random.random()
        i[1] = random.random()
        i[2] = 1 # i[2] é o bias. em ambos casos.
    else:
        i[0] = 1+random.random()
        i[1] = 1+random.random()
        i[2] = 1
        i[3] = 1
    count+=1

w = [random.random() for i in range(3)]
limiar = 0.0
txapr = 0.0

def calcula(x0, x1, x2):
    soma = (x0*w[0])+(x1*w[1])+(x2*w[2])
    global limiar
    if soma >= limiar:
        return 1
    else:
        return 0
    
def atualiza_peso(ent,s):
    global w
    w[0] += txapr * (ent[3] - s) * ent[0]
    w[1] += txapr * (ent[3] - s) * ent[1]
    w[2] += txapr * (ent[3] - s) * ent[2]

peso_igual = 0
def treina(ent):
    global peso_igual
    saida = calcula(ent[0],ent[1],ent[2])
    print('Saida desejada: ',ent[3],'\nSaída obtida: ',saida)
    if saida != ent[3]:
        print('Saídas diferentes. Recalculando pesos...')
        peso_igual=0
        atualiza_peso(ent,saida)
    else:
        print('Saidas iguais, pesos se repetem :)')
        peso_igual+=1

def perceptron(apr,lim):
    global limiar,txapr,peso_igual,w
    limiar = lim
    txapr = apr
    epoca = 0
    while 1:
        mat=0
        for i in entrada:
            print('Matriz: ',mat,'\nPeso de x: ',w[0],'\nPeso de y: ',w[1],'\nPeso do BIAS: ',w[2])
            treina(i)
            mat+=1
            print('................')
        epoca+=1
        print("Época: ",epoca)
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        if peso_igual >= len(entrada):
            break
        
