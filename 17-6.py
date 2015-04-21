
def find(seq):
    seq2 = []
    for i in seq:
        seq2.append(i)
    seq2.sort()
    print seq2
    print seq
    min = 0
    max = len(seq) - 1
    while seq2[min] == seq[min]:
        min += 1
    while seq[max] == seq2[max]:
        max -= 1
    return (min, max)

print find([1,2,4,7,10,11,7,12,6,7,16,18,19])