def find_min_max(arr):
    if not arr:
        return None, None
    minimum = maximum = arr[0]
    for x in arr[1:]:
        if x < minimum:
            minimum = x
        elif x > maximum:
            maximum = x
    return minimum, maximum

if __name__ == "__main__":
    data = [10, 2, 33, -1, 14]
    mn, mx = find_min_max(data)
    print(f"Min: {mn}, Max: {mx}")
