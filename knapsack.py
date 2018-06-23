import numpy as np
import operator

class Knapsack:
    def __init__(self, totalWeight, weights, values, itemIndexes):
        self.totalWeight = totalWeight
        indexes = np.array(weights) <= totalWeight
        self.weights = np.array(weights)[indexes]
        self.values = np.array(values)[indexes]
        self.itemIndexes = np.array(itemIndexes)[indexes]
        self.matrix = np.zeros((len(self.weights) + 1, totalWeight + 1)).astype(int)
        self.dictionary = {}
        self.items = {}
        for i in range(totalWeight + 1):
            self.items[(0,i)] = []
        for i in range(len(self.weights) + 1):
            self.items[(i, 0)] = []



    def getMatrix(self):
        return self.matrix

#1,0,1,0,1,0,1,1,1,0,0,0,0,1,1


    def run(self):
        #return self.knapsackRecursive(len(self.weights), self.totalWeight)
        #return self.knapsackRecursiveDictionary(len(self.weights), self.totalWeight)
        return self.knapsackIterative()




    def knapsackIterative(self):
        a, b = self.matrix.shape
        for i in range(1, a):
            for j in range(1, b):
                if j < self.weights[i-1]:
                    self.matrix[i, j] = self.matrix[i-1, j]
                    self.items[(i, j)] = self.items[(i-1), j]
                else:
                    maxIndex, self.matrix[i, j] = max(enumerate([self.matrix[i-1, j], self.matrix[i-1, j-self.weights[i-1]] + self.values[i-1]]), key=operator.itemgetter(1))
                    if maxIndex == 0:
                        self.items[(i, j)] = self.items[(i-1, j)]
                    else:
                        self.items[(i,j)] = self.items[(i-1, j-self.weights[i-1])] + [i]
        
        return self.matrix[a-1, b-1]



    
    def knapsackRecursive(self, i, j):
        if i * j != 0:
            if j < self.weights[i-1]:
                if self.matrix[i, j] == 0:
                    self.matrix[i, j] = self.knapsackRecursive(i-1, j)
                self.items[(i, j)] = self.items[(i-1), j]
            else:
                a, b = 0, 0
                if self.matrix[i-1,j] == 0:
                    a = self.knapsackRecursive(i-1, j)
                else:
                    a = self.matrix[i-1, j]

                if self.matrix[i-1, j-self.weights[i-1]] == 0:
                    b = self.knapsackRecursive(i-1, j-self.weights[i-1]) + self.values[i-1]
                else:
                    b = self.matrix[i-1, j-self.weights[i-1]]

                maxIndex, self.matrix[i, j] = max(enumerate([a, b]), key=operator.itemgetter(1))
                if maxIndex == 0:
                    self.items[(i, j)] = self.items[(i-1, j)]
                else:
                    self.items[(i,j)] = self.items[(i-1, j-self.weights[i-1])] + [i]

        return self.matrix[i, j]


    def knapsackRecursiveDictionary(self, i, j):
        if i * j != 0:
            if j < self.weights[i-1]:
                if (i, j) not in self.dictionary:
                    self.dictionary[(i, j)] = self.knapsackRecursiveDictionary(i-1, j)
                self.items[(i, j)] = self.items[(i-1), j]
            else:
                a, b = 0, 0
                if (i-1, j) not in self.dictionary:
                    a = self.knapsackRecursiveDictionary(i-1, j)
                else:
                    a = self.dictionary[(i-1, j)]

                if (i-1, j-self.weights[i-1]) not in self.dictionary:
                    b = self.knapsackRecursiveDictionary(i-1, j-self.weights[i-1]) + self.values[i-1]
                else:
                    b = self.dictionary[(i-1, j-self.weights[i-1])]

                maxIndex, self.dictionary[(i, j)] = max(enumerate([a, b]), key=operator.itemgetter(1))
                if maxIndex == 0:
                    self.items[(i, j)] = self.items[(i-1, j)]
                else:
                    self.items[(i,j)] = self.items[(i-1, j-self.weights[i-1])] + [i]

            return self.dictionary[(i, j)]
        else:
            return 0


    def showItems(self):
        indexes =  self.items[(len(self.weights), self.totalWeight)]
        #return [(self.weights[x-1], self.values[x-1]) for x in indexes]
        return [self.itemIndexes[x-1]  for x in indexes]
