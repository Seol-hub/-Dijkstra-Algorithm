# Dijkstra Algorithm
import heapq
from collections import deque

def dijkstra(graph, node):
    distances = {i: float('inf') for i in graph}
    from_node = {i: None for i in graph}

    distances[node] = 0

    queue = []
    heapq.heappush(queue, (0, node))

    while queue:
        current_distance, current_node = heapq.heappop(queue)

        for new_node, new_distance in graph[current_node]:
            distance = new_distance + current_distance
            if distance < distances[new_node]:
                distances[new_node] = distance
                from_node[new_node] = current_node
                heapq.heappush(queue, (distance, new_node))

    return distances, from_node

def findPath(from_node, start, goal):
    res = deque()
    node = goal
    while node != start:
        res.appendleft(node)
        node = from_node[node]
    res.appendleft(node)
    return res

graph = {
    "A": [("B", 1), ("C", 4), ("D", 5)],
    "B": [("A", 1), ("D", 2)],
    "C": [("A", 4), ("D", 4), ("E", 3)],
    "D": [("A", 5), ("B", 2), ("C", 4), ("F", 3)],
    "E": [("C", 3), ("F", 2)],
    "F": [("D", 3), ("E", 2)]
}

distances, from_node = dijkstra(graph, 'A')
path = findPath(from_node, 'A', 'F')
print(distances, from_node, path, sep='\n')