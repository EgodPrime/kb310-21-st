
class lcs(object):
    '''
    对两个字符串查找最大公共子序列
    找到最大公共子序列的长度以及它的内容
    转移方程：
        c[i,j]=c[i-1,j-1]+1  xi=yj
        c[i,j]=max(c[i-1],j),c[i,j-1])  xi!=yj 
        不相等的时候，是两者的较大者
    '''
    def __init__(self,first_string,second_string):
        self.first_string=first_string
        self.second_string=second_string
    def lcs_length(self):
        i=len(self.first_string)
        j=len(self.second_string)
        #初始化c[][]
        #sym作为标记,1表示等,2表示不等,3表示不等
        c=[[0 for _ in range(j+1)] for _ in range(i+1)]
        sym=[[0 for _ in range(j+1)] for _ in range(i+1)]
        #ls作为序列保存
        ls=[]
        '''
        for l in range(i+1):
            c[l][0]=0
        for l in range(j+1):
            c[0][l]=0
        '''
        #开始计算公共长度
        for ii in range(1,i+1):
            for jj in range(1,j+1):
                if self.first_string[ii-1]==self.second_string[jj-1]:
                    c[ii][jj]=c[ii-1][jj-1]+1
                    sym[ii][jj]=1
                #把两种情况分开，用于sym进行标记
                elif c[ii-1][jj]>=c[ii][jj-1]:
                    
                    c[ii][jj]=c[ii-1][jj]
                    sym[ii][jj]=2
                else :
                    c[ii][jj]=c[ii][jj-1]
                    sym[ii][jj]=3
        #找出序列
        li=i
        lj=j
        while li!=0 and lj!=0:
            if sym[li][lj]==1:
                ls.append(self.second_string[lj-1])
                li-=1
                lj-=1
            elif sym[li][lj]==2:
                li-=1
            else:lj-=1
        sum_c=c[i][j]
        ls=ls[::-1]
        return c,sym,ls,sum_c

if __name__=="__main__":
    f=['a','b','c','b','d','a','b']
    s=['b','d','c','a','b','a']
    ls=lcs(f,s)
    c,d,e,f=ls.lcs_length()
    print(c,d,e,f)
