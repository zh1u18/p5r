import pandas as pd
import pickle

with open('search_graph.pkl', 'rb') as file:
    graph = pickle.load(file)

def search_route(start, end, max_depth=3):
    def dfs(node, path, cost, depth):
        if depth > max_depth:
            return
        if node == end:
            # 处理路径的格式化
            formatted_path = f"{path[0][0]}" # 起始节点
            for i in range(1, len(path)):
                formatted_path += f" + {path[i][1]} -> {path[i][0]}"
            paths.append((formatted_path, cost))
            return
        for neighbor, material, weight in graph[node]:
            if neighbor not in [n for n, m in path]:
                new_path = path + [(neighbor, material)]
                dfs(neighbor, new_path, cost + weight, depth + 1)
    
    paths = []
    dfs(start, [(start, '')], 0, 1) # 初始深度设为1
    paths.sort(key=lambda x: x[1])
    return paths

