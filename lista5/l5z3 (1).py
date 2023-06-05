from json.encoder import INFINITY

def lcsubseq(X, Y, m, n):
    if m == 0 or n == 0:
       return 0
    elif X[m-1] == Y[n-1]:
       return 1 + lcsubseq(X, Y, m-1, n-1)
    else:
       return max(lcsubseq(X, Y, m, n-1), lcsubseq(X, Y, m-1, n))

def lcsubstr(X, Y, m, n, count = 0):
    if (m == 0 or n == 0):
        return count

    if (X[m - 1] == Y[n - 1]):
        count = lcsubstr(X, Y, m - 1, n - 1, count + 1)
 
    count = max(count, max(lcsubstr(X, Y, m, n - 1, 0),
                           lcsubstr(X, Y, m - 1, n, 0)))
 
    return count

s = "konwalia"
t = "zawalina"
print (lcsubstr(s, t, len(s), len(t)))

s = "ApqBCrDsEF"
t = "tABuCvDEwxFyz"
print (lcsubseq(s, t, len(s), len(t)))