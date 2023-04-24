def lcs(x, y):
    m = len(x)
    n = len(y)
    c = [[0 for j in range(n+1)] for i in range(m+1)]
    b = [['' for j in range(n+1)] for i in range(m+1)]

    for i in range(1, m+1):
        for j in range(1, n+1):
            if x[i-1] == y[j-1]:
                c[i][j] = c[i-1][j-1] + 1
                b[i][j] = 'diagonal'
            else:
                if c[i-1][j] >= c[i][j-1]:
                    c[i][j] = c[i-1][j]
                    b[i][j] = 'up'
                else:
                    c[i][j] = c[i][j-1]
                    b[i][j] = 'left'

    for i in range(n+1):
        print(c[i])
    return c[m][n], get_lcs(b, x, m, n)


def get_lcs(b, x, i, j):
    if i == 0 or j == 0:
        return ''
    if b[i][j] == 'diagonal':
        return get_lcs(b, x, i-1, j-1) + x[i-1]
    elif b[i][j] == 'up':
        return get_lcs(b, x, i-1, j)
    else:
        return get_lcs(b, x, i, j-1)


x = input("Enter the first string: ")
y = input("Enter the second string: ")
length, subseq = lcs(x, y)
print("The longest common subsequence length is:", length)
print("The longest common subsequence is:", subseq)

'''
-----------OUTPUT-----------
Enter the first string: abcdaf
Enter the second string: acbdaf
[0, 0, 0, 0, 0, 0, 0]
[0, 1, 1, 1, 1, 1, 1]
[0, 1, 1, 2, 2, 2, 2]
[0, 1, 2, 2, 2, 2, 2]
[0, 1, 2, 2, 3, 3, 3]
[0, 1, 2, 2, 3, 4, 4]
[0, 1, 2, 2, 3, 4, 5]
The longest common subsequence length is: 5
The longest common subsequence is: abdaf
'''