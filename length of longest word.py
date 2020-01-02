#Output should be the length of the longest word, as a number.


def find_longest(string):
    n = len(string)
    res = 0
    curr_len = 0

    for i in range(0, n):
        if string[i] != ' ':
            curr_len += 1
        else:
            res = max(res, curr_len)
            curr_len = 0
    print(max(res, curr_len))


find_longest("The quick white fox jumped around the massive dog")     # answer is 7
