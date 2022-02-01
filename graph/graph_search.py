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

def bfs(G: graph, start):
    queue = []
    closed = set()
    queue.append(start)
    while len(queue) != 0:
        u = queue.pop(0)
        if u not in closed:
            closed.add(u)
            print(u, end=" ")
            for u, v, _ in G.adjacent_list[u]:
                queue.append(v)
        


def main():
    v_num = int(input())
    G = graph()
    for i in range(v_num):
        edge_line = input().split(' ')
        G.add_edge(int(edge_line[0]), int(edge_line[1]), 0)
        G.add_edge(int(edge_line[1]), int(edge_line[0]), 0)
    
    bfs(G, 0)

    print('')
main()