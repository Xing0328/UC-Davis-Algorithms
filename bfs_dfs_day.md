# May 14 2013


# Breadth First Search: BFS
#### (Spaning Tree producer)

### Properties:
BFS builds a BFS tree (forest), where:
*   π[i] is the shortest distance (in number of edges) between
i and the root
*   CC[i] is i's connected component.
    * CC[i] == CC[j] iff i is reachable from j.


```
1.  unmark all vertices
2.  d[i] = inf.; π[i] = NIL; CC[i] = 0; COMP = 0
3.  while there exists an unmarked S in G
4.      d[s] = 0; π[s] = NIL; CC = CC + 1; Comp = 0; Q = Ø
5.      mark S
6.      ENQUEUE(Q,S)
7.      while Q is not empty:
8.          u = DEQUEUE(Q)
9.          for each v in Adj(u) where v is unmarked:
10.              mark v
11.             d[v] = d[u] + 1; π[v] = u; CC[v] = CC[u]
```
(Note: for step 8, whatever is in Q has just been marked, and many sources will distinguish this by using white, gray, and black in lieu of "marked").


![alt](./images/lecture_bfs_example.jpg "(with graphviz)")

walking through:

Q =  `A`, `Ø`, `BD`, `DC`, `C`, `Ø`
----

## Runtime Analysis:

- each vertex gets enqueued and dequeued exactly once. = `O(V)`
- vertices are discovered by exploring Adj. Lists. = `O(V+E)`
=> `O (V + E)`
----

## Uses:

- shortest path (unweighted)
- spanning tree
- connected components

# Depth First Search: DFS

```
DFS:
1.  for each v in G:
2.      color[v] = WHITE; π[v] = NIL;
3.  time = 0;
4.  for each u in G:
5.      if color[u] = WHITE
6.      DFS_VISIT(u)

```



```
DFS_visit(u):
1.  time = time + 1; d[u] = time; color[u] = GRAY
2.  for each V in Adj(u):
3.      if color[v] = WHITE
4.      π[v] = u
5.      DFS_visit(u)
6.  color[u] = BLACK  //explored
7.  time = time + 1
8.  f[u] = time
```

*   d[u] means discovered time - when we first find a node
*   f[u] means finished time - when we leave a node

## G with  d / f marked in:
![alt](./images/lecture_dfs_example.jpg "(with graphviz)")

## DFS Forest:
![alt](./images/lecture_dfs_forest_example.jpg "(with graphviz)")

notice the difference between `G = (V, E)` and `DFS_Forest = (V, E_π)`  i.e. there are some edges in G which are not in DFS_Forest. like `(A, D)`.

## DFS can be used to categorize G's edges.
1.  Tree Edges:
    *   `(u,v)` is a Tree Edge (`TE`) if `π[v] = u`.
2.  Back Edges:
    *   `(u,v)` is a Back Edge (`BE`) if `v` is an ancesstor of `u` in a DFS tree.
    * NB: If we find a back edge, then we have a cycle.
3.  Forward Edges:
    *   `(u,v)` is a forward edge (FE) if `u` is an ancestor of v, but `(u,v)` is not a tree edge.
4.  Cross Edges:
    *   (all others)~


## Thm: In undirected graphs we can only have `TE`'s or `BE`'s

## Classifying G's Edges using DFS:

    color:       edge Type
    =========+=================
    WHITE    |   Tree Edge
             |
    GRAY     |   Back Edge
             |
    Black    |   Forward Edge


## Def: Acyclic
### G is acyclic if there is no such vertex `v` such that there exists a path from v to v of length > 1.

## Thm: A graph G is acyclic iff DFS(G) yeilds no back edges.

#### Pf:
A -> B
*   Let DFS produce a `BE`, `(u,v)`.
*   Therefore, `v` is an ancestor of `u` in the DFS forest. So there is a path from 'v' to 'u'.
*   But we already know there's a path from `u` to `v`!
*   Thus, '(u,v)' closes a cycle.

B -> A
*   let `C` be a cycle in `G`.
*   let V be the first vertex of c discovered by DFS(G).
*   then we know that V has an edge going out on `C`, and an edge coming in from a node `v` on `C`.
*   `(u,v)` would be marked a `BE` by DFS.

# Topological Sort (Topsort)
## Def: An ordering of G's vertices such that if `(u,v)` is in `E`, then `u` comes before `v` in the ordering.  Only possible for Directed Acyclic Graphs (DAGs).

