from itertools import combinations
'''
FEP is the Fragile Exchange Property
I learned about this in Discrete Math 1
my Freshman year of college.
After finishing this project for
extra credit, I was still looking into
this topic and found out that it is
actually called Matroid Theory, and
the prof made up FEP so that we couldn't
go to google for answers...
'''

k = 3
n = 2

comb = list(map(set, combinations(range(1, k + 1), n)))
sets = []
for i in range(len(comb) + 1):
    sets += (list(map(list, combinations(comb, i))))

def checkFEP(A, B, C):
    for a in A:
        for b in B:
            if (b in A) or (a in B):
                continue
            test = A.difference(set([a])).union(set([b]))
            if test in C:
                return True
    return False

def checkFEPTotal(C):
    for A in C:
        for B in C:
            if not B == A:
                test = checkFEP(A, B, C)
                if not test:
                    return False
    return True

FEPSets = list(filter(checkFEPTotal, sets))
print(FEPSets)

def checkMaximalFEP(C):
    for add in comb:
        if add in C:
            continue
        for A in C:
            test1 = checkFEPTotal(A, add, C)
            test2 = checkFEPTotal(add, A, C)
            if (not test1) or (not test2):
                break
            return False
    return True

def findMaximalFEP():
    for C in FEPSets:
        doesCWork = checkMaximalFEP(C)
        if doesCWork:
            return C
        if not doesCWork:
            print("FEP always works")


findMaximalFEP()
