def pair(seq,val):
    min = 0
    max = len(seq)-1
    result = []
    while min < max:
        if seq[min] + seq[max] == val:
            result.append((seq[min],seq[max]))
            min += 1
            max -= 1
        elif seq[min] + seq[max] < val:
            min += 1
        else:
            max -= 1
    return result

print pair([1,2,3,4,5], 3)