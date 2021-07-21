#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Zhang Chi

#选择一个元素值为初始值，将比它小的元素移动到它的左边，将比它大的元素移动到它的右边
def quick_sort(arrs,i,j):
    if i >=j:
        return arrs #排序结束
    start=arrs[i]
    left=i
    right=j
    while i<j:
        while i<j and arrs[j]>=start: #arrs[j]比start大则继续寻找
            j=j-1 #j从右往左移动
        arrs[i]=arrs[j] #arrs[j]比start小则交换
        while i<j and arrs[i]<=start: #arrs[i]比start小则继续寻找
            i=i+1 #i从左往右移动
        arrs[j]=arrs[i] #arrs[i]比start大则交换
    arrs[j]=start #i和j相遇则start与arr[j]交换
    quick_sort(arrs,left,i-1) #对比start小的元素进行排序
    quick_sort(arrs,i+1,right) #对比start大的元素进行排序
    return arrs
#test
if __name__ =="__main__":
    arrs=[30,24,5,58,18,36,12,42,39]
    print("排序前的序列为：")
    for i in arrs:
        print(i,end =" ")
    print("\n排序后的序列为：")
    for i in quick_sort(arrs,i=0,j=len(arrs)-1):
        print(i,end=" ")