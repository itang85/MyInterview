def quick_sort(arr, left, right):
    if left >= right:
        return arr

    l = left
    r = right
    key = arr[left]

    while l < r:
        while arr[r] >= key and l < r:
            r -= 1
        while arr[l] <= key and l < r:
            l += 1

        arr[l], arr[r] = arr[r], arr[l]
        print(arr, l, r, key)
    arr[left], arr[l] = arr[l], arr[left]

    quick_sort(arr, left, l-1)
    quick_sort(arr, r+1, right)

    return arr

array = [65,2,4,2,1,4,5,6,4,7,65,4,1]
print(quick_sort(array, 0, len(array)-1))

