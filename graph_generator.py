import networkx as nx
import matplotlib.pyplot as plt
from networkx.drawing import nx_pydot
from graphviz import Source
import math
plt.figure(figsize=(10, 10))

G = nx.MultiDiGraph()

def reversed(tuple):
  newtuple = (tuple[1], tuple[0])
  return newtuple

print("how many pages do you have? ")
a = int(input())
for i in range(a):
  G.add_node(chr(i+65))

nodes_rank = [0 for i in range(a+5)]
linkage = [[float(0) for i in range(a+5)] for j in range(a+5)]
print("input the you final rank result ( the eigenvector ):")

for i in range(a):
  fraction_flag = 0
  str = input()
  for c in str:
    if c == '/':
      fraction_flag = 1
      break
  if fraction_flag == 0:
    nodes_rank[i] = float(str)
  else:
    numerator = ""
    denominator = ""
    meet = 0
    for c in str:
      if c == '/':
        meet = 1
        continue
      if meet == 0:
        numerator += c
      else:
        denominator += c
    nodes_rank[i] = float(numerator) / float(denominator)

print("input the linkage line by line:")

for i in range(a):
  j = 0
  str = input()
  str += " "
  temp = ""
  for c in range(len(str)):
    if str[c] == ' ':
      fraction_flag = 0
      for z in temp:
        if z == '/':
          fraction_flag = 1
          break
      if fraction_flag == 0:
        linkage[i][j] = float(temp)
      else:
        numerator = ""
        denominator = ""
        meet = 0
        for z in temp:
          if z == '/':
            meet = 1
            continue
          if meet == 0:
            numerator += z
          else:
            denominator += z
        linkage[i][j] = float(numerator) / float(denominator)
      temp = ""
      j += 1
    else:
      temp += str[c]

edge_formatter = []

for i in range(a):
  for j in range(a):
    if linkage[i][j] != 0:
      G.add_edge(chr(i+65), chr(j+65))
      edge_formatter.append(math.sqrt((linkage[i][j] * nodes_rank[i] * 100))+10)

val_map = {}
for i in range(a):
  val_map[chr(65+i)] = nodes_rank[i]

values = [val_map.get(node) for node in G.nodes()]
thebiggestnow = 0
thebiggestindex = -1
thesecond = 0
thesecondindex = -1
thethird = 0
thethirdindex = -1

for j in range(a):
  if nodes_rank[j] > thebiggestnow:
    thebiggestnow = nodes_rank[j]
    thebiggestindex = j

for j in range(a):
  if nodes_rank[j] > thesecond and j != thebiggestindex:
    thesecond = nodes_rank[j]
    thesecondindex = j

for j in range(a):
  if nodes_rank[j] > thethird and j != thebiggestindex and j != thesecondindex:
    thethird = nodes_rank[j]
    thethirdindex = j

color_array = []
size_array = []
font_array = []

for i in range(a):
  if i == thebiggestindex:
    color_array.append("gold")
    size_array.append(8000)
    font_array.append(36.0)
  elif i == thesecondindex:
    color_array.append("silver")
    size_array.append(5000)
    font_array.append(30.0)
  elif i == thethirdindex:
    color_array.append("brown")
    size_array.append(1000)
    font_array.append(24.0)
  else:
    color_array.append("blue")
    size_array.append(500)
    font_array.append(20.0)

curved_edges = [edge for edge in G.edges() if reversed(edge) in G.edges()]
curved_edges_formatter = [edge_formatter[i] for i, edge in enumerate(G.edges()) if reversed(edge) in G.edges()]
curved_edges_formatter_index = [i for i, edge in enumerate(G.edges()) if reversed(edge) in G.edges()]
straight_edges = list(set(G.edges()) - set(curved_edges))
straight_edges_formatter = []
for i in range(len(edge_formatter)):
    if i not in curved_edges_formatter_index:
        straight_edges_formatter.append(edge_formatter[i])

options = {
    "font_size": 20,
    "node_size": size_array,
    "node_color": color_array,
    "edgecolors": "black",
    "linewidths": 3,
    "width": 2,
    "arrowsize": 36,
    "arrowstyle": '<|-',
}
node_options = {
    "node_size": 750,
    "node_color": color_array,
    "edgecolors": "black",
    "linewidths": 3,
}
curve_edge_options = {
    "width": 3,
    "arrowsize": curved_edges_formatter,
    "arrowstyle": '<|-',
}
straight_edge_options = {
    "width": 3,
    "arrowsize": straight_edges_formatter,
    "arrowstyle": '<|-',
}
pos = nx.shell_layout(G)
fig, ax = plt.subplots()
nx.draw_networkx_nodes(G, pos, ax=ax, **node_options)
nx.draw_networkx_labels(G, pos, ax=ax)
nx.draw_networkx_edges(G, pos, ax=ax, edgelist=straight_edges, **straight_edge_options)
arc_rad = 0.2
nx.draw_networkx_edges(G, pos, ax=ax, edgelist=curved_edges, connectionstyle=f'arc3, rad = {arc_rad}', **curve_edge_options)