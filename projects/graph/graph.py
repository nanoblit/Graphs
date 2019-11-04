"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        # empty dictionary for verts
        self.vertices = {}

    def add_vertex(self, vertex):
        """
        Add a vertex to the graph.
        """
        # at vertex create an empty set
        self.vertices[vertex] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        # if v1 and v2 exist in vertices list
        if v1 in self.vertices and v2 in self.vertices:
            # add v2 at v1 of vertices
            # (add v2 to the vertices list at the index of v1)
            self.vertices[v1].add(v2)
        # otherwise
        else:
            # raise an error
            raise KeyError("That vertex does not exist")

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        # create an empty queue and enqueue the starting vertex ID
        q = Queue()
        q.enqueue(starting_vertex)
        # create a set to store the visited vertices
        visited = set()
        # while the queue is not empty
        while q.size() > 0:
            # Dequeue the first vertex
            v = q.dequeue()
            # if that vertex has not been vidited
            if v not in visited:
                # mark it as visited (printing for a representation)
                print(v)
                visited.add(v)
                # then add all of it's neighbors to the back of the queue
                for next_vertex in self.vertices[v]:
                    q.enqueue(next_vertex)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # create an empty stack and push the starting vertex ID
        s = Stack()
        s.push(starting_vertex)
        # create a set to store the visited vertices
        visited = set()
        # while the stack is not empty
        while s.size() > 0:
            # Pop the first vertex
            v = s.pop()
            # if that vertex has not been vidited
            if v not in visited:
                # mark it as visited (printing for a representation)
                print(v)
                visited.add(v)
                # then add all of it's neighbors to the back of the stack
                for next_vertex in self.vertices[v]:
                    s.push(next_vertex)

    def dft_recursive(self, vertex, visited=set()):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        This should be done using recursion.
        """
        # if visited
        if vertex in visited:
            # return
            return
        # add to visited
        visited.add(vertex)
        # print this value
        print(vertex)
        # for each vertice
        for found_vertex in self.vertices[vertex]:
            # call dft_recursive on this vertice, with this visited
            self.dft_recursive(found_vertex, visited)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # create visited set
        visited = set()
        # create dicts of lists
        paths = {}
        # create queue
        q = Queue()
        # add starting_vertex to queue
        q.enqueue(starting_vertex)
        # add starting_vertex to dict
        paths[starting_vertex] = [starting_vertex]
        # while true
        while True:
            # dequeue value from queue and set it as vertex
            vertex = q.dequeue()
            # set vertex as visited
            visited.add(vertex)
            # for searched_vertex in vertex
            for searched_vertex in self.vertices[vertex]:
                # if searched_vertex visited
                if searched_vertex in visited:
                    # break
                    break
                # get vertex list from the dict and add searched_vertex to it's copy
                new_path = paths[vertex][:]
                new_path.append(searched_vertex)
                # add it to dict with searched_vertex as the key
                paths[searched_vertex] = new_path
                # if searched_vertex is destination_vertex return path
                if searched_vertex == destination_vertex:
                    return paths[searched_vertex]
                # add searched_vertex to queue
                q.enqueue(searched_vertex)

    def dfs(self, vertex, destination_vertex, visited=set(), path=[]):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        # add to path
        path.append(vertex)
        # if destination or visited
        if vertex == destination_vertex or vertex in visited:
            # return path
            return path
        # add to visited
        visited.add(vertex)
        # for each vertice
        for found_vertex in self.vertices[vertex]:
            # call dft_recursive on this vertice, with this visited
            self.dfs(found_vertex, destination_vertex, visited, path)
            # if not found 
            if path[-1:][0] != destination_vertex:
                # pop from path
                path.pop()
            # if found
            else:
                # break
                break
        return path




if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT recursive paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
