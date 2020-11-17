#File Name : 最小生成树prim算法.py
 
from heapq import  *
class Node(object):
    pass
class UnionFindSet(object):
    def __init__(self,nodes):
        self.fatherDict = {}
        # key node  value father 一层一层向上找
        self.sizeDict = {}
        # key 节点  value 节点所在集合共有多少个节点
        for node in nodes:
            self.fatherDict[node]= node
            self.sizeDict[node] = 1
        #每个节点的父亲是自己 并且所在的集合为个数为1
        #因为要少挂多 ，所以要找节点数目
    def FindHead(self,node):
        stack = []
        father = self.fatherDict[node]
        while father!=node:
            stack.append(node)
            node = father
            father = self.fatherDict[node]
        while stack:
            self.fatherDict[stack.pop()] = father
        return father
    def isSameSet(self,a,b):
        return self.FindHead(a) == self.FindHead(b)
    def uion(self,a,b):
        if a is None or b is None:
            return
        aHead = self.FindHead(a)
        bHead = self.FindHead(b)
        if aHead!=bHead:
            asize = self.sizeDict[aHead]
            bsize = self.sizeDict[bHead]
            if asize<=bsize:
                self.fatherDict[aHead] = bHead
                self.sizeDict[bHead] = asize+bsize
            else:
                self.fatherDict[bHead] = aHead
                self.sizeDict[aHead] = asize+bsize
 
class Node(object):
    def __init__(self,value=None):
        self.value = value #节点的值
        self.come = 0 #节点入度
        self.out = 0 #节点出度
        self.nexts = [] #节点的邻居节点
        self.edges = [] #在节点为from的情况下，边的集合
class Edge(object):
    def __init__(self,weight=None,fro,to):
        self.weight = weight # 边的权重
        self.fro = fro # 边的from节点
        self.to = to #边的to节点
    def __lt__(self, other):
        return self.weight<other.weight
class Graph(object):
    def __init__(self):
        self.nodes = {} #图所有节点的集合  字典形式 ：{节点编号：节点}
        self.edges = [] #图的边集合
 
def creatGraph(matrix):
    # 二维数组matrix [权重  从那个点的值  去哪个点的值]
    graph = Graph()
    # 建立所有节点
    for edge in matrix:
        weight = edge[0]
        fro = edge[1]
        to = edge[2]
        if fro not in graph.nodes:
            graph.nodes[fro] = Node(fro)
        if to not in graph.nodes:
            graph.nodes[to] = Node(to)
    #建立所有的边
        fromNode = graph.nodes[fro]
        toNode = graph.nodes[to]
        newEdge = Edge(weight,fromNode,toNode)
        fromNode.nexts.append(toNode) #加上邻居指向
        fromNode.out+=1 #出度+1
        toNode.come+=1 #to 的入度+1
        fromNode.edge.append(newEdge) #边的集合+1
        graph.edges.append(newEdge)
 
    return graph
    
def primMST(graph):
    heapq = []
    set1 = set()
    res1 = set()
    #把节点与对应的边加入
    for node in graph.nodes.values():
        if node not in set1:
            set1.add(node)
            for edge in node.edges:
                heappush(heapq,edge)
            while len(heapq)>0:
                edge = heappop(heapq)
                tonode = edge.to
                if tonode not in set1:
                    set1.add(tonode)
                    res1.add(edge)
                    for nextedge in tonode.edges:
                        heappush(heapq,nextedge)
    return res1
