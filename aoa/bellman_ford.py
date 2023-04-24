def relax(u,v,dist,V,E):
    d = [float('inf')]*V
    d[0] = 0
    for i in range(V-1):
        for j in range(E):
            if d[v[j]-1] > d[u[j]-1] + dist[j]:
                d[v[j]-1] = d[u[j]-1] + dist[j]
    for i in range(E):
        if d[v[i]-1] > d[u[i]-1] + dist[i]:
            print("Graph contains negative weight cycle")
            return
    print("Vertex Distance from Source")
    for i in range(V):
        print("{0}\t\t{1}".format(i+1, d[i]))

V = int(input('enter the number of vertices : '))
E = int(input('enter the number of edges : '))

u,v,dist = [0]*E,[0]*E,[0]*E

for i in range(E):
    print('enter the start, end and distance :')
    u[i],v[i],dist[i] = map(int,input().split())

relax(u,v,dist,V,E) 

'''
-----------OUTPUT1-----------
enter the number of vertices : 4
enter the number of edges : 4
enter the start, end and distance :
1 2 4
enter the start, end and distance :
1 4 5
enter the start, end and distance :
4 3 3
enter the start, end and distance :
3 2 -10
Vertex Distance from Source
1               0
2               -2
3               8
4               5

-----------OUTPUT2-----------
enter the number of vertices : 4
enter the number of edges : 5
enter the start, end and distance :
1 2 4
enter the start, end and distance :
1 4 5
enter the start, end and distance :
2 4 5
enter the start, end and distance :
4 3 3
enter the start, end and distance :
3 2 -10
Graph contains negative weight cycle
'''