def steps(n):
    if n < 0:
        return 0
    if n == 0:
        return 1
    
    return steps(n-1) + steps(n-2) + steps(n-3)

print steps(1) # 1
print steps(2) # 2 (1 1, 2)
print steps(3) # 4 (1 1 1, 2 1, 1 2, 3)
print steps(4) # 7 (1 1 1 1, 1 2 1, 1 1 2, 1 3, 2 2, 2 1 1, 3 1)
print steps(5) # 13

def stepsdp(n, map):
    if n < 0:
        return 0
    if n == 0:
        return 1
    if map[n] > -1:
        return map[n]

    map[n] = stepsdp(n-1,map) + stepsdp(n-2,map) + stepsdp(n-3,map)
    return map[n]

arr = []
for i in xrange(101):
    arr.append(-1)

print stepsdp(100,arr)