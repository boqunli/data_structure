class graph:
    def __init__(self, E = []):
        self.adjacent_list = {}
        for s, t, w in E:
            if s in self.adjacent_list.keys():
                self.adjacent_list[s].append([s, t, w])
            else:
                self.adjacent_list[s] = [[s, t, w]]

    def add_edge(self, u, v, w):
        if u in self.adjacent_list.keys():
            self.adjacent_list[u].append([u, v, w])
        else:
            self.adjacent_list[u] = [[u, v, w]]
        if v not in self.adjacent_list.keys():
            self.adjacent_list[v] = []

    def get_weight(self, u, v):
        for _, t, w in self.adjacent_list[u]:
            if t == v:
                return w

    def set_weight(self, u, v, val):
        for i in range(len(self.adjacent_list[u])):
            s, t, w = self.adjacent_list[u][i]
            if t == v:
                self.adjacent_list[u][i][2] = val
    
    def exist_edge(self, u, v):
        if u in self.adjacent_list:
            for _, t, _ in self.adjacent_list[u]:
                if t == v:
                    return True
        return False
