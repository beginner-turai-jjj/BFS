def dfs(graph, node, visited=None):
    """
    深さ優先探索法（DFS）
    
    Parameters:
        graph (dict): グラフを表す辞書
        node : 探索を開始するノード
        visited (set): 訪問済みノードを記録する集合
    
    Returns:
        set: 訪問済みノード
    """
    if visited is None:
        visited = set()

    # 今のノードを訪問済みにする
    visited.add(node)
    print(node, end=" ")

    # 隣接ノードを順番に探索する
    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

    return visited


if __name__ == "__main__":
    graph = {
        "A": ["B", "C"],
        "B": ["D", "E"],
        "C": ["F"],
        "D": [],
        "E": ["F"],
        "F": []
    }

    print("DFSの探索順:")
    dfs(graph, "A")