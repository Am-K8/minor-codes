
graph = {
      'A' : ['B','C','D'],
      'B' : ['A','E','F','C'],
      'C' : ['A','E','F','G'],
      'D' : ['A','G'],
      'E' : ['B','H'],
      'F' : ['B','C','G','F','I'],
      'G' : ['C','G','D','I'],
      'H' : ['E','F','I','K','J'],
      'I' : ['F','G','F','K'],
      'J' : ['J'],
      'K' : ['H','I']
  }


visited = set()   #Set to keep track of visited nodes of graph.

def dfs(visited, graph, node):   #function for dfs 
    if node not in visited:
          print(node ," ->", end = " ")
          visited.add(node)
          for neighbour in graph[node]:
              dfs(visited, graph, neighbour)

print("Following is the Depth-First Search:")
dfs(visited, graph, 'A')


