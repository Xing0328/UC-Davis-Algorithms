# Greedy 1: Activity Scheduling
# A Classroom can accomodate 1 class at a time.


#Problem: Maximize the number of classes such that no two classes overlap.


# definition of conflict:
# --
#    Two activities a[i] = (s[i],f[i]) and a[j] = (s[j],f[j])
#    are in conflict (have overlap) iff
#    (s[i] < s[j] < f[i] or
#     s[i] < f[j] < f[i]    ).

# input : a set of classes a = [(s[i],f[i]), for i in range(n)]
                       #a[i] = (s[i],f[i])

# output: the set of classes which maximize
#   the time that the classroom is used.

#solution:
#

n = 5

"""create a classes array, a: with n entries"""
s, f = [x + 1 for x in range(n)], [(y + 1) ** 2 for y in range(n)]

# you can uncomment the next line to check it out.
print "a = ", [(s[i], f[i]) for i in range(n)]


def greedy_schedule(s, f, verbose=False):
    """s and f are paralell arrays of start and finish times.
    they're already sorted by s."""
    X = [False for p in range(n)]
    a = [(s[i], f[i]) for i in range(n)]
    count = 1
    X[count] = 1
    for i in range(2, n):
        if s[i] > f[X[count]]:
            count += 1
            X[count] = i

    """after this loop, an entry in X will contain either the start time
    of a task (denoting that we should use it) or it will contain False,
    denoting that we should skip it."""
    if verbose:
        set_of_classes = set([])
        for item in X:
            if item:
                set_of_classes.add(item)
        print set_of_classes

greedy_schedule(s, f, verbose=True)




