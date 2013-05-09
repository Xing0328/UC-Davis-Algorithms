from random import randint
from collections import namedtuple #for quick structs

# define the struct structure
Good = namedtuple("Good", "v w")

# struct usage:
# g = Good(3, 4)
# print g

def init_input(n=5):

    pre_g = []
    for j in xrange(n):
        v = randint(1, 9)
        w = randint(1, 9)
        this_good = Good(v, w)
        pre_g.append(this_good)
    # pre_g = [(v[i], w[i]) for i in xrange(n)]


    #sort by value per weight:
    g = sorted(pre_g, key=lambda g: float(g.v)/g.w)
    g.reverse()
    # at this point, g is sorted by g.v / g.w decreasing.
    return g



# allowed to take fractions of any item.
# output: a set of f[1], f[2], ... f[n] where
# f[k] is the fraction we take of item k (0 <= f[k] <= 1)

def fractional_knapsack(g, W=4):
    n = len(g)
    F = [0.0 for x in range(n)]
    R = W
    i = 0
    while R > 0 and i < n:
        if R >= g[i].w:
            F[i] = 1
        else:
            F[i] = float(R) / g[i].w
        R -= g[i].w
        i += 1
    return F


n = 7
g = init_input(n)

F = fractional_knapsack(g, 15)

for x in range(len(g)):
    print g[x], " Take: ", F[x]
