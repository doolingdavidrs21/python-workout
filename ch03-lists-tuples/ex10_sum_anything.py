"""
Docstring for ch03-lists-tuples.ex10_sum_anything
The result should be a new, longer sequence
of the type provided by the parameters.
Thus, the result of mysum('abc', 'def') will
be the string abcdef, and the result of mysum([1,2,3], [4,5,6])
will be the six-element list [1,2,3,4,5,6].
Of course, it should also still return the
integer 6 if we invoke mysum(1,2,3).
"""

def mysum(*args):
    total = args[0]
    for i, item in enumerate(args[1:]):
        total += item
    return total

if __name__ == '__main__':
    print([1,2,3,4,5])
    print(mysum(1,2,3,4,5))
    print(('abc','def','ghi'))
    print(mysum('abc', 'def', 'ghi'))
    print([1,2,3], [4, 5, 6], [7, 8, 9])
    print(mysum([1,2,3], [4,5,6], [7,8,9]))