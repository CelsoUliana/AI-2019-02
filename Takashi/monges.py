#!/usr/bin/python3
import copy
MONGES = 0
CANIBAIS = 1
BARCO = 2

def valido(v):
    ret = True
    c = [ 3 - v[MONGES], 3 - v[CANIBAIS]]
    if v[MONGES] > 3 or v[CANIBAIS] > 3:
        ret = False
    if v[MONGES] < 0 or v[CANIBAIS] < 0:
        ret = False
    if c[MONGES] > 3 or c[CANIBAIS] > 3:
        ret = False
    if c[MONGES] < 0 or c[CANIBAIS] < 0:
        ret = False
    if (c[CANIBAIS] > c[MONGES]) and c[MONGES] != 0 and ret:
        ret = False
    if (v[CANIBAIS] > v[MONGES]) and v[MONGES] != 0 and ret:
        ret = False
    return ret


#               [3, 3, -1]
def gera_filhos(estado):
    filhos = []
    binverte = estado[BARCO]* -1
    # 2 monges
    v = copy.deepcopy(estado)
    v[MONGES] = v[MONGES] + 2 * v[BARCO]
    v[BARCO] = binverte
    if valido(v):
        filhos.append(v)
    # 2 canibais
    v = copy.deepcopy(estado)
    v[CANIBAIS] = v[CANIBAIS] + 2 * v[BARCO]
    v[BARCO] = binverte
    if valido(v):
        filhos.append(v)
    # 1 monge
    v = copy.deepcopy(estado)
    v[MONGES] = v[MONGES] + 1 * v[BARCO]
    v[BARCO] = binverte
    if valido(v):
        filhos.append(v)
 
    # 1 canibal
    v = copy.deepcopy(estado)
    v[CANIBAIS] = v[CANIBAIS] + 1 * v[BARCO]
    v[BARCO] = binverte
    if valido(v):
        filhos.append(v)
 
    # 1 monge 1 canibal
    v = copy.deepcopy(estado)
    v[CANIBAIS] = v[CANIBAIS] + 1 * v[BARCO]
    v[MONGES]   = v[MONGES] + 1 * v[BARCO]
    v[BARCO] = binverte
    if valido(v):
        filhos.append(v)
    return filhos

def estado2str(v):
    return "%d %d %d"%(v[MONGES], v[CANIBAIS], v[BARCO])

if __name__ == '__main__':
    start_state = [3, 3, -1]
    final_state = [0, 0, 1]
    lista = [start_state]
    visitou = []
    dpai = dict()
    pai = start_state
    while(len(lista) > 0 and pai != final_state):
        pai = lista[0]
        del(lista[0])
        if pai not in visitou:
            visitou.append(pai)
            filhos = gera_filhos(pai)
            lista = lista + filhos
            print(pai, filhos, lista)
            for filho in filhos:
                    sfilho =  estado2str(filho)
                    if sfilho not in dpai:
                        dpai[sfilho] = estado2str(pai)
                    print('--->', filho, pai)
        print("pai->", pai, lista)
    spai = estado2str(final_state)
    cont = 0
    while spai != '3 3 -1' and cont < 20 :
       print(spai)
       spai = dpai[spai]
       cont += 1
    print(spai)
