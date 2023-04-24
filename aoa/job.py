profit = 0
number = int(input("enter the number of jobs :"))
id = list(map(int,input("enter the jobs :").split()))
profits = list(map(int,input("enter the profit :").split()))
deadline = list(map(int,input("enter the deadline :").split()))
dmax = max(deadline)
slots = [-1]*(dmax)
for i in range(number):
    k = min(dmax, deadline[i])
    while k>=1:
        if slots[k-1]==-1:
            slots[k-1]=id[i]
            profit += profits[id[i]-1]
            break
        k-=1
print('maximum profit sequence of jobs is ->',slots)
print('with a profit of ->',profit)