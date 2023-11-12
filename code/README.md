# **README - Practice 1 FSI**

Students: Santiago Ramirez Olivares and Adrián Talavera Naranjo

### **Tasks included:**

1. Implement "Branch and Bound Search."
2. Implement "Branch and Bound Search with Subestimation" using straight-line distance as the problem’s heuristic.
3. Compare the number of expanded nodes in both strategies. 

The first strategy is "Branch and Bound Search," an uninformed technique that prioritizes nodes with lower cost. The second is "Branch and Bound Search with Subestimation," an informed strategy that combines accumulated cost with an heuristic estimation. The graph of the cities of Romania is used as an example.

**Changes in 'run.py':**

Added the function measure_time that returns the traversal of each search algorithm and the execution time of each.

**Changes in 'search.py':**

Implemented the new search algorithms (branch_and_bound and branch_and_bound_subestimation), which are useful for search problems with costs.

Added new metrics (generated nodes, visited nodes, and cost).

**Changes in 'utils.py':**

Improved the 'pop' method of the 'FIFOQueue' class to simplify element removal.

Implemented two new priority queues, 'BranchAndBoundQueue' and 'InformedPriorityQueue,' used in the 'branch_and_bound' and 'branch_and_bound_subestimation' algorithms, respectively.

**Operation of 'BranchAndBoundQueue':**

* Method 'init': Initializes the queue and the initial node.

* Method 'append': Adds an element to the end of the queue, making a call to the 'extend' method.

* Method 'len': Returns the length of the queue.

* Method 'extend': Adds neighboring nodes of the current node to the queue and rearranges the queue based on cost.

* Method 'pop': Extracts the first element from the queue.

**Operation of 'InformedPriorityQueue':**

Shares the methods of the previous class.
The only difference lies in the 'extend' method, which now takes into account the problem's heuristic (new attribute of the class).

The provided heuristic uses the Pythagorean Theorem to calculate the distance between the current node and the destination node.