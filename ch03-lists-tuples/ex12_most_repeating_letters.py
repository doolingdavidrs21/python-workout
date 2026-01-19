def most_repeating_word(words):
    max_repeats = 0
    result_word = ""

    for word in words:
        letter_counts = {}
        for letter in word:
            letter_counts[letter] = letter_counts.get(letter, 0) + 1

        current_max = max(letter_counts.values())
        if current_max > max_repeats:
            max_repeats = current_max
            result_word = word

    return result_word, max_repeats

if __name__ == "__main__":
    words = ["this", "is", "an", "elemetary", "test", "example"]
    print(most_repeating_word(words))

