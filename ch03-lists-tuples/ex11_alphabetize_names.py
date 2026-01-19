PEOPLE = [
    {
        'first':'Reven',
        'last':'Lerner',
        'email':'reuven@lerner.co.il'
    },
    {
        'first':'Donald',
        'last':'Trump',
        'email':'president@whitehouse.gov'
    },
    {
        'first':'Vladimir',
        'last':'Putin',
        'email':'president@kremvax.ru'
    }
]


def alphabetize_names(people):
    """
    Takes a list of dictionaries containing 'first' and 'last' name keys,
    and returns a list of full names sorted alphabetically by last name,
    then by first name.
    :param people: List of dictionaries with 'first' and 'last' keys
    :return: List of full names sorted by last and first names
    """
    full_names = [f"{person['last']} {person['first']} {person['email']}" for person in people]
    return sorted(full_names, key=lambda name: (name.split()[0], name.split()[1]))


def sort_by_abs(seq):
    """
    Given a sequence of positive and negative numbers, return a
    them sorted by absolute value
    """
    if seq:
        return sorted(seq, key=abs)


def sort_by_vowel_count(seq):
    """
    Given a sequence of strings, return them sorted by
    the number of vowels in each string.
    """
    vowels = 'aeiouAEIOU'
    def vowel_count(s):
        return sum(1 for char in s if char in vowels)
    return sorted(seq, key=vowel_count,reverse=True)





if __name__ == "__main__":
    sorted_names = alphabetize_names(PEOPLE)
    for name in sorted_names:
        print(name)
    print(sort_by_abs((-10, 5, -30, 20, 0, -15, 25)))
    print(sort_by_abs([4,5,10,-90,3.4]))
    print(sort_by_vowel_count(['apple', 'banana', 'kiwi', 'grapefruit', 'pear']))




