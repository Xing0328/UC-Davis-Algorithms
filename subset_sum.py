# input:
# given a set of numbers L ...
# find a subset of L, S s.t.
# the sum of all numbers in S
# is less than but as close as possible to b.
# output:
# the sum that is <= but closest to b.

from pprint import pprint

#example inputs.
"""L - the numbers we can sum with"""
L = [1, 3, 5]

"""b - the number we're trying to sum up to"""
b = 7

"""show_steps lets you see the steps, and outputs all the
numbers you can sum to, which is found either way"""
show_steps = True

table = [False for x in range(b + 1)]
# mark table[0] True => indicates we can sum to 0 (with S = {})
table[0] = True
for number in L:
    # enumerate adds the ability to see indexes of table
    # reversed list lets us move downward through the array
    # so that we're able to move through
    for index, value in reversed(list(enumerate(table))):
            if value is True and index + number <= b:
                table[index + number] = True
                if show_steps:
                    pprint(table)

# now we linear search downward through the table,
# list(enumerate(table)) gives us a list of tuples
#
for wx in enumerate(reversed(list(enumerate(table)))):
    if x[1] is True:
        print x
        break
