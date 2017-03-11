__author__ = 'Michael Tang'
import sys

class DecisionTree:

    def __init__(self):
        self.parameters = 0


    def train(self, trainset):
        self.parameters = len(trainset[0])
        print(self.parameters)


def main():

    setlist = []
    with open(sys.argv[1]) as f:
        for line in f:
            split = line.split(" ")
            for i in range(0,len(split)):
                split[i] = int(split[i])
            setlist.append(split)

    tree = DecisionTree()
    tree.train(setlist)




main()
