""" Task 1: By using graph data structure, develop a Python program, which generates the above image.
Replace the edge labels, which are currently letters, with the actual distances between the stations,
in kilometers or miles. Use online map services, such as Apple Maps or Google Maps, to approximate the distances."""

import matplotlib.pyplot as plt
import networkx as nx
from matplotlib.lines import Line2D  # For custom legends

MyGraph = nx.Graph()

# Adding nodes and edges for the graph
# Piccadilly Line
MyGraph.add_node('Hyde_Park_Corner', npos=(35, 35), ccn='#0015ff')
MyGraph.add_node('Green_Park', npos=(50, 50), ccn='#0015ff')
MyGraph.add_node('Piccadilly_Circus', npos=(90, 50), ccn='#0015ff')
MyGraph.add_node('Leicester_Square', npos=(130, 50), ccn='#0015ff')
MyGraph.add_node('Covent_Garden', npos=(145, 60), ccn='#0015ff')
MyGraph.add_node('Holborn', npos=(165, 73), ccn='#0015ff')

MyGraph.add_edge('Hyde_Park_Corner', 'Green_Park', cce='#0015ff')
MyGraph.add_edge('Green_Park', 'Piccadilly_Circus', cce='#0015ff')
MyGraph.add_edge('Piccadilly_Circus', 'Leicester_Square', cce='#0015ff')
MyGraph.add_edge('Leicester_Square', 'Covent_Garden', cce='#0015ff')
MyGraph.add_edge('Covent_Garden', 'Holborn', cce='#0015ff')

# Sets graph attributes
pos = nx.get_node_attributes(MyGraph, 'npos')
nodecolour = nx.get_node_attributes(MyGraph, 'ccn')
edgecolour = nx.get_edge_attributes(MyGraph, 'cce')

NodeList = list(nodecolour.values())
EdgeList = list(edgecolour.values())

plt.figure(figsize=(11, 7))  # define width and height of the graph


text_size = 11
# Piccadilly Label
plt.text(28, 32, s='Hyde Park Corner', size=text_size)
plt.text(43, 52, s='Green park', rotation=15, size=text_size)
plt.text(83, 52, s='Piccadilly Circus', rotation=15, size=text_size)
plt.text(125, 45, s='Leicester Square', rotation=15, size=text_size)
plt.text(150, 60, s='Covent Garden', size=text_size)
plt.text(168, 73, s='Holborn', size=text_size)

# Draw nodes, edges, and edge labels
nx.draw_networkx(MyGraph, pos, node_color=NodeList, with_labels=False)
nx.draw_networkx_edges(MyGraph, pos, edge_color=EdgeList)
nx.draw_networkx_edge_labels(
    MyGraph, pos,
    edge_labels={('Hyde_Park_Corner', 'Green_Park'): '0.9 Km',
                 ('Green_Park', 'Piccadilly_Circus'): '0.5 Km',
                 ('Piccadilly_Circus', 'Leicester_Square'): '0.6 Km',
                 ('Leicester_Square', 'Covent_Garden'): '0.3 Km',
                 ('Covent_Garden', 'Holborn'): '0.5 Km'}
)

# define labels that will get added to legend
Line_label = [Line2D([0], [0], color='#0015ff', lw=2, label='Piccadilly Line')]

# adding custom legend
plt.legend(handles=Line_label, loc='lower right', title="Lines", fontsize=15, title_fontsize=15)

plt.savefig("task1.png")
plt.show()
