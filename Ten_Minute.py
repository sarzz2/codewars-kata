#You live in the city of Cartesia where all roads are laid out in a perfect grid.
#You arrived ten minutes too early to an appointment, so you decided to take the opportunity to go for a short walk.
#The city provides its citizens with a Walk Generating App on their phones -- everytime you press the button it sends you an
#array of one-letter strings representing directions to walk (eg. ['n', 's', 'w', 'e']). You always walk only a single block 
#in a direction and you know it takes you one minute to traverse one city block,
#so create a function that will return true if the walk the app gives you will take you exactly ten minutes 
#(you don't want to be early or late!) and will, of course, return you to your starting point. Return false otherwise.


    time = 0
    distance_vertical = 0     # To measure north and south distance
    distance_horizontal = 0   # To measure east and west distance
    for i in range(0, len(arr)):
        if arr[i] == 'n':
            time += 1
            distance_vertical += 1
            i += 1
        elif arr[i] == 's':
            time += 1
            distance_vertical -= 1
            i += 1
        elif arr[i] == 'w':
            time += 1
            distance_horizontal += 1
            i += 1
        elif arr[i] == 'e':
            time += 1
            distance_horizontal -= 1
            i += 1
    if time == 10 and distance_vertical == 0 and distance_horizontal == 0:
        return True
    else:
        return False
