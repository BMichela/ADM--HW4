# ADM--HW4
Homework 4 - Algorithmic Methods of Data Mining

---------------------------------------------------------
----------------    PART 1    --------------------------
---------------------------------------------------------

In this point we have to create a graph G, whose nodes are the authors and they are connected if they 
share at least one publication. To obtain that graph, we initialize three useful dictionary structures which 
contain the information we need:

{author_id: [author_name , [(id_publication, id_publication_int), ...]}

{publication_id: [[authors_id, ...], id_publication_int]}

{conference_id: [id_conference_int, [authors_id, ...]]}

The edges between the nodes are weighted in the following way: w(a1, a2) = 1 − J(p1, p2)
where a1, a2 are authors, p1 and p2 are the set of publications of the two authors and, J(p1, p2) represents 
the jaccard similarity between these two sets of publications.
To calculate the weight we implemented a function that find the jaccard similarity.
After obtaining all the necessary information, we constructed the graph adding the authors as nodes and connecting 
them with weighted edges. 


---------------------------------------------------------
----------------    PART 2    --------------------------
---------------------------------------------------------

Given a conference in input, we need to return the subgraph induced by the set of authors who published at the input 
conference at least once. A vertex-induced subgraph is a subset of the vertices of a graph G together with any edges 
whose endpoints are both in this subset. To construct this subgraph we took information from the conference dictionary 
mentioned above, considering just the authors which participated to a certain conference with a publication and adding them as nodes.

Once obtained the subgraph we can calculate some centrality measures, which give us relative measures of importance in the network. 
We can consider different measures since each of them measures a different type of 'importance'.
The degree centrality corresponds to the number or in our case to the fraction of connections, that a node has in the network. 
The closeness centrality of a node is the reciprocal of the sum of the shortest path distances from that node to all n-1 other 
nodes and since the sum depends on the number of nodes in the graph, the closeness is normalized by the sum of minimum possible 
distances n-1. Remark that our graph is disconnected but the algorithm we used computes the measure for each connected part separately.
The betweeness centrality of a node is the sum of the fraction of all-pairs shortest paths that pass through that node.

On the second point of this part we need to create a subgraph induced by the nodes that have hop distance at most equal to a certain given 
distance from a particular author. Hop distance corresponds to the number of edges from one node to another. 
For doing this we implemented a breadth-first search algorithm for traversing the graph, which explores first the neighbor nodes 
and after pass to the next level of neighbours. 


---------------------------------------------------------
----------------    PART 3    --------------------------
---------------------------------------------------------




---------------------------------------------------------
----------------    MODULES   --------------------------
---------------------------------------------------------

###   Module 'Distances'  ###

This module contains functions concerning distances.

The function 'jaccard' calculates the Jaccard distance between two sets of publications of two authors.
It takes in input the ids of two authors and a dictionary containing the information about the authors 
and returns the distance required. 
The Jaccard distance is calculated as the intersection of two sets divided by their union.

The function 'bfs' is an implementation of the algorithm bfs, that consider the nodes until a certain level from 
a given starting node. The parameters in input corresponds to a graph, the id of the starting node and the hop distance which we want to consider.
The mechanism is that it considers the neighbours of the starting node and adds them to a list, after it skips to the 
second step where it considers the neighbours of the nodes visited at the previous one and add them to the list if they are not
 already present and it repeats this procedure until it reaches the level of the distance given.
The function at the end return a subgraph with the visited nodes in a certain distance and each node has an attribute with containing its level.


###   Module 'Centrality_measures_plots'   ###

This module contains functions concerning the centrality measures and some pretty plots to show the results of these measures.

The function 'most_important' takes in input a graph and a centrality measure and return a graph with as nodes the 10% of 
nodes which are considered the most important given a certain centrality measure.
The output graph is obtained creating a copy of the original graph and removing the nodes that are not in the top positions 
of the sorted values returned by the centrality measure.

The function 'draw_1' provides a way to show the results of a centrality measure. It takes in input a graph, a graph with the 
most important nodes accordingly to the measure used and the name of that measure.
We obtain a plot where we have the structure of the entire graph with the most important nodes highlighted.

The function 'draw_2' provides a different way to show the results of a centrality measure. It takes in input a graph, the 
centrality measure and its name and return a graph where the nodes are colored with respect to their importance. The color 
scale starts from a clear color, which means more importance and ends with a dark color, which means less importance. 

The function 'draw_3' provides a plot of the hop distance with a color scale associated to node distance from a starting node. 
It takes as imput also the the id and the name of the author (identification of the starting node) to create an appositely label on the graph.
The dimensions of the nodes are proportionally to the number of connections they have with the other nodes.
The function 'draw_3_bis' is just a light and faster version (for huge distances) of the previous one, where we don't consider different 
colors for each level of nodes but simply a color for the starting node and one for all the others. 
