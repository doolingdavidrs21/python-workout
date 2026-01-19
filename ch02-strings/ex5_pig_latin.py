def pig_latin(word):
    """
    Convert a given word to Pig Latin.
    Rules:
    - If the word starts with a vowel (a, e, i, o, u), add "way" to the end of the word.
    - If the word starts with a consonant, move the first letter to the end and add "ay".
    """
    word = word.lower()
    vowels = 'aeiou'
    if word[0] in vowels:
        return word + 'qay'
    else:
        return word[1:] + word[0] + 'ay'