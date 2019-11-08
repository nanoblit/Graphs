from functools import reduce

class Queue():
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue)

class Graph:
    def __init__(self):
        self.vertices = {}
    
    def add_vertex(self, vertex_id):
        self.vertices[vertex_id] = {}
        self.vertices[vertex_id]['parents'] = set()
        self.vertices[vertex_id]['children'] = set()
    
    def add_edge(self, parent, child):
        if parent not in self.vertices:
            self.add_vertex(parent)
        if child not in self.vertices:
            self.add_vertex(child)
        self.vertices[parent]['children'].add(child)
        self.vertices[child]['parents'].add(parent)
    
    def find_furthest_parent(self, starting_node):
        if len(self.vertices[starting_node]['parents']) == 0:
            return -1

        # make a queue
        q = Queue()
        # make a dict for paths
        paths = {}
        # enqueue current node
        q.enqueue(starting_node)
        # add node list to paths with key node's id
        paths[starting_node] = [starting_node]
        # while queue not empty
        while q.size() > 0:
            # dequeue the node
            node = q.dequeue()
            # for parent in node's parents
            for parent in self.vertices[node]['parents']:
                # copy path with node key
                new_path = paths[node][:]
                # append parent to the new path and add to paths as key and path as value
                new_path.append(parent)
                paths[parent] = new_path
                # enqueue parent
                q.enqueue(parent)
        # return the largest last value of one of the longest paths
        paths_list = []
        for _, value in paths.items():
            paths_list.append(value)
        longest_path_length = -1
        for path in paths_list:
            if len(path) > longest_path_length:
                longest_path_length = len(path)
        longest_id = -1
        for path in paths_list:
            last_element = path[len(path) - 1]
            if len(path) == longest_path_length \
               and longest_id == -1 \
               or last_element < longest_id:
                longest_id = last_element

        return longest_id

def earliest_ancestor(ancestors, starting_node):
    g = Graph()
    for ancestor in ancestors:
        g.add_edge(ancestor[0], ancestor[1])
    return g.find_furthest_parent(starting_node)


    