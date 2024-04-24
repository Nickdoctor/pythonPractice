# Modify the following header to represent your submission
# reverse.py Nicolas Gugliemo (ngugliemo@csus.edu) for CSC 135 Spring 2024
# Implements mergesort
# Worked with Ellen Watermellon
# Used Stack Overflow page at https://stackoverflow.com/questions/5785745

from List135 import List135


# Returns a List135 that is the same as xs but in reverse order
# Function is tail-recursive to enable compiler optimization
# [] --> []; [1] --> [1]; [1,2] --> [2,1]; [1,2,3] --> [3,2,1]; etc.
def _reverse(xs, acc):
    if xs.empty():
        return acc
    else:
        newAcc = acc.add(xs.first())
        return _reverse(xs.rest(), newAcc)


def reverse(xs):
    acc = List135()
    return _reverse(xs, acc)  # Begin accumulation with an empty list


# If you run this file, the indented code below will run. This is a
# suitable place for you to put testing code. When I test your code
# using a separate file, the code below will not be run. to be eligible
# for credit, your code must run the following without sytax or runtime
# errors. Leave your test cases here, indented, so that I can see them.
if __name__ == '__main__':
    a = List135().add(3).add(1).add(5).add(2).add(4)
    b = reverse(a)
    print(a)
    print(b)

    c = List135().add(1).add(-10).add(0).add(0)
    print("List to be reversed: " + str(c))
    d = reverse(c)
    print("Test Case #1 C should be unchanged: " + str(c))
    print("Test Case #1 D should be reversed from C: " + str(d))

    e = List135()
    print("List to be reversed: " + str(e))
    f = reverse(e)
    print("Test Case #1 E should be unchanged: " + str(e))
    print("Test Case #1 F should be reversed from E: " + str(f))

    g = List135().add(1)
    print("List to be reversed: " + str(g))
    h = reverse(g)
    print("Test Case #1 G should be unchanged: " + str(g))
    print("Test Case #1 H should be reversed from G: " + str(h))
