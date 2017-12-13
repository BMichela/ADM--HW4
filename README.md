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
After obtaining all the necessary information, we constructed the graph with the nodes and the weighted edges. 


###   Module 'Jaccard'  ###

The function 'jaccard' calculates the Jaccard distance between two sets of publications of two authors.
It takes in input the ids of two authors and a dictionary containing the information about the authors 
and returns the distance required. 
The Jaccard distance is calculated as the intersection of two sets divided by their union.


