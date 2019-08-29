#!/usr/bin/python

import copy
import sys

def son2str(s):
    s1 = s[0] + s[1] + s[2]
    return ''.join([str(v) for v in s1])

def valid(x, y):
    r = True
    if x < 0 : r = False
    if x > 2 : r = False
    if y < 0 : r = False
    if y > 2 : r = False
    return r
    

def sons(s):
    r = []
    x = None
    y = None
    #localiza zero
    for i in range(len(s)):
        for j in range(len(s[i])):
            if s[i][j] == 0:
                x = i
                y = j
    # cima
    vx = x - 1
    vy = y
    if (valid(vx, vy)):
        ts = copy.deepcopy(s)
        t = ts[vx][vy]
        ts[vx][vy] = ts[x][y]
        ts[x][y] = t
        r.append(ts)
    # baixo
    vx = x + 1
    vy = y
    if (valid(vx, vy)):
        ts = copy.deepcopy(s)
        t = ts[vx][vy]
        ts[vx][vy] = ts[x][y]
        ts[x][y] = t
        r.append(ts)

    # direita
    vx = x 
    vy = y +1
    if (valid(vx, vy)):
        ts = copy.deepcopy(s)
        t = ts[vx][vy]
        ts[vx][vy] = ts[x][y]
        ts[x][y] = t
        r.append(ts)

    # esquerda
    vx = x 
    vy = y - 1
    if (valid(vx, vy)):
        ts = copy.deepcopy(s)
        t = ts[vx][vy]
        ts[vx][vy] = ts[x][y]
        ts[x][y] = t
        r.append(ts)

    return r

def printPuzzle(s):
    for v in s:
        print (v)


def bfs(start, goal):
    l = [start]
    fathers = dict()
    visited = [start]
    while (len(l) > 0):
        father = l[0]
        del l[0]
        for son in sons(father):
            if son not in visited:
                visited.append(son)
                print (len(visited))
                fathers[son2str(son)] = father
                if son == goal:
                    res = []
                    node = son
                    while node != start:
                        res.append(node)
                        node = fathers[son2str(node)]
                    res.append(start)
                    res.reverse()
                    print (res)
                    return res
                else:
                    l.append(son)
    print ('Sem Solucao')



if __name__ == '__main__':
    f = open(sys.argv[1])
    entrada = []
    for line in f:
        tv = [int(v) for v in line.rstrip('\n').split(' ')]
        entrada.append(tv)

    resp = bfs(entrada, [[1, 2, 3], [4, 5, 6], [7, 8, 0]])
    for s in resp:
        printPuzzle(s)
        print()
        