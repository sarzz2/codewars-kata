def sum_mix(arr):
    print(arr)
    ans = 0
    for i in range(0, len(arr)):
        arr[i] = int(arr[i])         # changing all elements in a list to an integer
        ans = ans + arr[i]
    return ans
sum_mix([1,"1","2"])                 # passing numbers in the function 
