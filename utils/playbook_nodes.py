import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

# Define the nodes and edges
node_data = {
    'From': ['A', 'B', 'B', 'B', 'B', 'C', 'D', 'E', 'F', 'F', 'F', 'F', 'F', 'C', 'D', 'E', 'N', 'N', 'Q', 'Q', 'T', 'V', 'W', 'X'],
    'To': ['B', 'C', 'D', 'E', 'F', 'F', 'F', 'F', 'G', 'H', 'I', 'J', 'K', 'F', 'L', 'M', 'O', 'P', 'R', 'S', 'U', 'W', 'X', 'Y'],
    'Action': ['Initiates', 'Addresses', 'Initiates', 'Submits', 'Links to', 'Links to', 'Links to', 'Captures', 'Captures', 'Determines', 'Assesses', 'References', 'Links to', 'Links to', 'Conducts', 'Initiates', 'Incorporates', 'Incorporates', 'Maps', 'Maps', 'Assigns', 'Selects', 'Manages', 'Provides']
}

# Create a DataFrame
df = pd.DataFrame(node_data)

# Create a directed graph
G = nx.DiGraph()

# Add nodes and edges to the graph
for index, row in df.iterrows():
    G.add_edge(row['From'], row['To'], action=row['Action'])

# Plot the graph
pos = nx.spring_layout(G, seed=42)
labels = nx.get_edge_attributes(G, 'action')
nx.draw(G, pos, with_labels=True, node_size=800, node_color='lightblue', font_size=10, font_weight='bold', arrows=True)
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels, font_size=8)
plt.title('Data Visualization')
plt.show()
