class Solution(object):
    def allPathsSourceTarget(self, graph):
        paths = []

        def find_paths(graph, curr, path):
            path.append(curr)
            if curr == len(graph) - 1:
                paths.append(path)
            else:
                for next in graph[curr]:
                    find_paths(graph, next, path[:])

        find_paths(graph, 0, [])
        return paths
