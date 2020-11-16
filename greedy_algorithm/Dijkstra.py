# dijjkstra算法(原生最短路径，还未优化)
def dij(start, graph):
    n = len(graph)
    # 初始化各项数据，把costs[start]初始化为0，其他为无穷大
    # 把各个顶点的父结点设置成-1
    costs = [99999 for _ in range(n)]
    costs[start] = 0
    parents = [-1 for _ in range(n)]
    visited = [False for _ in range(n)] # 标记已确定好最短花销的点
    t = []  # 已经确定好最短花销的点列表
    while len(t) < n:
        # 从costs里面找最短花销(找还没确定的点的路径)，标记这个最短边的顶点，把顶点加入t中
        minCost = 99999
        minNode = None
        for i in range(n):
            if not visited[i] and costs[i] < minCost:
                minCost = costs[i]
                minNode = i
        t.append(minNode)
        visited[minNode] = True

        # 从这个顶点出发，遍历与它相邻的顶点的边，计算最短路径，更新costs和parents
        for edge in graph[minNode]:
            if not visited[edge[0]] and minCost + edge[1] < costs[edge[0]]:
                costs[edge[0]] = minCost + edge[1]
                parents[edge[0]] = minNode
    return costs, parents


# 主程序

# Data
data = [
    [1, 0, 8],
    [1, 2, 5],
    [1, 3, 10],
    [1, 6, 9],
    [2, 0, 1],
    [0, 6, 2],
    [3, 6, 5],
    [3, 4, 8],
    [0, 5, 4],
    [5, 6, 7],
    [5, 3, 8],
    [5, 4, 5]
]
n = 7  # 结点数

# 用data数据构建邻接表
graph = [[] for _ in range(n)]
for edge in data:
    graph[edge[0]].append([edge[1], edge[2]])
    graph[edge[1]].append([edge[0], edge[2]])
# for edges in graph:
#     print(edges)

# 从1开始找各点到1的最短路径（单源最短路径）
# costs: 各点到店1的最短路径
# parents: 各点链接的父结点，可以用parents建立最短路径生成树
costs, parents = dij(1, graph)
print('costs')
print(costs)
print('parents')
print(parents)

# 结果：
# costs
# [6, 0, 5, 10, 15, 10, 8]
# parents
# [2, -1, 1, 1, 5, 0, 0]

