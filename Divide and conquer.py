#Given a mixed array of number and string representations of integers, add up the string integers 
#and subtract this from the total of the non-string integers.


def sum_mix(arr):
    ans = 0
    res = 0
    for i in arr:
        if isinstance(i, int):
            ans = ans + i
        elif isinstance(i, str):
            res = res + int(i)
    final = ans - res
    print(final)
summ_mix(9,3,'7','3')


#The above input will return the answer as 2 (9+3) -(7+3) = 2 
#since 9 and 3 are integers i.e. not enclosed in " " and 7 and 3 are string since enclosed in " "
