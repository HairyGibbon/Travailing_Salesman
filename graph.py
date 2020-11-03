
class Graph:
    """Create a Graph"""
    def __init__(self):
        pass

    __coordinates = []
    __connections = []
    __pressed_num = [0]
    __pressed_coo = []
    __route_length = 0

    def init(self):
        self.__coordinates = []
        self.__connections = []
        self.__pressed_num = [0]
        self.__pressed_coo = []
        self.__route_length = 0

    # Setters
    def set_coordinates(self, *coordinates):
        for coo in coordinates:
            self.__coordinates.append(coo)

    def set_connections(self, *connections):
        for coo in connections:
            self.__connections.append(coo)

    def set_pressed_num(self, node):
        self.__pressed_num.append(node)
        num1 = self.__pressed_num[-1]
        num2 = self.__pressed_num[-2]
        for con in self.__connections:
            if (con[0] == num1 and con[1] == num2) or (con[0] == num2 and con[1] == num1):
                self.__route_length += con[2]

    def set_pressed_coo(self, node):
        self.__pressed_coo.append(node)

    # Getters
    def get_coordinates(self):
        return self.__coordinates

    def get_connections(self):
        return self.__connections

    def get_pressed_num(self):
        return self.__pressed_num

    def get_pressed_coo(self):
        return self.__pressed_coo

    def get_route_length(self):
        return self.__route_length
