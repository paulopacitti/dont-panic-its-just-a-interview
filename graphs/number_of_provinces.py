# description: https://leetcode.com/problems/number-of-provinces
# tags: amazon

def number_of_provinces(cities):
    visited = [False for i in range(len(cities))]
    count = 0
    for v in range(len(cities)):
        if visited[v] == False:
            dfs(v, visited, cities)
            count += 1
    return count
    
    
def dfs(v, visited, graph):
    visited[v] = True
    
    for j in range(len(graph[v])):
        if graph[v][j] == 1 and visited[j] == False:
            dfs(j, visited, graph)

a = [
    [1,1,0],
    [1,1,0],
    [0,0,1]
]
print(number_of_provinces(a))

# Time complexity: O(n*2), where n is the number of nodes in the graph
# Space complexity: O(n*2)