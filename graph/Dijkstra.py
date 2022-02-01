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

    def get_weight(self, u, v):
        for _, t, w in self.adjacent_list[u]:
            if t == v:
                return w

    def dijkstra(self, s, t):
        S = set()
        dist = {s:0}
        prev = {s:None}
        for v in self.adjacent_list.keys():
            if v != s:
                dist[v] = float('inf')
                prev[v] = None
            S.add(v)
        v = s
        while v != t:
            for _, u, w in self.adjacent_list[v]:
                tmp = dist[v] + w
                if tmp < dist[u]:
                    dist[u] = tmp
                    prev[u] = v
            S.remove(v)
            min = float('inf')
            for x in S:
                if dist[x] < min:
                    min = dist[x]
                    v = x
        res = []
        v = t 
        while v != None:
            res.insert(0, v)
            v = prev[v]
        print(res)
        # print(prev)
        # print(dist)


def main():
    v_num = int(input())
    G = graph()

    for i in range(v_num):
        edge_line = input().split(' ')
        G.add_edge(edge_line[0], edge_line[1], int(edge_line[2]))
    
    s = input()
    t = input()

    G.dijkstra(s, t)

    # res = dijkstra(G, s, t)
    # print(res)
    
if __name__ == '__main':
    main()
