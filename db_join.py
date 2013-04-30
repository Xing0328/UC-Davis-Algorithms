from random import shuffle
from pprint import pprint

A = range(10)
print A
B = range(5, 14)
print B

hash_table = []
in_both_lists = []

#build hash table
for x in A:
    hash_table.append(x)

#check your way through
for x in B:
    if x in hash_table:
        in_both_lists.append(x)

pprint(in_both_lists)


#Could also use python magic...
print [x for x in A if x in B]

