## HW4 AMD ##

import json
import numpy
import networkx as nx
import time
from pylab import show
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
from itertools import count
from Distances import*
from Centrality_measures_plots import*


######  PART 1  ######

## Create a graph with weighted edges

# Read json file and load data
#fo = open('reduced_dblp.json', 'r')  #reduced dataset
fo = open('full_dblp.json', 'r')  #full dataset
data = fo.read()
fo.close()

dataset = json.loads(data)

# Initialize dictionary structures
authors_dict = {}
conf_dict = {}
public_dict = {}

def dictionaryInIt():
    for line in dataset:
        value = []
        authorIdSet = set()
        for aut in line['authors']:
            authorIdSet.add(aut['author_id'])
            if aut['author_id'] in authors_dict:
                authors_dict[aut['author_id']][1].append((line['id_publication'], line['id_publication_int']))
            else:
                authors_dict[aut['author_id']] = [aut['author'],[(line['id_publication'], line['id_publication_int'])]]
        value.append(list(authorIdSet))
        if line['id_publication_int'] in public_dict:
            public_dict[str(line['id_publication_int'])].append(public_dict[line['id_publication_int']][0].extend(value[0]))
            public_dict[str(line['id_publication_int'])] = filter(None, public_dict[str(line['id_publication_int'])])
        else:
            value.append(str(line['id_publication']))
            public_dict[str(line['id_publication_int'])] = value
        a = line['id_conference']
        if a in conf_dict:
            l = []
            for x in range(len(line['authors'])):
                l.append(line['authors'][x]['author_id'])
            lis = set(l)
            conf_dict[a][1].extend(list(lis))
            conf_dict[a][1] = list(set(conf_dict[a][1]))
        else:
            conf_dict[a] = [line['id_conference_int'], list(set([line['authors'][x]['author_id'] for x in range(len(line['authors']))]))]

dictionaryInIt()

# Create a graph
G = nx.Graph()

# Add authors as nodes
for i in authors_dict.keys():
    G.add_node(i, id=i, name=authors_dict[i][0], publication=authors_dict[i][1])

# Add edges where authors share at least one publication
# Edges should be weighted by Jaccard similarity
t1 = int(round(time.time() * 1000))

for authorList in public_dict.values():
    for i in range(len(authorList[0])):
        j = i+1
        while (j<len(authorList[0])):
            dist = jaccard(authorList[0][i], authorList[0][j], authors_dict)
            if dist != 0:
                G.add_edge(authorList[0][i], authorList[0][j], weight=1-dist)
            j += 1

print(int(round(time.time() * 1000)) - t1)

# Obtain info about the graph
nx.info(G)
nx.is_connected(G)


######  PART 2  ######

## Point 2.a

## Given a conference in input, return the subgraph induced by the set of authors who published at the input
## conference at least once and compute some centrality measures

# Insert a conference as input
q = input('Insert a conference name')
# conf/iitsi/2010 example

# Set of authors who published at the conference
nodes_of_subgraph = conf_dict[q][1]
len(nodes_of_subgraph)

# Create a subgraph
T = nx.Graph(G.subgraph(nodes_of_subgraph))

# Get info of the subgraph
nx.info(T)
nx.is_connected(T)


# Compute centrality measure: degree
degree = nx.degree_centrality(T)
Gt_d = most_important(T, degree)

# Obtain info about most important nodes
a = []
for n in Gt_d.nodes():
    a.append(authors_dict.get(n)[0])

# Plot degree centrality graph - top nodes
draw_1(T, Gt_d, 'Degree centrality')

# Plot degree centrality graph with color scale
draw_2(T, degree, 'Degree Centrality')


# Compute centrality measure: closeness
close = nx.closeness_centrality(T, distance='weight')
Gt_c = most_important(T, close)

# Plot closeness centrality graph - top nodes
draw_1(T, Gt_c, 'Closeness centrality')

# Plot closeness centrality graph with color scale
draw_2(T, close, 'Closeness centrality')


# Compute centrality measure: betweeness
betw = nx.betweenness_centrality(T, weight='weight', k=100)
Gt_b = most_important(T, betw)

# Obtain info about most important nodes
b = []
for n in Gt_b.nodes():
    b.append(authors_dict.get(n)[0])

# Plot betweeness centrality graph - top nodes
draw_1(T, Gt_b, 'Betweeness centrality')

# Plot betweeness centrality graph with color scale
draw_2(T, betw, 'Betweeness centrality')


## Point 2. b
# Given in input an author and an integer d, get the subgraph induced by the nodes that
# have hop distance at most equal to d with the input author.

author = input('Insert an author')   #paul roe
d = int(input('Insert a number for the hop distance'))

# Find Author_Id given the name
id_author = [(k) for k,v in authors_dict.items() if v[0] == author]
id = int(str(id_author).strip('[]'))

# Get hop distance
hopG = bfs(G, id, d)

# Faster implementation
hop1 = nx.ego_graph(G, id, d, undirected= True, center= True)

# Plot hop distance subgraph
draw_3(hopG, id, author)

# Faster way for big distances
draw_3_bis(hopG, id, author)

######  PART 3  ######


