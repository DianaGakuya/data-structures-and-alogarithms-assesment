#Stacks (is_balanced)
def is_balanced(expression):
    stack = []
    mapping = {')': '(', '}': '{', ']': '['}

    for char in expression:
        if char in mapping.values():
            stack.append(char)
        elif char in mapping.keys():
            if not stack or stack.pop() != mapping[char]:
                return False

    return not stack

#Sequences (remove_duplicates)
def remove_duplicates(sequence):
    seen = set()
    result = []

    for item in sequence:
        if item not in seen:
            seen.add(item)
            result.append(item)

    return result

#Dictionaries (word_frequency)
def word_frequency(sentence):
    import re
    word_count = {}
    words = re.findall(r'\b\w+\b', sentence.lower())

    for word in words:
        word_count[word] = word_count.get(word, 0) + 1

    return word_count








'''Stacks (is_balanced): The is_balanced function checks if a given expression containing parentheses, curly braces, and square brackets is balanced. It uses a stack to keep track of opening brackets and ensures that each opening bracket has a corresponding closing bracket in the correct order.

Sequences (remove_duplicates): The remove_duplicates function takes a sequence (list or tuple) and returns a new sequence with duplicates removed while maintaining the original order of elements. It uses a set to keep track of seen elements and builds a result list without duplicates.

Dictionaries (word_frequency): The word_frequency function takes a sentence and returns a dictionary containing the frequency of each word. It ignores punctuation, considers words in a case-insensitive manner, and uses a dictionary to store word frequencies.'''