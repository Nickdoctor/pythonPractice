# Modify the following header to represent your submission
# count.py Nicolas Gugliemo (ngugliemo@csus.edu) for CSC 135 Spring 2024
# Implements mergesort
# Worked with Ellen Watermellon
# Used Stack Overflow page at https://stackoverflow.com/questions/5785745

from List135 import List135


# Returns how many times x is found inside List135 xs (uses == to test equality)
# Function does NOT use tail-recursion or accumulators.
# [], 1 --> 0; [1], 1 --> 1; [1,2], 1 --> 1; [1,2,1], 1 --> 2; etc.
def count(xs, x):
    total = 0
    while not xs.empty():
        if xs.first() == x:
            total = total + 1
            xs = xs.rest()
        else:
            xs = xs.rest()

    return total


# If you run this file, the indented code below will run. This is a
# suitable place for you to put testing code. When I test your code
# using a separate file, the code below will not be run. to be eligible
# for credit, your code must run the following without sytax or runtime
# errors. Leave your test cases here, indented, so that I can see them.
if __name__ == '__main__':
    a = List135().add(1).add(2).add(1)
    print(count(a, 1) == 2)
    b = List135().add(1).add(2).add(3).add(4).add(1).add(1)
    print("B's list should count 3 ones in the list, Test case 1: " + str(count(b, 1)))
    c = List135()
    print("C's list should count 0 ones in the list, Test case 2: " + str(count(c, 1)))
    d = List135().add(-1).add(-100).add(10000)
    print("D's list should count 1 negative one in the list, Test case 3: " + str(count(d, -1)))
