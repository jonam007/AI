import itertools
import sys

def tsp(graph):
    n = len(graph)
    if n <= 2:
        return graph[0][1]

    all_points = set(range(n))
    memo = {}
    
    # Calculate the minimum distance between a set of cities and a destination city
    def tsp_dp(visited, current):
        if len(visited) == n:
            return graph[current][0]
        
        visited_set = frozenset(visited)
        if (visited_set, current) in memo:
            return memo[(visited_set, current)]
        
        min_distance = sys.maxsize
        for city in set(range(n)) - set(visited):
            distance = graph[current][city] + tsp_dp(visited + [city], city)
            min_distance = min(min_distance, distance)
        
        memo[(visited_set, current)] = min_distance
        return min_distance

    # Start from the first city (0)
    return tsp_dp([0], 0)

if __name__ == "__main__":
    # Example graph representing distances between cities (replace with your own data)
    graph = [
        [0, 10, 15, 20],
        [10, 0, 35, 25],
        [15, 35, 0, 30],
        [20, 25, 30, 0]
    ]
    
    min_distance = tsp(graph)
    print("Minimum TSP Distance:", min_distance)