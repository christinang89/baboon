test = [[0,1,2,3],[4,5,6,7],[8,9,10,11],[12,13,14,15]]

def rev(img):
    for i in img:
        for j in xrange(int(len(i)/2)):
            temp = i[j]
            i[j] = i[len(i)-j-1]
            i[len(i)-j-1] = temp
    return img

def flip(img):
    for i in xrange(len(img)):
        for j in xrange(i,len(img)):
            temp = img[i][j]
            img[i][j] = img[j][i]
            img[j][i] = temp
    return img

print flip(rev(test))
