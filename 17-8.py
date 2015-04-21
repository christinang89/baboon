def find(seq):
    if len(seq) <= 1:
        return "blah"
    maxSum = 0
    sum = 0

    for i in xrange(len(seq)):
        sum += seq[i]
        if sum > maxSum:
            maxSum = sum
        elif sum < 0:
            sum = 0
    return maxSum

print find([2,-8,3,-2,4,-10])