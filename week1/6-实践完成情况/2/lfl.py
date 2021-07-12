from typing import Counter, SupportsRound

class  dijkstra(object):
    def __init__(self,graph,sourse):
        self.graph=graph
        self.sourse=sourse
        ''' 
        有向图
        graph = {1:{1:0, 2:1, 3:12},
        2:{2:0, 3:9, 4:3},
        3:{3:0, 5:5},
        4:{3:4, 4:0, 5:13, 6:15},
        5:{5:0, 6:4},
        6:{6:0}}
        '''
    def dijkstra(self):
        #初始化一个距离字典，记录这点到sourse的距离
        dis=dict((i,float('inf')) for i in self.graph.keys())
        now_node=self.sourse
        dis[self.sourse]=0
        visited=[]#去记录已经遍历过的节点
        #初始化一个路径字典
        path=dict((i,[]) for i in self.graph.keys())
        path[self.sourse]=str(self.sourse)#自己到自己的路径是自己

        while len(visited)!=len(self.graph):#结束条件为遍历完所有
            visited.append(now_node)#加入当前节点
            for i in self.graph[now_node]:
                #去找当前节点的所有相邻节点,i为邻居节点
                if dis[now_node]+self.graph[now_node][i]<dis[i]:
                #如果起始点到该节点的距离大于当前节点到起始点距离+当前节点与它的距离之和就更新
                    dis[i]=dis[now_node]+self.graph[now_node][i]
                    seq=(path[now_node],str(i))
                    sym='-'
                    path[i]=sym.join(seq)
                    #path[i]='-'.join(((path[now_node]),str(i)))
                #对路径操作，把当前节点加入到对应路径。用-连接,必须用''字符串(str)才能用join
            #选择下一个节点
            #用temp暂时值，遍历所有的非visited中的节点，寻找最小的dis
            temp=9999
            for node in dis.keys():
                if node in visited:continue
                elif dis[node]<temp:
                    temp=dis[node]
                    now_node=node
                else:pass
        return dis,path

if __name__=='__main__':
    graph = {1:{1:0, 2:1, 3:12},
        2:{2:0, 3:9, 4:3},
        3:{3:0, 5:5},
        4:{3:4, 4:0, 5:13, 6:15},
        5:{5:0, 6:4},
        6:{6:0}}
    sourse=1
    djk=dijkstra(graph=graph,sourse=sourse)
    dis,path=djk.dijkstra()
    print(dis)
    print(path)