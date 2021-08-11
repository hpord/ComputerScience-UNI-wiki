import random

def randomSolution(tsp):
    cities = list(range(len(tsp)))
    solution=[]
    for i in range(len(tsp)):
        randonCity = cities[random.randint(0,len(cities)-1)]
        solution.append(randonCity)
        cities.remove(randonCity)
    #print(solution)
    return solution

def routeLength(tsp,solution):
    routeLength=0
    for i in range(len(solution)):
        #print(tsp[solution[i-1]][solution[i]])
        routeLength += tsp[solution[i-1]][solution[i]]
    #print(routeLength)
    return routeLength

def getNeighbours(solution):
    neighbours=[]
    for i in range(len(solution)):
        for j in range(i+1,len(solution)):
            neighbour = solution.copy()
            neighbour[i]=solution[j]
            neighbour[j]=solution[i]
            neighbours.append(neighbour)
    #print(neighbours)
    return neighbours

def getBestNeighbour(tsp,neighbours):
    bestRouteLength = routeLength(tsp,neighbours[0])
    bestNeighbour = neighbours[0]
    for neighbour in neighbours:
        currentRouteLength = routeLength(tsp,neighbour)
        if currentRouteLength < bestRouteLength:
            bestRouteLength = currentRouteLength
            bestNeighbour = neighbour
    #print(bestNeighbour)
    #print(bestRouteLength)
    return bestNeighbour,bestRouteLength

def hillClimbing(tsp):
    currentSolution= randomSolution(tsp)
    currentRouteLength=routeLength(tsp,currentSolution)
    neighbours = getNeighbours(currentSolution)
    bestNeighbour, bestNeighbourRouteLength = getBestNeighbour(tsp,neighbours)

    while bestNeighbourRouteLength < currentRouteLength:
        currentSolution = bestNeighbour
        currentRouteLength = bestNeighbourRouteLength
        neighbours = getNeighbours(currentSolution)
        bestNeighbour,bestNeighbourRouteLength=getBestNeighbour(tsp,neighbours)
    
    #print (currentSolution)
    #print(currentRouteLength)
    return currentSolution,currentRouteLength

def problemGenerator(nCities):
    tsp = []
    for i in range(nCities):
        distances = []
        for j in range(nCities):
            if j == i:
                distances.append(0)
            elif j < i:
                distances.append(tsp[j][i])
            else:
                distances.append(random.randint(10, 1000))
        tsp.append(distances)
    return tsp

tsp = [
        [0, 400, 500, 300],
        [400, 0, 300, 500],
        [500, 300, 0, 400],
        [300, 500, 400, 0]
    ]

def main():
    tsp = problemGenerator(15)
    for i in range(10):
        print(hillClimbing(tsp))


main()