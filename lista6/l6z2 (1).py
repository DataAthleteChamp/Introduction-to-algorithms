from json.encoder import INFINITY
from random import randint as rand
from queue import PriorityQueue

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
    return ls

def dijkstra(ls, v, u):
    D = [INFINITY]*(len(ls))
    p = [(-1,-1)]*(len(ls))
    D[v] = 0
    pq = PriorityQueue()
    pq.put((0,v))
    while not pq.empty():
        (dist,akt) = pq.get()
        for n in ls[akt]:
            if dist+n[1] < D[n[0]]:
                D[n[0]] = dist+n[1]
                p[n[0]] = (akt, n[1])
                pq.put((D[n[0]], n[0]))
    sum = D[u]
    result = []
    while (p[u] != (-1,-1)):
        result.append((p[u][0], u, p[u][1]))
        u = p[u][0]
    return (sum,result)

def Write(result):
    if result[0] == INFINITY:
        print("ŚCIEŻKA POMIĘDZY PODANYMI WIERZCHOŁKAMI NIE ISTNIEJE!")
    else:
        print("SUMARYCZNA WAGA ŚCIEŻKI = ", result[0], "\nŚcieżka:")
        result[1].reverse()
        for i in range(len(result[1])):
            print(result[1][i][0], " -> ", result[1][i][1], " = ", result[1][i][2])



ls = CreateGraph(10,20)
result = dijkstra(ls, rand(1,len(ls)-1), rand(1,len(ls)-1))
Write(result)