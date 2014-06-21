def bisearch(s, e, first, last, count=1):
    """ bisearch 二分查找

    s: a list
    e: element
    first: first index
    last: last index
    count: counter of calls

    1, pick the mid point
    2, check mid == answer?
    3, if not, reduse, repeat

    """
    print(first, last, count)
    mid = (first + last) // 2
    if e == s[mid]:
        return mid
    elif e < s[mid]:
        bisearch(s, e, first, mid - 1, count + 1)
    elif e > s[mid]:
        bisearch(s, e, mid + 1, last, count + 1)
