# 5/9/2013

### Midterms Returned

* average = 76
* median = 78
* std. dev = 10

## Greedy wrapup

### fractional knapsack:

You're a theif, and you need to maximize the value of the stuff you can snatch, but you can only carry items that fit in your bag.

Each object has a Weight, and a Value; and can be broken up into a fractional size.

How would you do that?

Fractional means you can break up items into fractions `0 <= f <= 1`

### Optomization problem:

We can abstract away the bag and items, if we focus on finding `f[i]` such that we maximize the sum of `f[i]` * `v[i]` (where f is the function to be optomized)
given the constraint that summing all of `f[i]` * `w[i]` = W.

Weight of taken items = sum(f[i] * w[i] for i in range(bag_size))

    1.  Sort the items in G by their v[i]/w[i] value, in decreasing order
    2.  F = (0,0,0,...,0), R <- W, i <- 1
    3.  While (R > 0 and i <= n):
    4.      if (R >= W[i]):
    4a.         f[i] = 1    (take this item)
    5.      else:
    5b.         f[i] <- R/w[i]
    6.      i += 1
    7. end-while
    8. return F.


Prove correctness:

## Thm: Greedy gives an optimal solution for fractional knapsack.
## Pf:

What does a greedy solution look like?

    F = (1, 1, 1, 1, 1, 1, 1, 1, f[i], 0, 0, 0, 0, 0, 0)
        ^------------v---------^   |  ^-------v--------^
            We take all of these   |    We take none of these.
            items.                 |
                        This it the last item we insert,
                        and we insert it partially

For contradiction, let the optimal solution be at least as good as greedy, and "look" different than the greedy pattern solution.

Then there exists `i`,`j` s.t. `f[i]*` < 1 and `f[j]*` > 0, `i < j`.


    f[i]*  is  the ith fraction in opt.

    greedy = 1  1  1   1  1  .5  0  0  0
       opt = 1  1  .8  1  1  .9  0  0  0
                    ^----v---^
                this optimal solution must still fill the bag,
                so if it is different anywhere in the 1's section of
                the greedy pattern, then we must take more of another item.


since such i, j must exist, then we can add "more" of item `g[i]`, and less of `g[j]` for at least as good a solution as opt.

### Note: replace part of item j with other other item i

r = min(`f[j]*` * w[j], (1 - `f[i]*`) * w[i])




## Graph Algorithms Review
Graph = (V, E)
====
where E is a subset of (V x V)

- how to organize it?
    - adj lists
    - adj matrix
    - hash tables? (hint)
    - Density of graphs
        - sparse
        - dense

### Notable graph algorithms:
* search
* connectivity
* connected components
* shortest path
* spanning tree

# Search:
## BFS
(uses a queue to traverse a graph)

(think of an expanding circle)

    set all verticies to unmarked
    while there is an unmarked vertex u
        visit and mark u
        ENQUEUE(Q, u)
        while Q not empty:
            x <- DEQUEUE(Q)
            for each unmarked w in the adj. list of x:
                visit & mark w
                ENQUEUE(Q,w)

## DFS
(uses recursion to traverse a graph to the ground before returning)

(think lightning bolts)

    set all vertices to unmarked
    while there is an unmarked vertex u
        DFS_visit(G,u)

DFS_visit:

    visit and mark u
    while there is an unmarked w in adj. list of u:
        DFS_visit(G,w)
