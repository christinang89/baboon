test = [[0,1,2,3],[4,5,6,7],[8,9,10,11],[12,13,14,15]]

test = [[0,1,2,3],[4,5,6,7],[8,9,0,11],[12,13,14,15]]

def t(input):
    indices = []
    for i in xrange(len(input)):
        for j in xrange(len(input[i])):
            if input[i][j] == 0:
                indices.append([i,j])

    for index in indices:
        for i in xrange(len(input)):
            input[index[0]][i] = 0
        for j in xrange(len(input[0])):
            input[j][index[1]] = 0
    return input

print t(test)
