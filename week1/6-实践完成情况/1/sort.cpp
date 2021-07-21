//Author Jiang shihao 
#include<cstdio>
#include<iostream>
using namespace std;
const int N = 1e5;
int a[N];

void change(int a,int b)
{
    int t=a;
    a=b;
    b=t;
}


void quicksort(int begin,int end)  //nlgn¸´ÔÓ¶È ²»ÎÈ¶¨ÅÅÐò
{
    if(begin>=end) return;
    int p=begin;
    int q=end;
    int v=a[begin];
    while(begin<end)
    {
        while(a[end]>=v && begin<end)
        end --;
        if(begin<end) a[begin]=a[end];

        while(a[begin]<=v && begin<end)
        begin ++;
        if(begin<end) a[end]=a[begin];
    }
    a[begin]=v;
    quicksort(p,begin-1);
    quicksort(begin+1,q);

}

int main()
{
      int n;
      cin>>n;
      for(int i=1;i<=n;i++)
      {
          cin>>a[i];
      }
      quicksort(1,n);

      for(int i=1;i<=n;i++)
      {
          cout<<a[i]<<" ";
      }
}
