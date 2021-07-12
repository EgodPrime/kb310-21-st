#include <iostream>
#include <vector>
#include <string>
using namespace std;



void d2arr1() //直接生成二维数组
{
    int n = 5, m = 6;
    vector<vector<int>> arr(n, vector<int>(m));

    for(int i=0; i<arr.size(); i++)
    {
        for(int j=0; j<arr[i].size(); j++)
        {
            cout<<arr[i][j]<<",";
        }
        cout<<"\n";
    }
}

void d2arr2()
{
    int n = 5, m = 6;
    vector<vector<int>> arr;
    arr.resize(n); //arr成n行
    for(int i=0; i<arr.size(); i++)
    {
        arr[i].resize(m);
    }
    for(int i=0; i<arr.size(); i++)
    {
        for(int j=0; j<arr[i].size(); j++)
        {
            cout<<arr[i][j]<<",";
        }
        cout<<"\n";
    }

}

void lcslen(string x, string y, vector<vector<int>> &c, vector<vector<int>> &b)
{
    //建表, c为长度表， b为记录相等表
    int m = x.size();
    int n = y.size();
    c.resize(m+1);
    b.resize(m+1);
    for(int i = 0; i < c.size(); i++)
    {
        c[i].resize(n+1);
    }
    for(int i = 0; i < b.size(); i++)
    {
        b[i].resize(n+1);
    }
    //动规
    for(int i = 1; i <= m; i++)
    {
        for(int j = 0; j <= n; j++)
        {
            if(x[i] == y[j])
            {
                c[i][j] = c[i-1][j-1] + 1;
                b[i][j] = 2; //b[i][j]=2时，说明此处两序列元素相等
            }
            else
            {
                if(c[i-1][j] >= c[i][j-1])
                {
                    c[i][j] = c[i-1][j];
                    b[i][j] = 1; 
                }
                else
                {
                    c[i][j] = c[i][j-1];
                    b[i][j] = 3;
                }
            }
        }
    }
}

void print_lcs(vector< vector<int>> &b,string x, int i, int j)
{
    if(i == 0 || j == 0)
        return;
    if(b[i][j] == 2)
    {
        print_lcs(b,x,i-1,j-1);
        cout << x[i-1];
    }
    else 
    {
        if(b[i][j] == 1)
            print_lcs(b,x,i-1,j);
        else
            print_lcs(b,x,i,j-1);
    } 
}


int main()
{
    string x = "BCBDABAC";
    string y = "DCABACB";
    vector< vector<int>> c;
    vector< vector<int>> b;
    cout<<"x: "<<x<<"\n";
    cout<<"y: "<<y<<"\n";
    lcslen(x,y,c,b);
    cout<<"LCS: ";
    print_lcs(b,x,x.size(),y.size());
}