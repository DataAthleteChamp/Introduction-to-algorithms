from json.encoder import INFINITY
from random import randint as rand

def CreateGraph(vertices, edges):
    ls = [ [] for i in range(vertices+1)]

    edges = max(0, min(edges, int(vertices*(vertices+1)/2)))
    for i in range(edges):
        v = rand(1,vertices)
        u = rand(1,vertices)
        while (u == v):
            u = rand(1,vertices)
        ls[u].append(v)
        ls[v].append(u)
    return ls

def dfs(visited, ls, v, color):
    visited[v] = color
    for u in ls[v]:
        if visited[u] == 0:
            dfs(visited, ls, u,color)

def SplitGraph(ls):
    visited = [0]*(len(ls))
    count=0
    for i in range(1,len(ls)):
        if visited[i]==0:
            count += 1
            dfs(visited, ls, i,count)

    result = [ [] for i in range(count+1)]
    for i in range(1,len(ls)):
        result[visited[i]].append(i)
    return count, result

def WriteConnected(result):
    print("Liczba spójnych składowych: ", result[0])
    for i in range(1,result[0]+1):
        print("Spójna składowa #1: ", end="")
        for j in range(len(result[1][i])):
            print(result[1][i][j], end=" ")
        print()

WriteConnected(SplitGraph(CreateGraph(10,10)))