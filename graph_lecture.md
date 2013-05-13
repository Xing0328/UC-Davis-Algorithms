
### Lecture Notes for Wed, 5/10/13

## Graphs - Ch. 22

* Representation
* BFS
* DFS
* Topological Sort (Top Sort)

#### Graph Questions:
1.  are two nodes (a, b) connected?
*   Is the graph connected?
*   What's the shortest path between two nodes?
*   What's the cheapest way to connect everything? (MST)


# What is a graph?

#### Def: A Graph is a tuple, G = (V, E)

where V is a set of vertices:  (a.k.a. elements, nodes)

    V = {v[1], v[2], ... v[n]}


and E is a set of edges between them:  (a.k.a. links, connections, relationships)


    E = {(V[i],V[j]) | V[i], V[j] 'in' V}

##### Example:

    G = {(A, C), (A, E), (B, C), (B, D), (C, E), (C, D)}

or, in the .dot language:

    graph G {
        A -- C;
        A -- E;
        B -- C;
        B -- D;
        C -- E;
        C -- D;
    }

Which creates:

![alt](./images/lecture.jpg "(with graphviz)")


#### Def: A Directed graph is a Graph, where the order of the edges matters.

    digraph G {
        A -> C;
        A -> E;
        B -> C;
        B -> D;
        C -> E;
        C -> D;
    }

![alt](./images/digraph.jpg "(with graphviz)")


# Graph Representation:

## Adjacency Matrix
* draw matrix, explain Size, explain:

    M[i,j] = 1 iff there's an edge (V_i, V_j)


## Adjacency List
*   Array of lists.
    *   draw the structure: Array of nodes with linked lists coming off each vertex.
    *   explain the size


### Efficiency of operations:
Adjacency Matrix

    Insert      O(1)
    Delete      O(1)
    Find        O(1)
    Space       O(V)

 - - -



Adjacency List

            best    |   expected  |   worst   |  sparse
    - - - - - - - - + - - - - - - + - - - - - + - - - - - -
    Insert  O(1)    |   O(1)      |   O(1)    |  O(1)
    Delete  O(1)    |   O(V)      |   O(V/E)  |  O(1)
    Find    O(1)    |   O(V)      |   O(V/E)  |  O(1)
    - - - - - - - - + - - - - - - + - - - - - + - - - - - -
    Space   O(V)    |   O(1)      |   O(1)    |  O(n)

#### Def: Sparse Graph
A graph can be defined as Sparse when the number of edges is O(V).  Most graphs are sparse.  That's why we typically use adjacency lists to represent them.




