blocks = [100, 500, 200, 300, 600]
process = [212, 417, 112, 426, 80, 2, 900]
m = len(blocks)
n = len(process)
allocation = [-1]*n
for i in range(n):
    index = -1
    worst = min(blocks)
    for j in range(m):
        if blocks[j]>=process[i]:
            if blocks[j]>=worst:
                worst = blocks[j]
                index = j
    if index != -1:
        allocation[i]=worst
        blocks[index] -= process[i]
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
memory blocks after  1  process --> [100, 500, 200, 300, 388]
memory blocks after  2  process --> [100, 83, 200, 300, 388]
memory blocks after  3  process --> [100, 83, 200, 300, 276]
memory blocks after  4  process --> [100, 83, 200, 300, 276]
memory blocks after  5  process --> [100, 83, 200, 220, 276]
memory blocks after  6  process --> [100, 83, 200, 220, 274]
memory blocks after  7  process --> [100, 83, 200, 220, 274]

Process No.    Process Size            Block
     1            212                   600
     2            417                   500
     3            112                   388
     4            426                   Not Allocated
     5            80                    300
     6            2                     276
     7            900                   Not Allocated
     
'''