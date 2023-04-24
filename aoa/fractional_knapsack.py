def greedy_fractional_knapsack(x,W,p,w,n):
    weight, profit = 0,0
    for i in range(n):
        if weight+w[i]<=W:
            x[i]=1
            weight += w[i]
            profit += p[i]
        else:
            x[i] = (W-weight)/w[i]
            weight = W
            profit += (p[i]*x[i])
            return profit
#input is in ascending order of ratios
n = int(input('enter the number of elements :'))
W = int(input('enter the capacity of sack :'))
w = list(map(int,input('enter the weights : ').split()))
p = list(map(int,input('enter the values : ').split()))
x = [0]*n
profit = greedy_fractional_knapsack(x,W,p,w,n)
print('profit : %.2f'%profit)
print('solution set ')
for i in range(n):
    print('%.2f' %x[i], end = '\t')

'''

-----------OUTPUT1-----------
enter the number of elements :3
enter the capacity of sack :50
enter the weights : 10 20 30
enter the values : 60 100 120
profit : 240.00
solution set
1.00    1.00    0.67

-----------OUTPUT2-----------
enter the number of elements :1
enter the capacity of sack :10
enter the weights : 30 
enter the values : 500
profit : 166.67
solution set
0.33

'''