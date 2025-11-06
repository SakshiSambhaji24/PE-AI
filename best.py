from queue import PriorityQueue

# Graph representation
graph = {
    'A': [('B', 2), ('C', 1)],
    'B': [('D', 5), ('E', 3)],
    'C': [('F', 4)],
    'D': [],
    'E': [('G', 1)],
    'F': [('G', 2)],
    'G': []
}

# Heuristic values 
heuristic = {
    'A': 7,
    'B': 6,
    'C': 2,
    'D': 1,
    'E': 4,
    'F': 0,
    'G': 0
}

def best_first_search(start, goal):
    visited = set()
    pq = PriorityQueue()
    pq.put((heuristic[start], start))  # (priority, node)

    while not pq.empty():
        h, node = pq.get()
        print(f"Visiting Node: {node}")

        if node == goal:
            print("Goal reached!")
            return
        
        visited.add(node)

        for neighbor, cost in graph[node]:
            if neighbor not in visited:
                pq.put((heuristic[neighbor], neighbor))

    print("Goal not found!")


best_first_search('A', 'G')
