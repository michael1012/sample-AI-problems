__author__ = 'Michael Tang'
import queue
import sys

# searches a graph using an edgelist for paths


def backtrace(parent, start, goal):
    path = []
    path.append(goal)
    while path[-1] != start:
        path.append(parent[path[-1]])
    path.reverse()
    return path


def breadth(inputfile, start, goal):
    edgelist = []
    with open(inputfile) as f:
        for line in f:
            edgelist.append(line)
    frontier = []
    found = []
    parent = {}
    children = []
    frontier.append(start)
    found.append(start)
    while frontier:
        node = frontier.pop(0)
        if node == goal:
            return backtrace(parent, start, goal)
        for edge in edgelist:
            first, second, dist = edge.split(" ")
            if node == first and found.count(second) == 0:
                frontier.append(second)
                found.append(second)
                children.append(second)
        for child in children:
            parent[child] = node
        children = []


def depth(inputfile, start, goal):
    edgelist = []
    with open(inputfile) as f:
        for line in f:
            edgelist.append(line)
    frontier = []
    found = []
    parent = {}
    children = []
    frontier.append(start)
    found.append(start)
    while frontier:
        node = frontier.pop()
        found.append(node)
        if node == goal:
            return backtrace(parent, start, goal)
        for edge in edgelist:
            first, second, dist = edge.split(" ")
            if node == first and found.count(second) == 0:
                frontier.append(second)
                children.append(second)
        for child in children:
            parent[child] = node
        children = []


class Node:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def __lt__(self, other):
        return self.weight < other.weight


def uniform(inputfile, start, goal):
    edgelist = []
    with open(inputfile) as f:
        for line in f:
            edgelist.append(line)
    frontier = queue.PriorityQueue()
    frontieritems = []
    explored = []
    parent = {}
    children = []
    frontier.put(Node(start, 0))
    while frontier:
        node = frontier.get()
        if node.name == goal:
            return backtrace(parent, start, goal)
        explored.append(node.name)
        for edge in edgelist:
            first, second, weight = edge.split(" ")
            if node.name == first:
                if explored.count(second) == 0:
                    if frontieritems.count(second) == 0:
                        frontier.put(Node(second, weight))
                        frontieritems.append(second)
                        children.append(second)
        for child in children:
            parent[child] = node.name
        children = []


def main():
    path = []
    if sys.argv[2] == "Breadth":
        path = breadth(sys.argv[1],sys.argv[3],sys.argv[4])
    if sys.argv[2] == "Depth":
        path = depth(sys.argv[1],sys.argv[3],sys.argv[4])
    if sys.argv[2] == "Uniform":
        path = uniform(sys.argv[1],sys.argv[3],sys.argv[4])

    f = open(sys.argv[5], "w")
    for node in path:
        f.write(node + "\n")
    f.close()


main()