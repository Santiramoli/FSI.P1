# Search methods

import search
import timeit

# Crear una función que envuelva la llamada a la función que deseas medir
def measure_time(func, *args):
    start_time = timeit.default_timer()
    result = func(*args)
    end_time = timeit.default_timer()
    execution_time = end_time - start_time
    return result, execution_time

ab = search.GPSProblem('A', 'B', search.romania)

print("\nBreadth First Search:\n")
result1, time1 = measure_time(search.breadth_first_graph_search, ab)
print("Recorrido:", result1.path())
print("Tiempo de ejecución:", time1, "segundos \n\n")

print("\nDepth First Search:\n")
result2, time2 = measure_time(search.depth_first_graph_search, ab)
print("Recorrido:", result2.path())
print("Tiempo de ejecución:", time2, "segundos\n\n")

print("\nBranch and Bound:\n")
result3, time3 = measure_time(search.branch_and_bound, ab)
print("Recorrido:", result3.path())
print("Tiempo de ejecución:", time3, "segundos\n\n")

print("\nBranch and Bound Subestimation:\n")
result4, time4 = measure_time(search.branch_and_bound_subestimation, ab)
print("Recorrido:", result4.path())
print("Tiempo de ejecución:", time4, "segundos\n\n")


# Result:
# [<Node B>, <Node P>, <Node R>, <Node S>, <Node A>] : 101 + 97 + 80 + 140 = 418
# [<Node B>, <Node F>, <Node S>, <Node A>] : 211 + 99 + 140 = 450
