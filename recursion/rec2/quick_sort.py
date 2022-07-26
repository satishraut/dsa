def quickSort(arr, start, end):
    if end - start <= 1:
        return
    pivot = start
    count = start
    for i in range(start + 1, end):
        if arr[i] <= arr[pivot]:
            count += 1
    temp = arr[pivot]
    arr[pivot] = arr[count]
    arr[count] = temp
    pivot = count

    left = start
    right = end - 1
    while left < pivot:
        while arr[left] <= arr[pivot] and left < pivot:
            left += 1
            if left >= pivot:
                break
        while arr[right] > arr[pivot]:
            right -= 1
        temp = arr[left]
        arr[left] = arr[right]
        arr[right] = temp
        left += 1
        right -= 1
    quickSort(arr, start, pivot)
    quickSort(arr, pivot + 1, end)


n = int(input())
arr = list(int(i) for i in input().strip().split(' '))
quickSort(arr, 0, n)
print(*arr)
