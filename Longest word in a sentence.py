def longest_word(sentence):
    words = sentence.split()
    return max(words, key=len)

# Example usage:
sentence = "Python programming is fun"
print(longest_word(sentence))  # Output: "programming"
