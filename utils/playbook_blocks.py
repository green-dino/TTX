class ProcessNode:
    def __init__(self, name):
        self.name = name
        self.next_node = None

    def set_next_node(self, next_node):
        self.next_node = next_node

    def __str__(self):
        return self.name

class ProcessFlow:
    def __init__(self):
        self.start_node = None

    def add_node(self, node):
        if not self.start_node:
            self.start_node = node
        else:
            current_node = self.start_node
            while current_node.next_node:
                current_node = current_node.next_node
            current_node.set_next_node(node)

    def __str__(self):
        result = ""
        current_node = self.start_node
        while current_node:
            result += f"{current_node} --> "
            current_node = current_node.next_node
        return result[:-5]  # Remove the trailing " --> "

# Create the nodes
b1 = ProcessNode("B1(Problem Identification and Change Initiation)")
b2 = ProcessNode("B2(Change Control Record Creation)")
b3 = ProcessNode("B3(Communication and Risk Assessment)")
b4 = ProcessNode("B4(Documentation and Evaluation)")
b5 = ProcessNode("B5(Fulfillment and Closure)")

# Create the process flow and connect the nodes
process_flow = ProcessFlow()
process_flow.add_node(b1)
process_flow.add_node(b2)
process_flow.add_node(b3)
process_flow.add_node(b4)
process_flow.add_node(b5)

# Connect the nodes as per the diagram
b1.set_next_node(b2)
b2.set_next_node(b3)
b3.set_next_node(b4)
b4.set_next_node(b5)

# Print the process flow
print(process_flow)
