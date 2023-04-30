seq = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2, 3]
nof = 4
pages = len(seq)
frames = [-1]*nof
pg_miss, pg_hit, pg_fault = 0, 0, 0
for i in range(pages):
    s = 0
    for j in range(nof):
        if seq[i] == frames[j]:
            s+=1
            pg_hit += 1
            pg_fault -= 1
    pg_fault += 1
    if (pg_fault<=nof and s==0):
        frames[i]=seq[i]
        pg_miss +=1
    elif s==0:    
        frames[(pg_fault-1) % nof] = seq[i]
        pg_miss += 1
    print(f'\n{seq[i]}',end='\t')
    for j in range(nof):
        if frames[j] != -1:
            print(f'{frames[j]}',end='\t')
        else:
            print('-',end='\t')
print()
print('hits -> ',pg_hit)
print('miss -> ',pg_miss)         
print('hit ratio -> %.2f' %(pg_hit/nof))
print('miss ratio -> %.2f'%(pg_miss/nof))

'''
------------------------------OUTPUT------------------------------

7       7       -       -       -
0       7       0       -       -
1       7       0       1       -
2       7       0       1       2
0       7       0       1       2
3       3       0       1       2
0       3       0       1       2
4       3       4       1       2
2       3       4       1       2
3       3       4       1       2
0       3       4       0       2
3       3       4       0       2
2       3       4       0       2
3       3       4       0       2
hits ->  7
miss ->  7
hit ratio -> 1.75
miss ratio -> 1.75

'''
