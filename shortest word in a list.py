def find_short(s):
    new = s.split()
    return len(min(new, key = len))
s = input("Enter a String")
find_short(s)
