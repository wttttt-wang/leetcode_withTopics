"""
Clone Graph
@ Graph + DFS/BFS
"""


# Definition for a undirected graph node
class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []

class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, nodeGiven):
        if not nodeGiven:
            return None
        nodeMap = {} # graph node map
        # 1. bfs/dfs to get all nodes
        queue, visited = [nodeGiven], set([nodeGiven])
        while queue:
            node = queue.pop()
            nodeMap[node] = UndirectedGraphNode(node.label)
            for nei in node.neighbors:
                if nei not in visited:
                    visited.add(nei)
                    queue.append(nei)
        # 2. update neighbors for new graph
        for origin in nodeMap:
            for nei in origin.neighbors:
                nodeMap[origin].neighbors.append(nodeMap[nei])
        return nodeMap[nodeGiven]

