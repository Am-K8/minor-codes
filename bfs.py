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

visited = []
queue = []

def bfs(visited, graph, node):
      visited.append(node)
      queue.append(node)  #enque

    
      while queue:
          m = queue.pop() # dequeue
          print(m ," ->", end = " ")

          for neighbour in graph[m]:
              if neighbour not in visited:
                  visited.append(neighbour)
                  queue.append(neighbour)

print("Following is the Breadth-First Search:")
bfs(visited, graph, 'A')     # function calling


