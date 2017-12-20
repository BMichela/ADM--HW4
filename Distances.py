import networkx as nx

# Calculate Jaccard distance between two sets of publications of two authors
def jaccard(id1,id2, authors_dict):
    list1 = []
    list2 = []
    # take publications
    for t in authors_dict[id1][1]:
        list1.append(t[1])
    for t in authors_dict[id2][1]:
        list2.append(t[1])
    # calculate Jaccard distance
    j = float(len(set(list1).intersection(set(list2))))/(len(set(list1).union(list2)))
    return j


# Hop distance algorithm
def bfs(G, id, distance):
    visited = {}         #level (number of hops) when seen in BFS
    height = 0         #the current level
    unexplored={id:1}  #dict of nodes to check at next level
    while unexplored and not (distance+1 <= height):
        thislevel = unexplored  #advance to next level
        unexplored = {}         #and start a new list (fringe)
        for elem in thislevel:
            if elem not in visited:
                visited[elem] = height  #set the level of vertex v
                unexplored.update(G[elem])  #add neighbors of v
        height = height+1
    hopGraph = G.subgraph(visited.keys())
    nx.set_node_attributes(hopGraph, 'level', visited)
    return hopGraph