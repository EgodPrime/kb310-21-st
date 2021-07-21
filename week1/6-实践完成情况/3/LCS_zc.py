#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Zhang Chi

#行数使用i来标记，列数使用j来标记
#初始化后表的行数和列数都比输入数组的长度多1，所以c和flag矩阵下标为0到len
def LCS(a,b):
    lena=len(a)
    lenb=len(b)
    c=[[0 for i in range(lenb+1)] for j in range(lena+1)] #初始化LCS表
    flag=[[0 for i in range(lenb+1)] for j in range(lena+1)] #初始化推导表
    for i in range(lena):
        for j in range(lenb):
            if a[i]==b[j]: #找到公共元素
                c[i+1][j+1]=c[i][j]+1 #LCS表的值为左上角元素值加1
                flag[i+1][j+1]='ok' #标记为公共元素点
            elif c[i+1][j]>c[i][j+1]: #左边的元素比上边的元素大
                c[i+1][j+1]=c[i+1][j] #LCS表的值为两者中较大的数
                flag[i+1][j+1]='left' #标记为寻找公共元素需要左移
            else: #上边的元素比左边的元素大
                c[i+1][j+1]=c[i][j+1] #LCS表的值为两者中较大的数
                flag[i+1][j+1]='up' #标记为寻找公共元素需要上移
    return c,flag

def LCS_flag(flag,a,i,j):
    if i==0 or j==0:
        return
    if flag[i][j]=='ok':
        LCS_flag(flag,a,i-1,j-1) #flag移动到左上方元素点位置
        print(a[i-1],end=' ') #输出公共元素
    elif flag[i][j]=='left': #左移
        LCS_flag(flag,a,i,j-1) #flag移动到左边元素点位置
    else: #上移
        LCS_flag(flag,a,i-1,j) #flag移动到上边元素点位置

a=[1,2,3,4,5,6,7,8]
b=[2,4,6,7,8,7,4]
c,flag=LCS(a,b)
#print('LCS表为：')
#for i in c:
#	print(i)
#print('\n')
#print('推导表为：')
#for j in flag:
#	print(j)
#print('\n')
print('最长公共子序列为：\n')
LCS_flag(flag,a,len(a),len(b))

