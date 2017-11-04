# Puzzle Solver
This code is a solver for the 8/15 puzzle using Breadth-First Search, Depth-First Search, Greedy Breadth-First Search, or A* Algorithms, as a part of the CSC 3309 Course (Artificial Intelligence) at Al Akhawayn University in Ifrane. The code is written in C++.

The states are defined using the grid configuration (using a 1-dimensional vector for the sake of simplicity), the parent state, and the depth of the state in the search tree. The goal configuration is also taken as input.

### 1. Input
The input of the program is the dimensions of the grid (x, y, z), followed by the initial state of the puzzle (numbers ranging from 1 to n, 0 represents the space), as well as the configuration of the goal state (see the file in.in for an example) The last input of the program is the algorithm to be used (BFS, DFS, GBFS, Astar). By default, the program is set to be taking its input from the file in.in, but feel free to use standard input if you like, by deleting the line 429.

### 2. Output
The output of the program is the depth of the first solution that the algorithm finds, followed by a series of parents of that goal state. The program uses standard output to display this data. For now, and for testing purposes, the program only prints the depth, but feel free to use the already defined function called "PrintAncestors" that displays all the parents of a state, bottom-up.

### 3. I/O Files
Input and Output files can be used with the program. for the default code to work using a file as an input, use in.txt.

### 4. Remarks:
Since the execution of the DFS Algorithm is far from being optimal, the memory reserved for the program may be saturated, and the program may be killed before reaching the goal state. Therefore, it is completely normal for the program to crash especially in that case.

### 5. The Search strategies Comparison:
To compare search strategies, we used many sets of initial states/goal states configurations. While BFS was relatively stable and was somehow optimal, DFS search took a longer time in general, and was even stuck and crashing (see section 4). About informed search, Greedy BFS was unstable in terms of results. It was better than BFS in some cases, and worse in some others. The A* Algorithm was a lot stable and provided results closer, in general, to the original BFS, and was even better in some cases. We can conclude that to solve this puzzle efficiently and reduce the time complexity, a better heuristic function should be used.
