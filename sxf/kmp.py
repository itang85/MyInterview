def getNexts(b, m):
    next = []
    next.append(-1)
    k = -1
    for i in range(1, m):
        while k != -1 and b[k + 1] != b[i]:
            k = next[k]
        if b[k + 1] == b[i]:
            k += 1
        next.append(k)
    return next


def kmp(a, n, b, m):
    next = getNexts(b, m)
    print(next)
    j = 0
    for i in range(0, n):
        while j > 0 and a[i] != b[j]:
            j = next[j - 1] + 1
        if a[i] == b[j]:
            j += 1
        if j == m:
            return i - m + 1
    return -1
a = 'asdfghjkabcdaskfjqwfjioqwefhjioswdhjfvoizsal;sjdfklajkjaskldjkbvwevjwevnjklsdhfhsdzjlkfhs'
b = 'ajkjasabc'
print(kmp(a, len(a), b, len(b)))
