def fast_max_value(w, v, i, aw, m=None):
    """
    max_value

    w, weight
    v, value
    i, index
    aw, available valie
    m, memoization
    """
    if m is None:
        m = {}
    global numcalls1
    numcalls1 += 1

    try:
        return m[(i, aw)]
    except KeyError:
        if i == 0:
            if w[i] <= aw:
                m[(i, aw)] = v[i]
                return v[i]
            else:
                m[(i, aw)] = 0
                return 0
        without_i = fast_max_value(w, v, i-1, aw)
        if w[i] > aw:
            m[(i, aw)] = without_i
            return without_i
        else:
            with_i = v[i] + fast_max_value(w, v, i-1, aw-w[i])
            res = max(without_i, with_i)
            m[(i, aw)] = res
            return res


def max_value(w, v, i, aw):
    """
    max_value

    w, weight
    v, value
    i, index
    aw, available valie
    """
    global numcalls2
    numcalls2 += 1

    if i == 0:
        if w[i] <= aw:
            return v[i]
        else:
            return 0

    without_i = max_value(w, v, i-1, aw)
    if w[i] > aw:
        return without_i
    else:
        with_i = v[i] + max_value(w, v, i-1, aw-w[i])
        return max(without_i, with_i)


weights = [2, 1, 5, 3, 4, 2, 4, 3, 4]
values = [10, 15, 10, 9, 5, 6, 17, 5, 11]
numcalls1 = 0
numcalls2 = 0
res1 = fast_max_value(weights, values, len(values)-1, 12)
res2 = max_value(weights, values, len(values)-1, 12)
print(res1, numcalls1)
print(res2, numcalls2)
