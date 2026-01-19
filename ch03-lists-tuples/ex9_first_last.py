"""
Docstring for ch03-lists-tuples.ex9_first_last
Write a function, firstlast, that takes a
sequence (string, list, or tuple) and returns
the first and last elements of that sequence, in
a two-element sequence of the same type. So
firstlast('abc') will return the string ac, while
firstlast([1,2,3,4]) will return the list [1,4].
"""

# def firstlast(seq):
#     if len(seq) == 0:
#         raise ValueError("The sequence must have at least one element.")
#     return type(seq)([seq[0], seq[-1]]) if isinstance(seq, (list, tuple)) else seq[0] + seq[-1]


def firstlast(seq):
    return seq[:1] + seq[-1:]


def even_odd_sums(seq):
    even_sum = sum(seq[::2])
    odd_sum = sum(seq[1::2])
    return [even_sum, odd_sum]


def plus_minus(seq):
    """
    Takes a list or tuple of numbers and retuns the result
    of alternately adding and subtracting numbers from each
    other.
    So calling the function as plus_minus([10, 20, 30, 40, 50, 60]),
    you’ll get back the result of 10+20-30+40-50+60, or 50.
    :param seq: Description
    """
    total = seq[0]
    for index, value in enumerate(seq[1:]):
        print(index, index % 2,  value, total)
        if index % 2 == 0:
            total += value
        else:
            total -= value
    return total

def myzip(*args):
    min_length = min(len(arg) for arg in args)
    result = []
    for i in range(min_length):
        result.append(tuple(arg[i] for arg in args))
    return result



if __name__ == "__main__":
    print(plus_minus([10, 20, 30, 40, 50, 60]))
    print(myzip([10,20,30], 'abc'))

