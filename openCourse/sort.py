def merge_sort(L):
    """merge sort 归并排序 O(N * log N)

    分解logN次,得N个len为1的list,
    tree每层merge的复杂度均为N
    (最底层, merge开销为1, N次merge
    底+1层, merge开销为2, N/2次merge)

    """
    assert isinstance(L, list) and all(isinstance(e, (int, float)) for e in L)
    print(L)

    if len(L) == 1:
        return L[:]
    else:
        middle = len(L) / 2
        left = merge_sort(L[0:middle])
        right = merge_sort(L[middle:])
        together = merge(left, right)
        print('merged', together)
        return together


def merge(left, right):
    """合并两个已排序的list O(N)   N = len(left) + len(right)"""
    result = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i = i + 1
        else:
            result.append(right[j])
            j = j + 1

    while i < len(left):
        result.append(left[i])
        i = i + 1
    while j < len(right):
        result.append(right[j])
    return result


def bubble_sort(L):
    """bubble sort 冒泡排序 O(n^2)  worst sort...

    L: a list of numbers
    """
    #assert isinstance(L, list) and all(isinstance(e, (int, float)) for e in L)

    for i in range(len(L)):  # 第1次,L中最大的最大数被移到最后;
                             # 第2次,移第二大的数到次后
        for j in range(len(L) - 1):
            if L[j] > L[j+1]:
                L[j], L[j+1] = L[j+1], L[j]
#        print(L, i+1)
    return L


def selection_sort(L):
    """selection_sort 选择排序 O(n^2) always

    L: a list of numbers

    """
    print(L)

    for i in range(len(L)):
        min_val = L[i]
        min_index = i
        is_swap = False

        for j in range(i+1, len(L)):
            if min_val > L[j]:
                is_swap = True
                min_val = L[j]
                min_index = j

        if is_swap:
            L[i], L[min_index] = L[min_index], L[i]

#        print(L, i+1)

    return L


def test_s():
    L1 = [10, 9, 8, 7, 6, 5, 4, 1]
    L2 = [20, 10, 40, 30, 60, 50, 80, 70]
    selection_sort(L1)
    selection_sort(L2)


def test_b():
    L1 = [10, 9, 8, 7, 6, 5, 4, 1]
    L2 = [20, 10, 40, 30, 60, 50, 80, 70]
    bubble_sort(L1)
    bubble_sort(L2)
