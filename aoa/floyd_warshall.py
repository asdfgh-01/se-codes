n = int(input("Enter the number of vertices: "))
A = [[0 for j in range(n+1)] for i in range(n+1)]

print("Enter the adjacency matrix:")
for i in range(1, n+1):
    for j in range(1, n+1):
        A[i][j] = int(input())

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            A[i][j] = min(A[i][j], (A[i][k] + A[k][j]))

    print("A{}=\n".format(k))
    for i in range(1, n+1):
        for j in range(1, n+1):
            print(A[i][j], "\t", end="")
        print("\n")
    print("\n")
