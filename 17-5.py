SOLUTION = "RGBY"

def check(guess, solution):
    solutionArr = [0,0,0,0]
    hit = 0
    pseudo = 0

    for i in xrange(len(guess)):
        if guess[i] == solution[i]:
            hit += 1
            solutionArr[i] = 1

    for i in xrange(len(guess)):
        for j in xrange(len(solution)):
            if guess[i] == solution[j] and guess[i] != solution[i] and solutionArr[j] == 0:
                pseudo += 1
                solutionArr[j] = 1

    return (hit, pseudo)

guess1 = "RGBY"
guess2 = "XXXX"
guess3 = "BBBB"
guess4 = "GGRR"
print check(guess1, SOLUTION)
print check(guess2, SOLUTION)
print check(guess3, SOLUTION)
print check(guess4, SOLUTION)
