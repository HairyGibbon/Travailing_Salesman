
class Graph:
    """Create a Graph"""
    def __init__(self):
        pass

    __coordinates = []
    __connections = []

    def set_coordinates(self, *coordinates):
        for co in coordinates:
            self.__coordinates.append(co)

    def set_connections(self, *connections):
        for co in connections:
            self.__connections.append(co)

    def get_coordinates(self):
        return self.__coordinates

    def get_connections(self):
        return self.__connections
