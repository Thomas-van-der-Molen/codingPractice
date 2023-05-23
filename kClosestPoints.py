
def kClosestThree(points, k):
    if len(points) == k:
        return points
    for point in points:
        distance = ((point[0]**2) + (point[1]**2)) ** 0.5
        point.append(distance)
    #how to sort a list of lists based on the third element
    #itemgetter could also work - https://stackoverflow.com/questions/4174941/how-to-sort-a-list-of-lists-by-a-specific-index-of-the-inner-list
    points.sort(key=lambda x:x[2])
    return [points[x][0:2] for x in range(k)]


#do the same problem but use a min heap
import heapq
def kClosest(points, k):
    if len(points) == k:
        return points
    myHeap = []
    ret = []
    x = 0
    for point in points:
        distance = ((point[0] ** 2) + (point[1] ** 2)) ** 0.5
        newPoint = [distance, x]
        heapq.heappush(myHeap, newPoint)
        x+=1
    for x in range(k):
        ret.append(heapq.heappop(myHeap))
    return [points[point[1]] for point in ret]

#improve the min heap solution using the max heap solution for inspiration
def kClosestFive(points, k):
    if len(points) == k:
        return points
    heap = []
    for (x,y) in points:
        dist = ((x**2) + (y**2)) **0.5
        heapq.heappush(heap, (dist, x, y))
    return [list(heapq.heappop(heap)[1:]) for x in range(k)]


#this is the max heap solution,
#basically add all the distances to the heap, but only keep the k smallest distances in the heap
#then just return the whole heap
#how do you specify between a minheap and maxheap in python?
#there is no way to make a "max heap" with heapq
#Heapq is always a min heap
#Therefore, if you want a max heap, you must negate the values in the heap
#This will function like a max heap
def kClosestFour(points, k):
    if len(points) == k:
        return points
    heap = []

    for (x,y) in points:
          
        dist = ((x**2) + (y**2)) ** 0.5
        dist = -dist

        if len(heap) == k:
            heapq.heappushpop(heap, (dist, x, y))
        else:
            heapq.heappush(heap, (dist, x, y))
    
    return [(x,y) for (dist, x, y) in heap]
    

#does not work, my initial approach
#A dictionary/hash table could not be used because the distances are not necessarily unique
#And it would not make sense to use the points as the dictionary keys
def kClosestTwo(points , k):
        if len(points) == k:
            return points
        distances = {}
        for point in points:
            distance = ((point[0]**2) + (point[1]**2)) ** 0.5
            distances[distance] = point
        distList = list(distances.keys())
        distList.sort()
        points = []
        for x in range(k):
            points.append(distances[distList[x]])
        return points



points, k = [[1,3],[-2,2]], 1
print(f' result 1 {kClosest(points,k)} ')

points, k = [[3,3],[5,-1],[-2,4]], 2
print(f' result 2 {kClosest(points,k)} ')

points, k = [[0,1],[1,0]], 2
print(f' result 3 {kClosest(points,k)} ')

points,k = [[1,3],[-2,2],[2,-2]], 2
print(f' result 4 {kClosest(points,k)} ')



points, k = [[1,3],[-2,2]], 1
print(f' result 1 {kClosestFive(points,k)} ')

points, k = [[3,3],[5,-1],[-2,4]], 2
print(f' result 2 {kClosestFive(points,k)} ')

points, k = [[0,1],[1,0]], 2
print(f' result 3 {kClosestFive(points,k)} ')

points,k = [[1,3],[-2,2],[2,-2]], 2
print(f' result 4 {kClosestFive(points,k)} ')