class Graph:
    def __init__(self) -> None:
        self.adj_list = {}
        
    def add_vertex(self, vertex):
        if vertex not in self.adj_list.keys():
            self.adj_list[vertex] = []
            return True
        return False
    
    def show_graph(self):
        for vertex in self.adj_list:
            print(vertex, ':', self.adj_list[vertex])
            
    def add_edges(self, v1, v2):
        if v1 in self.adj_list.keys() and v2 in self.adj_list.keys():
            self.adj_list[v1].append(v2)
            self.adj_list[v2].append(v1)
            return True
        return False
    
    def remove_edge(self, v1, v2):
        if v1 in self.adj_list.keys() and v2 in self.adj_list.keys():
            try:
                self.adj_list[v1].remove(v2) 
                self.adj_list[v2].remove(v1) 
            except ValueError:
                pass
            return True
        return False
    
    def remove_vertex(self, v1):
        if v1 in self.adj_list.keys():
            for v2 in self.adj_list[v1].copy():
                self.remove_edge(v1=v1, v2=v2)
            del self.adj_list[v1]
            return True
        return False

        
    
# Initialize the Graph
my_graph = Graph()

# Add Vertex
my_graph.add_vertex('A')
my_graph.add_vertex('B')
my_graph.add_vertex('C')
my_graph.add_vertex('D')

# Add Edges
my_graph.add_edges('A','B')
my_graph.add_edges('A','C')
my_graph.add_edges('A','D')
my_graph.add_edges('B','D')
my_graph.add_edges('C','D')


print('-'*15, "Before", '-'*15)
my_graph.show_graph()
# Remove a vertex
my_graph.remove_vertex('D')
print('-'*15, "After Removal of 'D' vertex", '-'*15)
my_graph.show_graph()
print('-'*15)

# my_graph.remove_edge('A','D')
# my_graph.show_graph()
        