import string 

input = "aabccccaaa"

def compress(st):
    if len(st) <= 1:
        return st
    first = 0
    last = first+1
    result = ""

    for i in xrange(len(st)):
        if last >= len(st):
            result += st[first]
            result += str(last-first)
        elif st[last] != st[first]:
            result += st[first]
            result += str(last-first)
            first = last
            last += 1
        else:
            last += 1

    if len(result) >= len(st):
        return st
    else:
        return result

print compress(input)
