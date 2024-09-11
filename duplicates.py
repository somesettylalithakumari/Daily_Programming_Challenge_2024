def D(arr):
    i = j = arr[0]
    while True:
        i = arr[i]
        j = arr[arr[j]]
        if i == j:
            break
    i = arr[0]
    while i != j:
        i = arr[i]
        j = arr[j]
    return j

print(D([1, 3, 4, 2, 2]))
print(D([3, 1, 3, 4, 2]))
print(D([1, 1]))
print(D([1, 4, 4, 2, 3]))
print(D(list(range(1, 100000)) + [50000]))
