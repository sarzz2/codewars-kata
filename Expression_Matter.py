#Given three integers a ,b ,c, return the largest number obtained after inserting the following operators and brackets: +, *, ().

#With the numbers are 1, 2 and 3 , here are some ways of placing signs and brackets:
#1 * (2 + 3) = 5
#1 * 2 * 3 = 6
#1 + 2 * 3 = 7
#(1 + 2) * 3 = 9
#So the maximum value that you can obtain is 9.


def expression_matter(a,b,c):
    # All the possible Combinations
    ans1 = a*(b+c)
    ans2 = a*b*c
    ans3 = a+b*c
    ans4 = (a+b)*c
    ans5 = a+b+c
    large = ans1
    # Comparing the largest
    if ans2 > large:
        large = ans2
    if ans3 > large:
        large = ans3
    if ans4 > large:
        large = ans4
    if ans5 > large:
        large = ans5
    print(large)
