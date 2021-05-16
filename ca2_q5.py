# date : 25/05/2021
# Author : Renato Gusani
# Student no. : x19411076
# Question - Q5 - Undirected – Unweighted Coastal City Graph (Tokyo) – BFS algorithm

# * * * * * * * * * * question 5) * * * * * * * * * *

# a dict information structure, where every vertex has a put away rundown of its nearby node
# undirected unweighted vertices and edges (cities and transports lines)
graph = {'Tokyo': ['Kawaguchi', 'Soka', 'Ichikawa'],
'Kawaguchi': ['Chofu'],
'Soka': ['Matsudo'],
'Ichikawa': ['Kawasaki'],
'Chofu': ['Saitama'],
'Matsudo': [],
'Kawasaki': [],
'Saitama': []}


visited_list = [] # list that is utilized to monitor visited nodes
frontier_queue = [] # list that is utilized to monitor nodes right now in the queue

# Breadth-first search function
def breadth_first_search(visited_list, graph, node):
  visited_list.append(node)
  frontier_queue.append(node)

  while frontier_queue:
    coastal_city = frontier_queue.pop(0) 
    print (coastal_city, end = " ") 

    for neighbour in graph[coastal_city]:
      if neighbour not in visited_list:
        visited_list.append(neighbour)
        frontier_queue.append(neighbour)

# driver
breadth_first_search(visited_list, graph, 'Tokyo')