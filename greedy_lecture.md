Review
==

Dynamic Programming:
--
- optimality of subproblems
- overlapping subproblems
-> we notice there is a recurrence

Divide and Conquer:
--
- subproblems not overlapping.

finally:
Algorithms
Instances
Solutions

Greedy
====
- Optimality of sub-problems
- FAST
    - doesn't have to look at arrays.
- Greedy Choice
    - don't worry about anything but the next step.

Optimization Problems
=====
Minimizing (or Maximizing) a function.

A(Instance) = Solution
Opt(Instance) = Optimal Solution //this is also called an oracle.


Greedy 1: Activity Scheduling
====
A Classroom can accomodate 1 class at a time.


Problem: Maximize the time used such that we find the largest subset without conflicts

definition of conflict:
--
   Two activities a[i] = (s[i],f[i]) and a[j] = (s[j],f[j])
   are in conflict (have overlap) iff

    s[i] < s[j] < f[i] or s[i] < f[j] < f[i]

 input : a set of classes a = [(s[i],f[i]), for i in range(1,n)]
                      a[i] = (s[i],f[i])
 output: the set of classes which maximize the time that the classroom is used.

solution:
--
overview:
1.  Enumerate all subsets of {a[1], a[2], ..., a[n]}
2.  Check if there are conflicts
3.  Return the largest subst without conflicts.

algorithm:

    1.  sort tasks by finish time.
    2.  choose the first task, which has finish time f[k]
    3.  while (there are still more classes)
        3a. skip to time f[k], choose the first class with time f[k+1]


Therom: The greedy schedule is an optimal schedule.
====
Lemma:
The first class in the schedule must be included, since it has the earliests ending time.

Proof:
----
Constrast the greedy schedule and an optimal schedule, find the first difference between the two, and argue that the greedy choice would have worked as well.

    g1, g2, g3, g4, ... gj-1, gj, cj+1 ... cm
    c1, c2, c3, c4, ... cj-1, cj
                              ^-----Note:
                    Here the greedy must be correct, because
                    at step j, gj will be the best choice, since it will be
                    the next availiable option with the soonest finish time.
