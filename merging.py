def merge(arr1, arr2):
    m, n = len(arr1), len(arr2)
    arr1.extend([0] * n)
    i, j, k = m - 1, n - 1, m + n - 1

    while j >= 0:
        if i >= 0 and arr1[i] > arr2[j]:
            arr1[k] = arr1[i]
            i -= 1
        else:
            arr1[k] = arr2[j]
            j -= 1
        k -= 1

    arr2[:] = arr1[m:]
    arr1[:] = arr1[:m]

test_cases = [
    ([1, 3, 5], [2, 4, 6]),
    ([10, 12, 14], [1, 3, 5]),
    ([2, 3, 8], [4, 6, 10]),
    ([1], [2]),
    (list(range(1, 100001)), list(range(50001, 100001))),
]

for i, (arr1, arr2) in enumerate(test_cases, 1):
    merge(arr1, arr2)
    print(f"Test Case {i}: arr1 = {arr1}, arr2 = {arr2}")
