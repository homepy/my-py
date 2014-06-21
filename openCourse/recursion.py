def isPalindrome(s):
    assert isinstance(s, str)

    if s == '' or len(s) == 1:
        return True
    else:
        return s[0] == s[-1] and isPalindrome(s[1:-2])


"""递归 可分为以下两类，求全排列及求子集
    或 进一歩 全排列的子集 子集的全排列..."""


def rec_permute(sofar, rest):
    if rest == '':  # if not rest  would be more pythonic, but less readable
        print(sofar)
    else:
        for i in range(0, len(rest)):
            next = sofar + rest[i]
            remaining = rest[0:i] + rest[i + 1:]  # rest = rest del rest[i]
            rec_permute(next, remaining)


def list_permutations(s):
    """ list all permutations of char in string s

    eg. s="ABC"
    输出 AB 的全排列 AB, BA

    """
    rec_permute('', s)


def rec_subsets(sofar, rest):
    if rest == '':
        print(sofar)
    else:
        rec_subsets(sofar + rest[0], rest[1:])
        rec_subsets(sofar[:], rest[1:])


def list_subsets(s):
    """list all subsets of string s

    eg.
    s='ab', 输出下面四个子集
    'ab'
    'a'
    'b'
    ''

    """
    rec_subsets('', s)

list_permutations('ABC')
list_subsets('ab')
print(isPalindrome('121'))
print(isPalindrome(''))
print(isPalindrome('22'))
