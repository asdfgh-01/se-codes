seq = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2, 3]
nof = 4
frames = []
pages = len(seq)
pg_miss, pg_hit, count = 0, 0, 0
for i in seq:
    if i not in frames:
        if(len(frames) == nof):
            frames.remove(frames[0])
            frames.append(i)
            count -= 1
        else:
            frames.append(i)
        pg_miss +=1
        count +=1
    else:
        frames.remove(i)
        frames.append(i)
        pg_hit +=1

    print(f'\n{i}',end='\t')
    a = 0
    for j in range(count):
        print(f'{frames[j]}',end='\t')
        a+=1
    for j in range(nof-a):
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
0       7       1       2       0
3       1       2       0       3
0       1       2       3       0
4       2       3       0       4
2       3       0       4       2
3       0       4       2       3
0       4       2       3       0
3       4       2       0       3
2       4       0       3       2
3       4       0       2       3
hits ->  8
miss ->  6
hit ratio -> 2.00
miss ratio -> 1.50

'''
