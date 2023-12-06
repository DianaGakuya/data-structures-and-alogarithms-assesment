from questions import is_balanced, remove_duplicates, word_frequency

# Test for is_balanced function
expression1 = "([]{})"
expression2 = "([)]"
print(is_balanced(expression1))  # Expected Output: True
print(is_balanced(expression2))  # Expected Output: False 

# Test for remove_duplicates function
input_sequence = [2, 3, 2, 4, 5, 3, 6, 7, 5]
result = remove_duplicates(input_sequence)
print(result)  # Expected Output: [2, 3, 4, 5, 6, 7]

# Test for word_frequency function
sentence = "This is a test sentence. This sentence is a test."
result = word_frequency(sentence)
print(result)  # Expected Output: {'this': 2, 'is': 2, 'a': 2, 'test': 2, 'sentence': 2}
