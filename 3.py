def sel_sort(array):
    for i in range(len(array)):
        m = i
        for j in range(i + 1, len(array)):
            if array[j] > array[m]:
                m = j
        array[i], array[m] = array[m], array[i]

a = list(map(int, input().split()))
sel_sort(a)
print(*a)