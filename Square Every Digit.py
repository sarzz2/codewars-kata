# square every digit of a number.
# example, if we run 9119 through the function, 811181 will come out, because 92 is 81 and 12 is 1.


def square(num):
    num = str(num)
    c = []
    for i in range(0,len(num)):
        b = int(num[i]) * int(num[i])
        c.append(b)
    res = int("".join(map(str, c)))
    print(res)
