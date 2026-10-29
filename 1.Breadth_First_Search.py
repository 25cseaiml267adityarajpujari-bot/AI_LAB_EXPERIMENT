
from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    visited.add(start)
    print("BFS Traversal:", end=" ")
    
    while queue:
        vertex = queue.popleft()
        print(vertex, end=" ")
        
    
        for neighbour in graph.get(vertex, []):
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)


graph = {}
n = int(input("Enter the number of vertices: "))

for i in range(n):
    vertex = input(f"Enter vertex {i+1}: ")
    
    neighbours = input(f"Enter adjacent vertices of {vertex} (space-separated): ").split()
    graph[vertex] = neighbours

start = input("Enter the starting vertex: ")
print("\nGraph:", graph)
bfs(graph, start)