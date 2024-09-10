def find_missing(arr):
    n = len(arr) + 1
    total= n * (n + 1) // 2
    x = sum(arr)
    return total - x
arr = [1, 2, 3, 4]
print(find_missing(arr))  

