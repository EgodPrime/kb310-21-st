//Author Jiangshihao
 
#include<iostream>
#include<cstdio>
#include<algorithm>
#include<cstring>
const int N = 1e3;
using namespace std;
int a[N];
int b[N];
int res[N][N];
int path[N][N];//1=б��ݹ� 2=���� 3=����
int result[N];//��¼���մ�LCS
int lenth;

int dp(int n,int m)//�ݹ��㷨���޷��ó�LCS�������ܵó����ȣ���ʱ�临�ӶȽϸ�
{
    if(n==0 || m==0) return 0;
    if(a[n]==b[m]) {
        return dp(n-1,m-1)+1;
    }
    else return max(dp(n,m-1),dp(n-1,m));
}


int main()
{
    int n,m;
    cin>>n>>m;
    for(int i=1;i<=n;i++)
    {
        cin>>a[i];
    }
    for(int i=1;i<=m;i++)
    {
        cin>>b[i];
    }

    //��� ���Ӷ�ΪO(mn)
    for(int i=0;i<=n;i++)
    {
        for(int j=0;j<=m;j++)
        {
            if(i==0 || j==0) res[i][j]=0;
            else if(a[i]==b[j])
            {
                res[i][j]=res[i-1][j-1]+1;path[i][j]=1;
            }
            else if(a[i]!=b[j])
            {
                res[i][j]=max(res[i-1][j],res[i][j-1]);
                if(res[i-1][j]>res[i][j-1]) path[i][j]=2;
                else path[i][j]=3;
            }
        }
    }
    int lcs=res[n][m];int len0=lcs;
    for(int i=0;i<=n;i++)
    {
        for(int j=0;j<=m;j++)
        {
            cout<<res[i][j]<<" ";
        }
        cout<<endl;
    }

    while(n>0 && m>0)
    {
        if(path[n][m]==1)
        {
            result[lcs--]=a[n];
            n--;m--;
        }
        else if(path[n][m]==2)
            n--;
        else if(path[n][m]==3)
            m--;
    }

    for(int i=1;i<=len0;i++)
    {
        cout<<result[i]<<" ";
    }

    return 0;
}
