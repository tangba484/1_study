def is_spanning_tree(graph, start_vertex=0):
    num_vertices = len(graph)
    visited = [False] * num_vertices
    parent = [-1] * num_vertices
    
    def dfs(vertex, parent_vertex):
        visited[vertex] = True
        parent[vertex] = parent_vertex
        
        for neighbor in graph[vertex]:
            if not visited[neighbor]:
                if dfs(neighbor, vertex):
                    return True
            elif parent_vertex != neighbor:
                return True
        
        return False
    
    if dfs(start_vertex, -1):
        return False
    
    # 모든 정점이 연결되었는지 확인
    for vertex in range(num_vertices):
        if not visited[vertex]:
            return False
    
    return True

# 그래프의 인접 리스트 표현 예시
graph = {
    0: [1, 2],
    1: [0, 3],
    2: [0],
    3: [1,4],
    4: [3]
}

print(is_spanning_tree(graph))  # True or False 출력
