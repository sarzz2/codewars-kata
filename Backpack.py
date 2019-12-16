#You're about to go on a trip around the world! On this trip you're bringing your trusted backpack, that anything fits into. 
#The bad news is that the airline has informed you, that your luggage cannot exceed a certain amount of weight.
To make sure you're bringing your most valuable items on this journey you've decided to give all your items a score that 
#represents how valuable this item is to you. It's your job to pack you bag so that you get the most value out of the items 
#that you decide to bring.

#Your input will consist of two arrays, one for the scores and one for the weights. You input will always be valid lists of 
#equal length, so you don't have to worry about verifying your input.

#You'll also be given a maximum weight. This is the weight that your backpack cannot exceed.

#For instance, given these inputs:

#scores = [15, 10, 9, 5]
#weights = [1, 5, 3, 4]
#capacity = 8
#The maximum score will be 29. This number comes from bringing items 1, 3 and 4.


def pack_bagpack(scores, weights, capacity):
    used = []
    weight = 0
    value = 0
    ratios = [scores[x]/weights[x] for x in range(0, len(scores))]
    print(ratios)
    while weight < capacity:
        try:
            ratio = max(ratios)
            index = ratios.index(ratio)
            if ratio in used:
                ratios.pop(index)
                scores.pop(index)
                weights.pop(index)
                ratio = max(ratios)
                index = ratios.index(ratio)
            used.append(ratio)
            if not weight + weights[index] > capacity:
                value += scores[index]
                weight += weights[index]
        except ValueError:
            break
    print(value)
pack_bagpack([19,8,6,20,3,16], [8,2,3,10,1,5], 2)
