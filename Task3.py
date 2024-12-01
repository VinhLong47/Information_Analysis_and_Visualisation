import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
import pandas as pd
from matplotlib.lines import Line2D


def draw_node(graph, node_data):
    for index, row in node_data.iterrows():
        graph.add_node(row['Station_name'], npos=(row['x'], row['y']), ccn=row['Colour'])


def draw_edge(graph, edge_data):
    for index, row in edge_data.iterrows():
        graph.add_edge(row['First_station'], row['Second_station'], cce=row['Colour'], weight=row['Distance'])


# Set path to file
path = str('D:/College Stuffs/OOP/DataInfoLab/Coursework/data/')
# Load CSV file into data frame
station_node_df = pd.read_csv(path + 'station_node_data.csv', delimiter=',')
station_edge_df = pd.read_csv(path + 'station_edge_data.csv', delimiter=',')

MyGraph = nx.Graph()

draw_node(MyGraph, station_node_df)
draw_edge(MyGraph, station_edge_df)


pos = nx.get_node_attributes(MyGraph, 'npos')
nodecolour = nx.get_node_attributes(MyGraph, 'ccn')
edgecolour = nx.get_edge_attributes(MyGraph, 'cce')

NodeList = list(nodecolour.values())
EdgeList = list(edgecolour.values())

plt.figure(figsize=(18, 14))

# Drawing network map
nx.draw_networkx(MyGraph, pos, node_color=NodeList, with_labels=False)

# Highlighting Intercepting nodes
intersecting_nodes = ["Green_Park", "Piccadilly_Circus", "Oxford_Circus", "Charing_Cross", "Leicester_Square",
                      "Warren_Street"]
nx.draw_networkx_nodes(MyGraph, pos, nodelist=intersecting_nodes,
                       node_color='white', edgecolors='black', linewidths=2, node_size=300)

# Drawing Edges
nx.draw_networkx_edges(MyGraph, pos, edge_color=EdgeList, width=2.5)
nx.draw_networkx_edge_labels(
    MyGraph, pos,
    edge_labels={(
                  # Piccadilly Line
                 'Hyde_Park_Corner', 'Green_Park'): '0.9 Km',
                 ('Green_Park', 'Piccadilly_Circus'): '0.5 Km',
                 ('Piccadilly_Circus', 'Leicester_Square'): '0.6 Km',
                 ('Leicester_Square', 'Covent_Garden'): '0.3 Km',
                 ('Covent_Garden', 'Holborn'): '0.5 Km',

                 # Victoria Line
                 ('Victoria', 'Green_Park'): '1.2 Km',
                 ('Green_Park', 'Oxford_Circus'): '1 Km',
                 ('Oxford_Circus', 'Warren_Street'): '1.2 Km',
                 ('Warren_Street', 'Euston'): '0.5 Km',
                 ('Euston', 'King_Cross'): '0.7 Km',

                 # Bakerloo Line
                 ('Embankment', 'Charing_Cross'): '0.3 km',
                 ('Charing_Cross', 'Piccadilly_Circus'): '0.6 Km',
                 ('Piccadilly_Circus', 'Oxford_Circus'): '0.9 Km',
                 ('Oxford_Circus', 'Regens_Park'): '1 Km',
                 ('Regens_Park', 'Baker_Street_Station'): '0.8 Km',

                 # Northern Line
                 ('Waterloo', 'Charing_Cross'): '1.4 Km',
                 ('Charing_Cross', 'Leicester_Square'): '0.4 Km',
                 ('Leicester_Square', 'Goodge_Street'): '1.1 Km',
                 ('Goodge_Street', 'Warren_Street'): '0.5 Km',
                 ('Warren_Street', 'Mornington_Crescent'): '1.3 Km'}
)

text_size = 11

# Piccadilly Label
plt.text(25, 29, s='Hyde Park Corner', size=text_size)
plt.text(43, 52, s='Green park', rotation=15, size=text_size)
plt.text(83, 52, s='Piccadilly Circus', rotation=15, size=text_size)
plt.text(125, 42, s='Leicester Square', rotation=15, size=text_size)
plt.text(148, 58, s='Covent Garden', size=text_size)
plt.text(168, 73, s='Holborn', size=text_size)

# Victoria Label
plt.text(53, 10, s='Victoria', size=text_size)
plt.text(80, 80, s='Oxford Circus', rotation=20, size=text_size)
plt.text(133, 98, s='Warren Street', size=text_size)
plt.text(147, 135, s='Euston', size=text_size)
plt.text(190, 135, s='King Cross &\nSt Pancras International', size=text_size)

# Bakerloo Label
plt.text(142, 6, s='Embankment', rotation=20, size=text_size)
plt.text(134, 25, s='Charing Cross', rotation=20, size=text_size)
plt.text(58, 105, s='Regens Park', rotation=20, size=text_size)
plt.text(38, 125, s='Baker Street Station', rotation=20, size=text_size)

# Northern Label
plt.text(118, -10, s='Waterloo', size=text_size)
plt.text(133, 80, s='Goodge Street', size=text_size)
plt.text(143, 150, s='Mornington Crescent', size=text_size)

plt.title("London Underground Transport Network Graph", size=22)

# Task 3
edge_distances = MyGraph.size(weight="weight")
average_distances = edge_distances / MyGraph.size()
weights = [d["weight"] for (u, v, d) in MyGraph.edges(data=True)]
std_distances = round(np.std(weights), 2)

# Add custom legend for the lines
line_labels = [
    Line2D([0], [0], color='#0015ff', lw=2, label='Piccadilly Line'),
    Line2D([0], [0], color='#2e9ddb', lw=2, label='Victoria Line'),
    Line2D([0], [0], color='#aa5516', lw=2, label='Bakerloo Line'),
    Line2D([0], [0], color='#262324', lw=2, label='Northern Line')
]

legend1 = plt.legend(handles=line_labels, loc='lower right', title="Lines", fontsize=15, title_fontsize=15)

# Add the first legend back to the plot
plt.gca().add_artist(legend1)

# Add custom legend for the statistics
stats_labels = [
    Line2D([0], [0], color='white', lw=2, label=f'Total Length: {edge_distances:.2f} Kilometers'),
    Line2D([0], [0], color='white', lw=2, label=f'Average Distance: {average_distances:.2f} Kilometers'),
    Line2D([0], [0], color='white', lw=2, label=f'Standard Deviation: {std_distances:.2f} Kilometers'),
]

legend2 = plt.legend(handles=stats_labels, loc='lower left', title="Statistics", fontsize=15, title_fontsize=15)

plt.title("London Underground Transport Network Graph", size=22)
plt.savefig("task3.png")
plt.show()
