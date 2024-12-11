from collections import defaultdict


def calcEquation(equations, values, queries):
    # Time: O(q*)
    # step 1: build a graph with a weighted edge
    # a -> b : value
    # b -> a : 1/value
    graph = defaultdict(list)
    for i, equation in enumerate(equations):
        a, b = equation
        graph[a].append((b, values[i]))
        graph[b].append((a, 1 / values[i]))

    # step 2: dfs to find path and compute result
    def dfs(source, target, visited):
        if source not in graph or target not in graph:
            return -1.0
        if source == target:
            return 1.0
        visited.add(source)
        for neighbor, weight in graph[source]:
            if neighbor not in visited:
                result = dfs(neighbor, target, visited)
                if result != -1.0:  # if path found, calculate result
                    return result * weight
        return -1.0

    # answer each query using dfs
    results = []
    for query in queries:
        results.append(dfs(query[0], query[1], set()))
    return results


equations = [["a", "b"], ["b", "c"]]
values = [2.0, 3.0]
queries = [["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]]
print(
    calcEquation(equations, values, queries)
)  # [6.00000,0.50000,-1.00000,1.00000,-1.00000]

equations = [["a", "b"], ["b", "c"], ["bc", "cd"]]
values = [1.5, 2.5, 5.0]
queries = [["a", "c"], ["c", "b"], ["bc", "cd"], ["cd", "bc"]]
print(calcEquation(equations, values, queries))  # [3.75000,0.40000,5.00000,0.20000]


equations = [["a", "b"]]
values = [0.5]
queries = [["a", "b"], ["b", "a"], ["a", "c"], ["x", "y"]]
print(calcEquation(equations, values, queries))  # [0.50000,2.00000,-1.00000,-1.00000]
