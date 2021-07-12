class quick_sort(object):
    def __init__(self):
        pass
    def partition(self,array,left_index,right_index):
        '''
        隔断函数，把函数划分为左边都比某个值小，右边都比某个值大
        input:array,left,right
        output:返回简单隔断之后的最右边的index
        '''
        x=array[right_index]
        i=left_index-1
        #从lef到rig-1遍历
        for j in range(left_index,right_index):
            if array[j]<=x:
                i+=1
                #exchange a[i] a[j]
                temp=array[i]
                array[i]=array[j]
                array[j]=temp
            else:pass
            '''
            i在最外面减一，在循环里面再先加一再交换位置
            为了保证如果存在连续的比右边大的数，那么i的位置可以保证
            它的对应值一直比右边的小
            '''
        #i+1位置的值是比x要大的值，它的右边全部都是比x大的
        #所以交换它与x的位置就可以得到符合要求的隔断序列
        #exchange a[rignt] a[i+1]
        temp=array[right_index]
        array[right_index]=array[i+1]
        array[i+1]=temp
        return i+1
    def quick_sort(self,array,left_index,right_index):
        if left_index<right_index:
            #递归结束条件就是左右位置相遇
            index=self.partition(array,left_index,right_index)
            #对于index的位置，无需再进行递归，所以后面的对应-1和+1
            self.quick_sort(array,left_index,index-1)
            self.quick_sort(array,index+1,right_index)
        return array
if __name__=="__main__":
    array=[2,8,7,1,3,5,6,4]
    lef=0
    rig=len(array)-1
    sort=quick_sort()
    res=sort.quick_sort(array=array,left_index=lef,right_index=rig)
    print(res)