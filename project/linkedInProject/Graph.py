

class Graph :

    unlinkedInGraph = None

    def __init__(self):
        self.edges = list()
        self.vertices = list()

        if Graph.unlinkedInGraph is None :
            Graph.unlinkedInGraph = self




