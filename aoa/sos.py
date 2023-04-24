w = [0]*6
n = s = count = tot_pl = 0
sol = [0]*6

def promising(l, wsf, tpl):
    if wsf + w[l+1] <= s and wsf + tpl >= s:
        return 1
    return 0

def sum_of_subsets(l, wsf, tpl):
    global count
    if wsf == s:
        count += 1
        print(f"Solution Vector {count} : [\t",end="")
        for i in range(1, n+1):
            print(f"{sol[i]}\t", end="")
        print("]")
        print()
    elif promising(l, wsf, tpl):
        sol[l+1] = 1
        sum_of_subsets(l+1, wsf + w[l+1], tpl - w[l+1])
        sol[l+1] = 0
        sum_of_subsets(l+1, wsf, tpl - w[l+1])

n = int(input(" Enter the number of distinct items : "))
for i in range(1, n+1):
    w[i] = int(input(f" Enter the weight of the Item Number {i} : "))
    tot_pl += w[i]
s = int(input(" Enter the Maximum allowed weight : "))
sum_of_subsets(0, 0, tot_pl)

'''
-----------OUTPUT-----------
Enter the number of distinct items : 4
Enter the weight of the Item Number 1 : 1
Enter the weight of the Item Number 2 : 3
Enter the weight of the Item Number 3 : 4
Enter the weight of the Item Number 4 : 5
Enter the Maximum allowed weight : 8

Solution Vector 1 : [  1       1       1       0       ]

Solution Vector 2 : [  0       1       0       1       ]

'''