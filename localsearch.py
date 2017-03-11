__author__ = 'Michael Tang'

import math
import random
import sys

def hillclimb(function, parameters):
    var = []
    jump = 1
    lowest = sys.maxsize
    stopcounter = 0
    stop = 1000 * parameters
    for i in range(0,parameters):
        var.append(0)

    currentvalue = function(var)
    if lowest > currentvalue:
        lowest = currentvalue
        stopcounter = 0
    else:
        stopcounter += 1

    while stopcounter != stop:
        # choose random change
        choose = random.randrange(0, parameters)
        save = var[choose]
        if random.randrange(0,2) == 0:
            var[choose] += jump
        else:
            var[choose] -= jump

        currentvalue = function(var)
        if lowest > currentvalue:
            lowest = currentvalue
            stopcounter = 0
        else:
            stopcounter += 1
            var[choose] = save

    print("Found local min at:")
    for i in range(0, len(var)):
        print("var[", i, "]: ", var[i])
    print("With a min of: {0:.15f}".format(lowest))


def anneal(function, parameters):
    var = []
    for i in range(0,parameters):
        var.append(0)
    lowest = sys.maxsize
    jump = 1
    temp = 10000 * parameters
    cool = .001

    currentvalue = function(var)
    if lowest > currentvalue:
        lowest = currentvalue

    while temp > 0.000001:

        # choose random change
        choose = random.randrange(0, parameters)
        save = var[choose]
        if random.randrange(0, 2) == 0:
            var[choose] += jump
        else:
            var[choose] -= jump

        currentvalue = function(var)
        if lowest > currentvalue:
            lowest = currentvalue
        elif math.exp((lowest - currentvalue) / temp) > random.random():
            lowest = currentvalue
        else:
            var[choose] = save

        # cooling
        temp *= 1 - cool



    print("Found local min at:")
    for i in range(0, len(var)):
        print("var[", i, "]: ", var[i])
    print("With a min of: {0:.15f}".format(lowest))


def genetic(function, parameters):
    var = []
    popvars = []
    popsize = 200
    for i in range(0, popsize):
        for j in range(0, parameters):
            var.append(random.randrange(0, 100))
        popvars.append(var)
        var = []
    popsolutions = []
    for i in range(0, popsize):
        popsolutions.append(function(popvars[i]))
    totallowest = min(popsolutions)
    popvarsnew = []
    generations = 2000

    for i in range(0, generations):
        weighted_solutions = []
        for solution in popsolutions:
            fitnessval = fitness(solution, totallowest)

            if fitnessval == 0:
                weighted = (solution, 1.0)
            else:
                weighted = (solution, 1.0 / fitnessval)
            weighted_solutions.append(weighted)

        for j in range(0, int(popsize/2)):
            sol1 = choose_solution(weighted_solutions)
            sol2 = choose_solution(weighted_solutions)

            sol1, sol2 = crossover(popvars[sol1], popvars[sol2], parameters)

            popvarsnew.append(mutate(sol1))
            popvarsnew.append(mutate(sol2))

        popvars = popvarsnew
        popvarsnew = []
        popsolutions = []
        for j in range(0, popsize):
            popsolutions.append(function(popvars[j]))
        totallowest = min(popsolutions)

    lowest = sys.maxsize
    lowestvar = 0
    for i in range(0, popsize):
        if lowest > popsolutions[i]:
            lowest = popsolutions[i]
            lowestvar = popvars[i]
    print("Found local min at:")
    for i in range(0, len(lowestvar)):
        print("var[", i, "]: ", lowestvar[i])
    print("With a min of: {0:.15f}".format(lowest))

# returns index of a solution
def choose_solution(solutions):
    weighttotal = sum((solution[1] for solution in solutions))
    n = random.uniform(0, weighttotal)
    for i in range(0, len(solutions)):
        weight = (solutions[i])[1]
        if n < weight:
            return i
        n = n - weight
    return 0

def fitness(solution, totallowest):
    return solution - totallowest

def mutate(var):
    mutationchance = .01
    for i in range(0, len(var)):
        if random.random() < mutationchance:
            var[i] = random.randrange(0, 100)
    return var

def crossover(var1, var2, parameters):
    child1 = []
    child2 = []
    pos = random.randrange(0, parameters)
    for i in range(0, parameters):
        if i >= pos:
            child1.append(var2[i])
            child2.append(var1[i])
        else:
            child1.append(var1[i])
            child2.append(var2[i])

    return child1, child2


def easy(var):
    x = var[0]
    y = var[1]
    z = var[2]
    k = var[3]
    return ((x-10)**2 + (y+8)**2 + z**2 + k**2)


def medium(var):
    x = var[0] + 100
    y = var[1] + 100
    r = x**2 + y**2
    firstPart = (math.sin(x**2+(3 * y**2))/ (.1 + r))
    secondPart = (x**2 + 5 * (y**2)) * (( math.e ** (1-r))/2)
    return -(firstPart + secondPart)


def hard(var):
    a = int(var[0])
    b = int(var[1])
    c = int(var[2])
    d = int(var[3])
    e = int(var[4])
    f = int(var[5])
    g = int(var[6])
    h = int(var[7])
    i = int(var[8])
    j = int(var[9])
    penalty = 0
    if(a < 1 or a > 3):
        penalty += abs(a-1) * 100
    if(b < 1 or b > 3):
        penalty += abs(b-1) * 100
    if(c < 1 or c > 3):
        penalty += abs(c-1) * 100
    if(d < 1 or d > 3):
        penalty += abs(d-1) * 100
    if(e < 1 or e > 3):
        penalty += abs(e-1) * 100
    if(f < 1 or f > 3):
        penalty += abs(f-1) * 100
    if(g < 1 or g > 3):
        penalty += abs(g-1) * 100
    if(h < 1 or h > 3):
        penalty += abs(h-1) * 100
    if(j < 1 or j > 3):
        penalty += abs(j-1) * 100
    if(i < 1 or i > 3):
        penalty += abs(i-1) * 100

    if(a == b):
        penalty += 1
    if(a == c):
        penalty += 1
    if(c == d):
        penalty += 1
    if(b == c):
        penalty += 1
    if(d == e):
        penalty += 1
    if(d == f):
        penalty += 1
    if(f == g):
        penalty += 1
    if(e == g):
        penalty += 1
    if(g == h):
        penalty += 1
    if(h == i):
        penalty += 1
    if(h == j):
        penalty += 1
    if(i == j):
        penalty += 1

    return penalty


def main():
    func = eval(sys.argv[1])
    hillclimb(func, int(sys.argv[2]))
    anneal(func, int(sys.argv[2]))
    genetic(func, int(sys.argv[2]))

main()
