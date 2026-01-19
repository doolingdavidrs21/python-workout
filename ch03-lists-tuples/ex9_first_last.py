"""
Docstring for ch03-lists-tuples.ex9_first_last
Write a function, firstlast, that takes a
sequence (string, list, or tuple) and returns
the first and last elements of that sequence, in
a two-element sequence of the same type. So
firstlast('abc') will return the string ac, while
firstlast([1,2,3,4]) will return the list [1,4].
"""

def firstlast(seq):
    if len(seq) == 0:
        raise ValueError("The sequence must have at least one element.")
    return type(seq)([seq[0], seq[-1]]) if isinstance(seq, (list, tuple)) else seq[0] + seq[-1]

