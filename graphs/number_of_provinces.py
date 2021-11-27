# description: https://leetcode.com/problems/number-of-provinces
# tags: amazon

def findCircleNum(isConnected):
    visited = [False for i in range(len(isConnected))]
    count = 0
    for v in range(len(isConnected)):
        if visited[v] == False:
            dfs(v, visited, isConnected)
            count += 1
    return count
    
    
def dfs(v, visited, graph):
    visited[v] = True
    
    for j in range(len(graph[v])):
        if graph[v][j] == 1 and visited[j] == False:
            dfs(j, visited, graph)

a = [[1,0,0,1],[0,1,1,0],[0,1,1,1],[1,0,1,1]]
print(findCircleNum(a))

# Time complexity: O(n*2), where n is the number of nodes in the graph
# Space complexity: O(n*2)