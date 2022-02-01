import graph
import sys

def EdmondsKarp(G: graph, s, t):
    parents = {}
    max_flow = 0
    while bfs(G, s, t, parents):
        flow = float('inf')
        it = t
        while it != s:
            p = parents[it]
            flow = min(flow, G.get_weight(p, it))
            it = p
        it = t
        while it != s:
            p = parents[it]
            G.set_weight(p, it, G.get_weight(p, it)-flow)
            G.set_weight(it, p, G.get_weight(it, p)+flow)
            it = p
        max_flow += flow
        parents.clear()
    return max_flow

def bfs(G: graph, start, end, parents):
    dist = {}
    for k in G.adjacent_list.keys():
        parents[k] = None
        dist[k] = float('inf')
    dist[start] = 0
    queue = []
    queue.append(start)
    while len(queue) != 0:
        u = queue.pop(0)
        for u, v, _ in G.adjacent_list[u]:
            if dist[v] == float('inf') and G.get_weight(u, v) > 0:
                dist[v] = dist[u] + 1
                parents[v] = u
                if v == end:
                    return True
                queue.append(v)
    
    return False

def main():
    v_num = int(input())
    G = graph()
    for _ in range(v_num):
        line = input()
        edge_line = line.split(' ')
        if not G.exist_edge(edge_line[0], edge_line[1]):
            G.add_edge(edge_line[0], edge_line[1], int(edge_line[2]))
        else:
            G.set_weight(edge_line[0], edge_line[1], G.get_weight(edge_line[0], edge_line[1]) + int(edge_line[2]))
        if not G.exist_edge(edge_line[1], edge_line[0]):
            G.add_edge(edge_line[1], edge_line[0], 0)
    s = input()
    t = input()
    print(EdmondsKarp(G, s, t))

main()