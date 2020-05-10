graph = {
    "A":["B","C"],
    "B":["A","C","D"],
    "C":["A","B","D","E"],
    "D":["B","C","E","F"],
    "E":["C","D"],
    "F":["D"],
}
def BFS(graph, s):
    queue = []
    queue.append(s)
    seen = set()
    seen.add(s)
    while (len(queue) > 0):
        vertex = queue.pop(0)
        nodes = graph[vertex]
        for i in nodes:
            if i not in seen:
                seen.add(i)
                queue.append(i)
        print(vertex)
def DFS(graph, s):
    stack = []
    stack.append(s)
    seen = set()
    seen.add(s)
    while (len(stack) > 0):
        vertex = stack.pop()
        nodes = graph[vertex]
        for i in nodes:
            if i not in seen:
                seen.add(i)
                stack.append(i)
        print(vertex)
def _BFS(graph, s):
    queue = []
    queue.append(s)
    seen = set()
    seen.add(s)
    parent = {s : None}
    while (len(queue) > 0):
        vertex = queue.pop(0)
        nodes = graph[vertex]
        for i in nodes:
            if i not in seen:
                seen.add(i)
                queue.append(i)
                parent[i] = vertex
    return parent
#DFS(graph,"A")
a = _BFS(graph, "E")
distance = 0
v = "B"
while v != None:
    distance += 1
    v = a[v]
print(distance)
