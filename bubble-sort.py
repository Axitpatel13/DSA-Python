#create an array
arr = [12,24,36,3,23,43]
def bubble_sort_check(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0,n-i-1):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
print(arr)
bubble_sort_check(arr)
print(arr)