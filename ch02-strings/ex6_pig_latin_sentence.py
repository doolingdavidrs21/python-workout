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
        return word + 'way'
    else:
        return word[1:] + word[0] + 'ay'

def pig_latin_sentence(sentence):
    """
    Convert a given sentence to Pig Latin by converting each word individually.
    """
    words = sentence.split()
    pig_latin_words = [pig_latin(word) for word in words]
    return ' '.join(pig_latin_words)