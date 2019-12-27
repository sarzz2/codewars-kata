# Given a Divisor and a Bound , Find the largest integer N , Such That ,
# N is divisible by divisor
# N is less than or equal to bound
# N is greater than 0.
# Example maxMultiple (2,7) ==> return (6)



def max_multiple(divisor, bound):
    if bound % divisor == 0:
        print(bound)
    else:
        for i in range(1, bound):
            ans = divisor*i
            i += 1
            if ans >= bound:
                break
            res = ans
        print(res)
