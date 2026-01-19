"""
In Ubbi Dubbi, every vowel (a, e, i, o, or u) is
prefaced with ub.
Thus milk becomes mubilk (m-ub-ilk) and program becomes
prubogrubam (prub-ogrub-am). In theory, you only put an
ub before every vowel sound, rather than before
each vowel. Given that this is a book about
Python and not linguistics, I hope that you’ll
forgive this slight difference in definition.
"""


def ubbi_dubbi(word:str):
    """
    Convert a given word to Ubbi Dubbi.
    Rules:
    - For every vowel (a, e, i, o, u) in the word, add "ub" before it.
    """
    word = word.lower()
    vowels = 'aeiou'
    ubbi_dubbi_word = []
    for char in word:
        if char in vowels:
            ubbi_dubbi_word.append('ub' + char)
        else:
            ubbi_dubbi_word.append(char)
    return ''.join(ubbi_dubbi_word)


