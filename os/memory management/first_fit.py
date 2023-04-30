blocks = [100, 500, 200, 300, 600]
process = [212, 417, 112, 426, 80, 2, 900]
m = len(blocks)
n = len(process)
allocation = [-1]*n

for i in range(n):
    for j in range(m):
        if blocks[j]>=process[i]:
            choosen = blocks[j]    
            allocation[i] = choosen
            blocks[j] -= process[i]
            break
    print('memory blocks after ',i+1,' process -->',blocks)

print()
print("Process No.    Process Size            Block")
for i in range(n):
    print('    ',i + 1, "          ", process[i],end = "\t\t\t")
    if allocation[i] != -1:
        print(allocation[i])
    else:
        print("Not Allocated")
'''
------------------------------OUTPUT------------------------------

memory blocks after  1  process --> [100, 288, 200, 300, 600]
memory blocks after  2  process --> [100, 288, 200, 300, 183]
memory blocks after  3  process --> [100, 176, 200, 300, 183]
memory blocks after  4  process --> [100, 176, 200, 300, 183]
memory blocks after  5  process --> [20, 176, 200, 300, 183]
memory blocks after  6  process --> [18, 176, 200, 300, 183]
memory blocks after  7  process --> [18, 176, 200, 300, 183]

Process No.    Process Size            Block
     1            212                   500
     2            417                   600
     3            112                   288
     4            426                   Not Allocated
     5            80                    100
     6            2                     20
     7            900                   Not Allocated
     
'''