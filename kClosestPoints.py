
def kClosest(points, k):
    if len(points) == k:
        return points
    for point in points:
        distance = ((point[0]**2) + (point[1]**2)) ** 0.5
        point.append(distance)
    #how to sort a list of lists based on the third element
    #itemgetter could also work - https://stackoverflow.com/questions/4174941/how-to-sort-a-list-of-lists-by-a-specific-index-of-the-inner-list
    points.sort(key=lambda x:x[2])
    return [points[x][0:2] for x in range(k)]


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
print(kClosest(points,k))

points, k = [[3,3],[5,-1],[-2,4]], 2
print(kClosest(points,k))

points, k = [[0,1],[1,0]], 2
print(kClosest(points,k))

points,k = [[1,3],[-2,2],[2,-2]], 2
print(kClosest(points,k))