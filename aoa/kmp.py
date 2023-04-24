def KMPSearch(pat, txt):
    M = len(pat)
    N = len(txt)
    lps = [0]*M
    i, j = 0, 0
    computeLPSArray(pat, M, lps)
    while i < N:
        if pat[j] == txt[i]:
            i += 1
            j += 1
        if j == M:
            print (" Pattern found at index : " + str(i-j))
            j = lps[j-1]
        elif i < N and pat[j] != txt[i]:
            if j != 0:
                j = lps[j-1]
                i+=1
            else:
                i += 1
  
def computeLPSArray(pat, M, lps):
    len =0
    i = 1
    while i < M:
        if pat[i]== pat[len]:
            len += 1
            lps[i] = len
            i += 1
        else:
            if len != 0:
                len = lps[len-1]
            else:
                lps[i] = 0
                i += 1
    print('lps table :')
    print(lps)

txt = str(input(" Enter the text : "))
pat = str(input(" Enter the pattern : "))
KMPSearch(pat, txt)

'''
-----------OUTPUT1-----------
Enter the text : abcdabcf
Enter the pattern : abc
lps table :
[0, 0, 0]
Pattern found at index : 0
Pattern found at index : 4

----------OUTPUT2-----------
Enter the text : abcababd
Enter the pattern : ababd
lps table :
[0, 0, 1, 2, 0]
Pattern found at index : 3

'''