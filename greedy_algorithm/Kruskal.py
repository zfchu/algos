'''
给定一个无向图G=（V，E），如果它的生成子图是连通无圈的，那么我们就称这个生成子图为生成树(Spanning Tree)。
如果是带权值的无向图，那么权值之和最小的生成树，我们就称之为最小生成树(MST， Minimum Spanning Tree)。

Kruskal算法原理
Kruskal算法是基于贪心的思想得到的。首先把所有的边按照权值从小到大排列，接着按照顺序选取每条边，
如果这条边的两个端点不属于同一棵树（即：不会形成圈），那么就将它们合并；如果这条边的两个端点属于
同一棵树（即：会形成圈），就舍去这条边，考虑下条边。以此类推，直到所有的点都属于同一棵树为止，
这棵树就是最小生成树。Kruskal算法是所有最小生成树算法中最为简单理解的一个，这里充分体现了贪心算法的精髓。

'''
import time                         
start = time.perf_counter() #开始计时
class DisjointSet(dict):
    '''不相交集'''

    def __init__(self, dict):
        pass

    def add(self, item):
        self[item] = item

    def find(self, item):
        if self[item] != item:
            self[item] = self.find(self[item])
        return self[item]

    def unionset(self, item1, item2):
        self[item2] = self[item1]

def Kruskal(nodes, edges):
    '''基于不相交集实现Kruskal算法'''
    forest = DisjointSet(nodes)
    MST = []
    for item in nodes:
        forest.add(item)
    edges = sorted(edges, key=lambda element: element[2])
    num_sides = len(nodes)-1  # 最小生成树的边数等于顶点数减一
    for e in edges:
        node1, node2, _ = e
        parent1 = forest.find(node1)
        parent2 = forest.find(node2)
        if parent1 != parent2:
            MST.append(e)
            num_sides -= 1
            if num_sides == 0:
                return MST
            else:
                forest.unionset(parent1, parent2)
    pass

def main():
    nodes = set(list('ABCDE'))
    edges = [("A", "B", 1), ("A", "C", 7),
             ("A", "D", 3), ("B", "C", 6),
             ("B", "E", 4), ("C", "D", 8),
             ("C", "E", 5), ("D", "E", 2)]
    print("\n\nThe undirected graph is :", edges)
    print("\n\nThe minimum spanning tree by Kruskal is : ")
    print(Kruskal(nodes, edges))

if __name__ == '__main__':
    main()
end = time.perf_counter()
print('Running time: %f seconds'%(end-start))
import time
start = time.perf_counter()
class DisjointSet(dict):
    '''不相交集'''

    def __init__(self, dict):
        pass

    def add(self, item):
        self[item] = item

    def find(self, item):
        if self[item] != item:
            self[item] = self.find(self[item])
        return self[item]

    def unionset(self, item1, item2):
        self[item2] = self[item1]

def Kruskal(nodes, edges):
    '''基于不相交集实现Kruskal算法'''
    forest = DisjointSet(nodes)
    MST = []
    for item in nodes:
        forest.add(item)
    edges = sorted(edges, key=lambda element: element[2])
    num_sides = len(nodes)-1  # 最小生成树的边数等于顶点数减一
    for e in edges:
        node1, node2, _ = e
        parent1 = forest.find(node1)
        parent2 = forest.find(node2)
        if parent1 != parent2:
            MST.append(e)
            num_sides -= 1
            if num_sides == 0:
                return MST
            else:
                forest.unionset(parent1, parent2)
    pass

def main():
    nodes = set(list('ABCDEFG'))
    edges = [("A", "B", 7), ("A", "D", 5),
             ("B", "C", 8), ("B", "D", 9), ("B", "E", 7), 
             ("C", "E", 5), ("D", "E", 15), ("D", "F", 6),
             ("E", "F", 8), ("E", "G", 9), ("F", "G", 11)]
    print("\n\nThe undirected graph is :", edges)
    print("\n\nThe minimum spanning tree by Kruskal is : ")
    print(Kruskal(nodes, edges))

if __name__ == '__main__':
    main()
end = time.perf_counter()   #结束计时
print('Running time: %f seconds'%(end-start))  #程序运行时间

