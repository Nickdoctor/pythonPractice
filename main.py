from List135 import List135
from functools import reduce


# Problem 1: The maximum distance between any element of the pyhton list
# [-1,2,0] and the number 1 is 2 because abs(-1 - 1) is larger than abs(2 - 1)
# and abs(0 - 1). The following two functions can be used together to find such
# maximum distances.

# Write a function that uses some combination of map, reduce, filter
# and/or lambda that takes a python list of numbers xs and a number c as
# parameters and produces a python list of the distances each element
# x is from c (ie, abs(x-c)). For example dists([-1, 2, 0], 1) should return
# [2, 1, 1]. You may use the builtin function abs(x) in your lambda.
def dists(xs, c):
    newxs = list(map(lambda x: abs(c - x), xs))
    return newxs


# Write a function max_nonempty that takes a nonempty python list
# of numbers and returns the largest number. Use reduce to do this by
# using the builtin function max(a,b) in your lambda.
def max_nonempty(xs):
    return reduce(lambda acc, x: max(acc, x), xs)


# Problem 2: Write a function that takes a unary boolean function and a python
# list as parameters and returns True if more elements of the list make f True
# than make it false. For example more_true(lambda x: x%2==0, [1,2,3,4])
# should return False because 2 elements make it True and 2 make it False.
def more_true(f, xs, accTrue=0, accFalse=0):
    if len(xs) == 0:
        return True if accTrue > accFalse else False
    else:
        if f(xs.pop()) == True:
            accTrue = accTrue + 1
        else:
            accFalse = accFalse + 1
        return more_true(f, xs, accTrue, accFalse)


# NOTE: The following are client functions of List135. They must not
# access the _data or _next fields. Only the first(), rest(), add(),
# and empty() methods and no-argument List135() constructor are allowed.

# Problem 3: Write a recursive function firstN that takes a List135 xs as a
# parameter and returns a new List135 composed of the first n elements
# of xs. For example firstN([1,2,3], 2) would produce [1,2]. You may
# assume 0 <= n <= len(xs). Hint: n == 0 is your base case.
def _firstN(xs, n, acc):
    if n == 0:
        print("HERE1")
        return acc
    if xs.empty() == 0:
        return acc
    else:
        print("HERE3")
        newacc = acc.add(xs.first())
        return _firstN(xs.rest(), n - 1, newacc)


def firstN(xs, n):
    acc = List135()
    return _firstN(xs, n, acc)


# Problem 4: The following function returns how many elements of a List135
# are greater than x. Rewrite it to be tail recursive. You may add a helper
# function or an extra parameter with a default value if you want to.
#
# def num_greater(xs, x):
#    if xs.empty():
#        return 0
#    else:
#        cnt = 0
#        if xs.first() > x:
#            cnt = 1
#        return cnt + num_greater(xs.rest(), x)
def _num_greater(xs, x, acc):
    if xs.empty():
        return acc
    else:
        if xs.first() > x:
            acc = acc +1
        return _num_greater(xs.rest(),x,acc)
def num_greater(xs, n):
    acc = 0
    return _num_greater(xs, n, acc)

# Midterm testing will ignore the following indented code. You test here.
if __name__ == '__main__':
    xs = List135().add(3).add(2).add(1)
    ys = dists([-1, 2, 0], 1)
    print(1, isinstance(ys, list))
    print(1, ys == [2, 1, 1])
    print(2, max_nonempty([2, 1, 1]) == 2)
    print(3, more_true(lambda x: x % 2 == 0, [1, 2, 3, 4]) == False)
    print(xs)
    ys = firstN(xs, 2)
    print(ys)
    print(4, isinstance(ys, List135))
    print(4, str(ys) == "[1,2]")
    print(str(ys))
    print(5, num_greater(xs, 1) == 2)
