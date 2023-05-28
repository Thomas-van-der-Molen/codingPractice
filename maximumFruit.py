def totalFruit(fruits, window, minLL):
    if len(set(fruits)) <= 2: return len(fruits)
    for x in range(len(fruits) - window + 1):
        if len(set(fruits[x : x + window])) <= minLL[0]: minLL = (len(set(fruits[x : x+window])), fruits[x : x + window])
    totalFruit(minLL[1], minLL[0], minLL) 

def totalFruitThree(fruits):
    window = len(fruits) - 1
    while window > 1:
        if len(set(fruits)) <= 2: return len(fruits)
        window = len(fruits) - 1
        left = fruits[0 : window]
        right = fruits[1 : 1 + window]
        if len(set(left)) <= len(set(right)): fruits = left
        else: fruits = right
    return 1

def totalFruitTwo(fruits):
        check = set(fruits)
        if len(check) <= 2: return len(fruits)
        window = len(fruits)
        mini = (window, 0)
        while window > 1:
            for x in range(len(fruits) - window + 1):
                if len(set(fruits[x : x + window])) <= 2: return window 
                mini = min(mini, (len(set(fruits[x : x + window])), x))
            window -= 1
        return 1

fruits = [1,2,1]
window, minLL = len(fruits), (len(set(fruits)), fruits)
print(totalFruit(fruits, window, minLL))

fruits = [0,1,2,2]
window, minLL = len(fruits), (len(set(fruits)), fruits)
print(totalFruit(fruits, window, minLL))

fruits = [1,2,3,2,2]
window, minLL = len(fruits), (len(set(fruits)), fruits)
print(totalFruit(fruits, window, minLL))

fruits = [1,2,1,2,1,2,1,2,1,2,1,2,1,2,1]
window, minLL = len(fruits), (len(set(fruits)), fruits)
print(totalFruit(fruits, window, minLL))

fruits = [1,2,1,2,1,2,1,2,3]
window, minLL = len(fruits), (len(set(fruits)), fruits)
print(totalFruit(fruits, window, minLL))

fruits = [1,1,1]
window, minLL = len(fruits), (len(set(fruits)), fruits)
print(totalFruit(fruits, window, minLL))

fruits = [0,1,2,3,4,4,4,4,4,5,5,5,5]
window, minLL = len(fruits), (len(set(fruits)), fruits)
print(totalFruit(fruits, window, minLL))
