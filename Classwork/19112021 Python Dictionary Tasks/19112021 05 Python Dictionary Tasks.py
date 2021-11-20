#Python Dictionary Tasks

unweighted_graph = {"A": ["B","E"],
                    "B": ["A","C","D"],
                    "C": ["B","D","G"],
                    "D": ["B","C","E","F"],
                    "E": ["A","D"],
                    "F": ["D"],
                    "G": ["C"]}

weighted_graph = {"A": {"B":5,"E":4},
                  "B": {"A":5,"C":4,"D":3},
                  "C": {"B":4,"D":5,"G":2},
                  "D": {"B":3,"C":5,"E":7,"F":6},
                  "E": {"A":4,"D":7},
                  "F": {"D":6},
                  "G": {"C":2}}


visited = []
def depth_first_search(visited, graph, node):
    if node not in visited:
        print(node)
        visited.append(node)
        for adjacent in graph[node]:
            depth_first_search(visited, graph, adjacent)

depth_first_search(visited, unweighted_graph, "A")
