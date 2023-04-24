n = int(input("Enter the number of items: "))
W = int(input("Enter the capacity of the knapsack: "))
w = [0]*n
p = [0]*n
V = [[0 for j in range(W+1)] for i in range(n+1)]
X = [0]*n

for i in range(n):
    print("Enter the weights and profits of item ", i+1)
    w[i], p[i] = map(int, input().split())

for i in range(1,n+1):
    for j in range(1,W+1):
        if w[i-1] > j:
            V[i][j] = V[i-1][j]
        else:
            V[i][j]=max(V[i-1][j],V[i-1][j-w[i-1]]+p[i-1])
      
print("TABLE -> ")
for i in range(n+1):
    for j in range(W+1):
        print(V[i][j],end="\t")
    print()

i = n
j = W
while i > 0 and j > 0:
    if V[i][j] != V[i-1][j]:
        X[i-1] = 1
        i = i-1
        j = j-w[i]
    else:
        i = i-1

print("\nSOLUTION SET : ")
for i in range(n):
    print(X[i],end="\t")
total_profit = V[n][W]
print("\nTotal Profit =", total_profit)

'''
-----------OUTPUT1-----------
Enter the number of items: 3
Enter the capacity of the knapsack: 6
Enter the weights and profits of item  1
1 10
Enter the weights and profits of item  2
2 15
Enter the weights and profits of item  3
3 40
TABLE -> 
0       0       0       0       0       0       0 
0       10      10      10      10      10      10
0       10      15      25      25      25      25
0       10      15      40      50      55      65

SOLUTION SET : 
1       1       1
Total Profit = 65

-----------OUTPUT2-----------
Enter the number of items: 3 
Enter the capacity of the knapsack: 5
Enter the weights and profits of item  1
1 60
Enter the weights and profits of item  2
2 100
Enter the weights and profits of item  3
3 120
TABLE -> 
0       0       0       0       0       0
0       60      60      60      60      60
0       60      100     160     160     160
0       60      100     160     180     220

SOLUTION SET :
0       1       1
Total Profit = 220
'''
