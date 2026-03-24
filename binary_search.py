def binary_search_iterative(arr, key):
    lo, hi = 0, len(arr) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if arr[mid] == key:
            return mid
        elif arr[mid] < key:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1


def binary_search_recursive(arr, key, lo=0, hi=None):
    if hi is None:
        hi = len(arr) - 1
    if lo > hi:
        return -1
    mid = (lo + hi) // 2
    if arr[mid] == key:
        return mid
    if arr[mid] < key:
        return binary_search_recursive(arr, key, mid + 1, hi)
    return binary_search_recursive(arr, key, lo, mid - 1)

if __name__ == "__main__":
    arr = [1, 3, 5, 7, 9]
    t = 7
    print("Iterative:", binary_search_iterative(arr, t))
    print("Recursive:", binary_search_recursive(arr, t))
