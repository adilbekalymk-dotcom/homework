def selection_sort(arr):
    for i in range(len(arr)):
        m = i
        for j in range(i + 1, len(arr)):
            arr[i], arr[m] = arr[m], arr[i]
            return arr

        print(selection_sort([5, 2, 9, 1, 5, 6]))