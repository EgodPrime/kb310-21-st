def swap(array, i, j):
    array[i], array[j] = array[j], array[i]


def Quick_Sort(array, left = None, right = None):
    left = 0 if not isinstance(left, (int, float)) else left
    right = len(array) - 1 if not isinstance(right, (int, float)) else right
    if left < right:
        index = find_index(array, left, right) - 1
        Quick_Sort(array, left, index - 1)
        Quick_Sort(array, index + 1, right)
    return array

def find_index(array, left, right):
    pivot = left
    index = left + 1
    i = index
    while(i < right+1):
        if(array[i] < array[pivot]):
            swap(array, i, index)
            index+=1
        i+=1
    swap(array, pivot, index-1)
    return index



if __name__=='__main__':
    a=[5,1,6,7,87,4,4,6,73,7,3,7]
    b=Quick_Sort(a)
    print(b)