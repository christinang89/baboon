def printmap(map):
    for lst in map:
        print lst
    print "\n"
        

def spiral(map):
    length = len(map)
    begining = 0
    row = 0
    col = 0
    times = length * length
    for i in xrange(len(map)*len(map)):
        print row,col
        if col < length and row <= col:
            #row <= col and col < length - row:            #first row move right
            map[row][col] = "x"
            col += 1
            if col == length:
                row += 1
        elif row < length:
        # row < col and col == length and row < length-1:             # move down
            map[row][col-1] = "x"
            row += 1
            if row == length:
                col+= 1
        elif col < 2 * length and row <= col:
            map[row-1][2*length-col-1] = "x"
            col += 1
            if col == 2*length:
                col = begining
                row += 1
        else:
            map[2*length-row-1][col] = "x"
            row += 1
            if row == 2*length-1:
                row = begining + 1
                col += 1
                begining += 1
                length -= 1
        
        print row,col
        printmap(map)

def spiral2(map):
    row = 0
    col = 0
    end = len(map)
    start = 0

    for i in xrange(len(map)*len(map)):
        if col < end and row <= col:
            map[row][col] = "x"
            col += 1
            if col == end:
                row += 1
        elif row < end and row <= col:
            map[row][col-1] = "x"
            row += 1
            if row == end:
                col-= 1
        elif col > start and row > col:
            map[row-1][col-1] = "x"
            col -= 1
            if col == start:
                row -= 1
        else:
            map[row-1][col] = "x"
            row -= 1
            if row == start + 1:
                col += 1

        if row == start+1 and col == start+1:
            start += 1
            end -= 1
        
        printmap(map)
        print "\n"

def spiral3(map):
    
    def getNewDirection(currentDirection):
        if currentDirection == (0,1):
            return (1,0)
        if currentDirection == (1,0):
            return (0,-1)
        if currentDirection == (0,-1):
            return (-1,0)
        if currentDirection == (-1,0):
            return (0,1)            
    
    def isValid(map, nextSquare):
        (x,y) = nextSquare

        if x < 0 or y < 0 or x >= len(map) or y >= len(map):
            return False
        if map[x][y] == "x":
            return False
        return True

    x = 0
    y = 0
    direction = (0,1)

    for i in xrange(len(map)*len(map)):
        map[x][y] = "x"
        printmap(map)
        nextSquare = (x+direction[0],y+direction[1])
        if not isValid(map,nextSquare):
            direction = getNewDirection(direction)
            nextSquare = (x+direction[0],y+direction[1])
        x = nextSquare[0]
        y = nextSquare[1]





arr = []
for i in xrange(5):
    arr.append([])
    for j in xrange(5):
        arr[i].append("o")

spiral3(arr)