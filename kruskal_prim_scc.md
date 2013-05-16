## 5 / 16 / 13

# Topological Sort:

1.  call `DFS(G)` to compute finish time `f[i]` for all `i`.
2.  sort the vertices in reverse order of the `f[i]`'s.
    * i.e. if `g(i)` is the rank, then `g(i) = 2n - f[i] + 1`

### pf:  TS gives a Topoligical sorting of V's.
*   for each `(u,v)` in `E` => `g(v) > g(u)`.

*   Since there are no BE in G, v must either be WHITE or BLACK.  either way `f[v]` < `f[u]`.

*   Then,

            2n - g[v] + 1 < 2n - g[u] + 1
                 =   g[u] < g[v]


## Connectedness in G:
### Undirected:

    G is connected iff for all x, y in V:
        There's a path from x to y.


### Directed

    G is connected if it's undirected G is connected

    G is strongly connected if for all x, y in V:
        There exists a path (x -> y) and (y -> x).


# Strongly Connected Components:

1.  Run `DFS(G)` to get `f[i]`'s
2.  Computer `G' = Transpose(G)`
3.  Run `DFS(G')`
4.  The DFS Forest produced in step 3,
    are the SCCs of G.


### Why are SCC important?

*   Condensation

### Thm: Gc = `Condense(G)` is a `DAG`.

# Minimum Spanning Trees

### Thm: B - 2 (from Section B5)
A tree in an `n`-vertex graph has:
    - n-1 edges
    - no cycles
    - connects every pair of vertices with a unique path
    - if we add an edge, we get a cycle.


### Spanning Tree Definition:

A spanning tree in an `n`-vertex graph: a tree with `n-1` edges.

### Minimal Spanning Tree Definition:

A MST `T` is a spanning tree in a `G = (V, E)` where `T = (V, T_E)` such that:
    `sum( cost(i, j) | all i,j in T_e )` is minimal
    and the size of `T_e` is `|V| - 1`

### General Idea for solving the MST problem.
Given a connected, undirected `G`, with edge weights `w_e` or `w_i`,

    Start with an arbitrary v in V.
    T_v = T_v.append(v)
    T_e = Ø
    Repeat n-1 times
        let e = (u, w) be the cheapest edge
            s.t. u is in T_v and w is not in T_v.

## Kruskal's

    Sort edges st w(e_1) <= w(e_2) <= ... <= w(e_m)
    T = Ø
    for i = 1 to m:
        if e_i does not create a cycle to T
            T.append(e_i)

## Prim's

    Start with an arbirtrary vertex V
    Repeat:
        Find cheapest edge (v, w) via priority queue Q
            (s.t. w is in Adj(v) and w does not create a cycle).
        Add to Q the edges (w, x), for x in Adj(w)

- - -
Proof of correctness


