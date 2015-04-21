# x: row
# y: col

def move(x,y):

    arr = []
    for i in xrange(101):
        arr.append([])
        for j in xrange(101):
            arr[i].append(-1)

    def helper(x,y, paths):
        if x == 0:
            return 1
        if y == 0:
            return 1
        if paths[x][y] > -1:
            return paths[x][y]

        paths[x][y] = helper(x-1, y, paths) + helper(x, y-1, paths)
        return paths[x][y]

    return helper(x,y,arr)

def movesmart(x,y):
    map = [[1,1,1,1],[1,0,1,1],[1,0,1,1],[1,1,1,0]]
    arr = []

    for i in xrange(4):
        arr.append([])
        for j in xrange(4):
            arr[i].append(-1)

    def helper(x,y, paths):
        if map[x][y] == 0:
            return 0
        if x == 0 or y == 0:
            return 1
        if paths[x][y] > -1:
            return paths[x][y]

        paths[x][y] = helper(x-1, y, paths) + helper(x, y-1, paths)
        return paths[x][y]

    return helper(x,y,arr)

print movesmart(2,3)

