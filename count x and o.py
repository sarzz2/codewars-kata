#Check to see if a string has the same amount of 'x's and 'o's. The method must return a boolean and be case insensitive.
#The string can contain any char.


def xo(str):
    str = str.lower()
    count1 =str.count("x")
    count2 = str.count("o") 
    if count1 == count2:
        return True
    else:
        return False
str = input("Enter the string:")
xo(n)  
