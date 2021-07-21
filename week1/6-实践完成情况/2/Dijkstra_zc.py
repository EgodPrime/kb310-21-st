#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Zhang Chi
import heapq
import math

#计算图中各个节点与初始节点的最短距离，给出到达目标节点最短路径经过的节点
#如果存在负权边，那就有可能先通过并不是距源点最近的一个次优点，再通过这个负权边，使得路径之和更小，这样就出现了错误，可使用SPFA算法避免
graph={
    "A":{"B":5,"C":1},
    "B":{"A":5,"C":2,"D":2},
    "C":{"A":1,"B":2,"D":4,"E":3},
    "D":{"B":2,"C":4,"E":3,"F":6},
    "E":{"C":8,"D":3},
    "F":{"D":6}
    }

def init_distance(graph,s): #初始化LCS表
    distance={s:0} #与自己的距离为0
    for vertex in graph:
        if vertex != s:
            distance[vertex]=math.inf #与未达到点的距离设为无穷大
    return distance

def dijkstra(graph,s):
    pqueue=[] 
    heapq.heappush(pqueue,(0,s)) #堆插入自己
    seen=set() #空集
    parent={s : None}
    distance=init_distance(graph,s)
    while (len(pqueue)>0):
        pair=heapq.heappop(pqueue) #堆弹出最短路径点和距离
        dist=pair[0]
        vertex=pair[1]
        seen.add(vertex) #标记该点已经过
        nodes=graph[vertex].keys() #获取该节点连接的点
        for w in nodes:
            if w not in seen:
                if dist + graph[vertex][w] < distance[w]: #比较路径长度
                    heapq.heappush(pqueue, (dist + graph[vertex][w],w)) #堆插入新的距离值和节点
                    parent[w]=vertex #更新下一节点
                    distance[w]=dist + graph[vertex][w] #更新到达下一节点的距离值
    return parent,distance

def dist_result(parent,v): #到达目标节点的最短路径
    result=[]
    while v != None: 
        result.append(v) #倒推出最短路径经过的节点
        v=parent[v] #更新
    result=result[::-1] #倒序输出
    return result

parent,distance=dijkstra(graph,"A")
distance=sorted(distance.items(), key=lambda x: x[1]) #按value排序
result=dist_result(parent,'F')
print("最短路径值为：",distance) #输出最短路径值
print("路径为：",result) #输出最短路径节点

