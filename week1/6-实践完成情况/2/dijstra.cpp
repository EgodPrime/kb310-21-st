//Author Jiang shihao  
//dijstra�ڽӾ���ʵ��
const int N = 1e3;
#include <iostream>
#include<cstdio>
#include<queue>
#include<cstring>
#include<string>
using namespace std;

typedef struct node
{
    int n,v;
}NODE;
NODE node[N];

struct cmp {
    bool operator() (const NODE &p,const NODE &q)
    {
        return p.v>q.v;
    }
};
int graph[N][N];
int res[N];
bool visit[N];
int value[N];
int n,m,i,j,k;
int x=1;
priority_queue <NODE,vector<NODE>,cmp> a;
/*����������
5 6
1 2 2
1 3 1
2 4 5
2 5 6
3 4 7
4 5 3
���е�һ��Ϊ����n,m���ֱ��ʾ����ͼ�нڵ�ĸ����������
������2-n-1�У�ÿһ�е���������i��j��k��ʾ�ڵ�i���ڵ�j�ĵ���·������Ϊk
�㷨������ǽڵ�1��n�ĵ�Դ���·
*/

void setgraph()
{
    memset(graph,-1,sizeof(graph));
    cin>>n>>m;
    for(int t=1;t<=m;t++)
    {
        cin>>i>>j>>k;
        graph[i][j]=k;
    }

}

int search1(int s)
{
    for(int i=1;i<=n;i++)
    {
        if(graph[s][i]!=-1)
        {
            if(visit[i]==false)
            {
                if(s==1) value[i]=graph[s][i];
                else value[i]=value[s]+graph[s][i];
                visit[i]=true;
            }
            else {
                if(s==1) value[i]=graph[s][i];
                else value[i]=(value[s]+graph[s][i]<value[i])?value[s]+graph[s][i]:value[i];
            }
            a.push(NODE{i,value[i]});
        }
    }
    NODE tmp=a.top();
    a.pop();
    res[x++]=tmp.n;
    return tmp.n;
}

int main()
{
    setgraph();

    int temp=1;
    while(x!=n+1)
    {
        temp=search1(temp);
    }

    cout<<value[n]<<endl;
    return 0;
}
