# Python program to print topological sorting of a DAG
from collections import defaultdict
from collections import OrderedDict

import json
import pprint


# Class to represent a graph
from operator import getitem



class Graph:
    def __init__(self, vertices):
        self.graph = defaultdict(list)  # dictionary containing adjacency List
        self.V = vertices  # No. of vertices
        self.dic = dict()
        self.time = 0
        # self.pred = 0

    # function to add an edge to graph
    def addEdge(self, u, v):
        self.graph[u].append(v)
        for val in [u, v]:
            # if val not in self.dic.keys():
            if val not in list(self.dic):
                self.dic[val] = {
                    'color': 'white',
                    'd': 0,
                    'f': 0,
                    'P': []
                    # 'pred': 0,
                }
    def addEdgeByPath(self, path):
        file1 = open(path, 'r')
        Lines = file1.readlines()
        for line in Lines:
            line = line.strip()
            lineArray = line.split(' ')
            self.addEdge(lineArray[0], lineArray[1])

    def DFS(self):
        # for val in self.graph.keys():
        for val in list(self.graph):
            # self.graph.l = self.graph
            # self.dic[val]['l'] = self.dic[self.dic[val]['p']]['l'] + 1
            # print('val is', val)
            if self.dic[val]['color'] == 'white':
                self.DFS_VISIT(val)

    def DFS_VISIT(self, u):
        self.time += 1
        self.dic[u]['d'] = self.time
        self.dic[u]['color'] = 'grey'
        for i in self.graph[u]:
            if self.dic[i]['color'] == 'white':
                self.dic[i]['P'].append(u)
                # self.dic[i]['l'] = self.dic[u]['l']  + 1
                self.DFS_VISIT(i)
            else:
                self.dic[i]['P'].append(u)
        self.dic[u]['color'] = 'black'
        self.time = self.time + 1
        self.dic[u]['f'] = self.time

    # def findLength(self, node):



    def longestPath(self):
        res = OrderedDict(sorted(self.dic.items(),
                                 key=lambda x: getitem(x[1], 'f'), reverse=True))
        dp = [0] * len(list(res))
        sortedArray = list(res)
        for i, element in enumerate(list(res)):
            parentNode = self.dic[element]['P']
            t = [dp[sortedArray.index(k)] + 1 for k in parentNode]
            if len(t) == 0:
                dp[i] = 0
            else:
                dp[i] = max(t)



        print('longest distance is', max(dp))


    def finalData(self):
        res = OrderedDict(sorted(self.dic.items(),
                                 key=lambda x: getitem(x[1], 'f'), reverse=True))
        print('tropological order is', list(res))




g = Graph(50)
g.addEdgeByPath('/Users/udayreddy/Desktop/uday.txt')



# #
# g.addEdge('A1', 'B1');
# g.addEdge('B1', 'A2');
# g.addEdge('A1', 'C1');
# g.addEdge('C1', 'B2');
# g.addEdge('C2', 'B2');

# g.iterateLoop()
g.DFS()
g.finalData()
g.longestPath()

# g.longestPmaath()