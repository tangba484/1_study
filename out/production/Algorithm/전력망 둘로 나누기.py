def solution(n, wires):
    graph=[[]for _ in range(n+1)]
    for x,y in wires:
        graph[x].append(y)
        graph[y].append(x)
    ans=[]
    for w in wires:
        x,y = w[0],w[1]
        visited=[0]*(n+1)
        stack=graph[x][:]
        visited[x] = 1
        while stack:
            t = stack.pop()
            if t != y:
                visited[t] = 1
                for i in graph[t]:
                    if not visited[i] and i!=y:
                        stack.append(i)
        ans.append(abs(sum(visited)-n+sum(visited)))
    return min(ans)