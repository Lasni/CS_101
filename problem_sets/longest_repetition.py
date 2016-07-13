# Question 8: Longest Repetition

# Define a procedure, longest_repetition, that takes as input a
# list, and returns the element in the list that has the most
# consecutive repetitions. If there are multiple elements that
# have the same number of longest repetitions, the result should
# be the one that appears first. If the input list is empty,
# it should return None.


def longest_repetition(lst):
    current_el = None
    current_len = 0
    best_el = None
    best_len = 0
    for i in lst:
        if i != current_el:
            current_el = i
            current_len = 1
        elif i == current_el:
            current_len += 1
        if current_len > best_len:
            best_el = current_el
            best_len = current_len
    return best_el


# For example,

print longest_repetition([1, 2, 2, 3, 3, 3, 2, 2, 1])
# 3

print longest_repetition(['a', 'b', 'b', 'b', 'c', 'd', 'd', 'd'])
# b

print longest_repetition([1, 2, 3, 4, 5])
# 1

print longest_repetition([])
# None
