# input:
#   n - the amount of currency
#   couns - the array of availiable denominations
# output:
#   number of coins needed to exchange amount of cents
n = 39
coins = [1, 5, 10, 25]

#fill in the table "by hand"
s = {1: 1, 2: 2, 3: 3, 4: 4,
     5: 1, 6: 2, 7: 3, 8: 4, 9: 5,
     10: 1, 11: 2, 12: 3, 13: 4, 14: 5,
     15: 2, 16: 3, 17: 4, 18: 5, 19: 6,
     20: 2, 21: 3, 22: 4, 23: 5, 24: 6,
     25: 1}

# build up table from 26 -> n
for i in range(26, n + 1):
    s[i] = 1 + min(s[i - 1], s[i - 5], s[i - 10], s[i - 25])


print s[n]

# # print the whole table:
# from pprint import pprint
# print s
