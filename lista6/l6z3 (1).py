from json.encoder import INFINITY
from random import randint as rand
from queue import PriorityQueue
from re import M

def CreateGraph(vertices, edges):
    ls = [ [] for i in range(vertices+1)]

    edges = max(0, min(edges, int(vertices*(vertices+1)/2)))
    for i in range(edges):
        v = rand(1,vertices)
        u = rand(1,vertices)
        while (u == v):
            u = rand(1,vertices)
        w = rand(1,100)
        ls[u].append((v,w))
        ls[v].append((u,w))
    return ls, ls

def Find(parent, x):
    if parent[x] == x:
        return x
    return Find(parent, parent[x])

def Union(parent, rank, x, y):
    a = Find(parent,x)
    b = Find(parent,y)
    if rank[a] < rank[b]:
        a,b = b,a
    parent[b] = a
    rank[a] += rank[b]


def Kruskal(ls):
    V = len(ls)
    result = []
    rank = [0] * V
    parent = [i for i in range(V)]

    es = []
    for i in range(1,V):
        for j in range(0,len(ls[i])):
            if i < ls[i][j][0]:
                es.append((ls[i][j][1], i,ls[i][j][0]))
    es.sort()
    
    for edge in es:
        if len(result) == V-1:
            break
        w,v,u = edge
        x = Find(parent,v)
        y = Find(parent,u)
        if x != y:
            result.append((v,u,w))
            Union(parent,rank,x,y)

    return len(result)==V-2, result

def Prim(ls):
    V = len(ls)
    mx = [[0 for i in range(len(ls))] for i in range(len(ls))]
    for i in range(1,V):
        for j in range(0,len(ls[i])):
            if i < ls[i][j][0]:
                mx[i][ls[i][j][0]] = mx[ls[i][j][0]][i] = ls[i][j][1]
    
    visited = [0]*(V)
    es = 0
    visited[1] = True
    result = []
    while(es < V-2):
        mini = INFINITY
        a = 0
        b = 0
        for x in range(1,V):
            if visited[x]:
                for y in range(1,V):
                    if ((not visited[y]) and mx[x][y]):
                        if mini > mx[x][y]:
                            mini = mx[x][y]
                            a = x
                            b = y
        result.append((a,b,mx[a][b]))
        visited[b] = True
        es += 1

    return len(result)==V-2, result



def Write(result, name):
    print(name, ":")
    if result[0] == False:
        print("Podany Graf nie jest spójny!")
    else:
        print("Krawędzie MST:")
        for e in result[1]:
            print(e[0], " -> ", e[1], " = ", e[2])


lsK, lsP = CreateGraph(10,20)
resultK = Kruskal(lsK)
resultP = Prim(lsP)
Write(resultK, "KRUSKAL")
Write(resultP, "PRIM")