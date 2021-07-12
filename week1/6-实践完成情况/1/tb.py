
def partition(arr, left, right):
    pivot = arr[left]
    while (left < right):

        while(left < right and arr[left] <= pivot):
            left+=1
        arr[right] = arr[left]
        while (left < right and arr[right] >= pivot):
            right -= 1
        arr[left] = arr[right]
    arr[right]= pivot
    return left


def quick_sort(arr, left=None, right=None):
    left = 0 if not isinstance(left, (int, float)) else left
    right = len(arr) -1 if not isinstance(right, (int, float)) else right
    if (left < right):
        pivot = partition(arr, left, right)
        quick_sort(arr, left, pivot-1)
        quick_sort(arr, pivot+1, right)
    return arr


if __name__=='__main__':
    a=[1,5 ,7 ,9 ,0,20,11,155,87,4]
    b=quick_sort(a)
    print(b)

