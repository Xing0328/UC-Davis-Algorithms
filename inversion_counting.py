def count_inversions(a):
    # print a
    inv_count = 0
    for i in range(len(a)):
        for j in range(i, len(a)):
            if i < j and a[i] > a[j]:
                inv_count += 1
    # print "*" * inv_count
    return inv_count

def brute_force(length):
    """The strategy here is to emperically find the number of inversions.
        We look at all permutations, count the inversions for each,
        and return the average (expected) number of inversions."""
    import itertools
    a = itertools.permutations(range(length))
    totals = []
    for l in a:
        totals.append(count_inversions(l))
    print "bf # of inversions: ", sum(totals) / float(len(totals))

def using_irv(n):
    """The odds of picking 2 distinct numbers, and having one be larger
        than the other is 1/2.  with n numbers in our array, we know the
        the sum of (1 + 2 + 3 + ... + n-1) * 1/2 then, will count the expected
        number of inversions."""
    print "irv # of inversions: ",  (n * (n - 1) / 2.0) / 2.0


if __name__ == "__main__":
    """# Don't make size > 9 if you're brute forcing ^_^"""
    SIZE = 8
    for x in range(SIZE):
        print "for ", x, "elements:"
        brute_force(x) # this takes O(n!) time
        using_irv(x)   # this runs in O(1) time
        print
