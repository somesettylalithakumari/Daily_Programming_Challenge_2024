def sort(arr):
    i, j, k = 0, 0, len(arr) - 1
    while j <= k:
        if arr[j] == 0:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j += 1
        elif arr[j] == 1:
            j += 1
        else:
            arr[j], arr[k] = arr[k], arr[j]
            k -= 1

arr = [0, 1, 2, 1, 0, 2, 1, 0]
sort(arr)
print(arr)
