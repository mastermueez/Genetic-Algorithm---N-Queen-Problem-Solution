import random
import string
from math import factorial
import time

class GeneticAlgorithm():

    chromosomeLength = 8
    populationSize = 100
    maxFitness = 28

    def __init__(self, chromosomeLength, populationSize):
        self.chromosomeLength = chromosomeLength
        self.populationSize = populationSize
        self.maxFitness = (factorial(self.chromosomeLength))/(factorial(2) * factorial(self.chromosomeLength-2))

    def getChromosome(self, chromosomeLength):
        #Returns a list of 'length' random numbers
        chromosome = []
        for n in range(chromosomeLength):
            randomNumberBetween1andLen = random.randint(1, self.chromosomeLength)
            chromosome.append(randomNumberBetween1andLen)
        return chromosome

    def getPopulation(self, chromosomeLength, populationSize):
        population = []
        for n in range(populationSize):
            chromosome = self.getChromosome(chromosomeLength)
            population.append(chromosome)
        return population

    def getFitnessVal(self, chromosome):
        chessBoard =  chromosome
        #HORIZONTAL ATTACKING PAIRS
        horizontalAttackingPairs = 0
        for queenPos in chessBoard:
            chessBoardWithoutCurrentQueen = chessBoard.copy()
            #Creating a new chessboard so that [n] and [n] are different values
            #Otherwise for every number, we would get a horizontal attacking pair even if there isn't any
            chessBoardWithoutCurrentQueen.remove(queenPos)
            for otherQueenPos in chessBoardWithoutCurrentQueen:
                if queenPos == otherQueenPos:
                    horizontalAttackingPairs += 1
        horizontalAttackingPairs /= 2 #To get rid of duplicates
        #Notice there are no vertical collisions

        diagonalAttackingPairList = []

        # D I A G O N A L
        #RIGHT DOWN
        rightDownDiagonalAttackingPair = 0
        for queenToBeAnalaysed_ColumnNumber in range(1, len(chessBoard)+1): #1-8
            diagonalAttackingPairFound = False
            InitialQueenRowNumber = chessBoard[queenToBeAnalaysed_ColumnNumber-1]
            InitialQueenColumnNumber = queenToBeAnalaysed_ColumnNumber
            #print("\nNEW queen initial state: ",InitialQueenRowNumber, InitialQueenColumnNumber)
            currentQueenRowNumber = InitialQueenRowNumber - 1
            currentQueenColumnNumber = InitialQueenColumnNumber + 1
            while currentQueenRowNumber > 0 and currentQueenColumnNumber <= self.chromosomeLength:
                #print("Current queen next state: ",currentQueenRowNumber, currentQueenColumnNumber)
                for otherQueenColumnNumber in range(currentQueenColumnNumber, len(chessBoard)+1):
                    otherQueenRowNumber = chessBoard[otherQueenColumnNumber-1]
                    #print("Other queen pos:", otherQueenRowNumber, otherQueenColumnNumber)
                    if currentQueenRowNumber == otherQueenRowNumber and currentQueenColumnNumber == otherQueenColumnNumber:
                        diagonalAttackingPairFound = True
                        rightDownDiagonalAttackingPair += 1
                        if InitialQueenRowNumber<otherQueenRowNumber:
                            pair = "("+str(InitialQueenRowNumber)+", "+str(InitialQueenColumnNumber)+"), ("+str(otherQueenRowNumber)+", "+str(otherQueenColumnNumber)+")"
                            diagonalAttackingPairList.append((pair))
                        else:
                            pair = "("+str(otherQueenRowNumber)+", "+str(otherQueenColumnNumber)+"), ("+str(InitialQueenRowNumber)+", "+str(InitialQueenColumnNumber)+")"
                            diagonalAttackingPairList.append((pair))
                        break
                currentQueenRowNumber -= 1
                currentQueenColumnNumber += 1
        queenToBeAnalaysed_ColumnNumber = 0

        #RIGHT UP
        rightUpDiagonalAttackingPair = 0
        for queenToBeAnalaysed_ColumnNumber in range(1, len(chessBoard)+1): #1-8
            diagonalAttackingPairFound = False
            InitialQueenRowNumber = chessBoard[queenToBeAnalaysed_ColumnNumber-1]
            InitialQueenColumnNumber = queenToBeAnalaysed_ColumnNumber
            currentQueenRowNumber = InitialQueenRowNumber + 1
            currentQueenColumnNumber = InitialQueenColumnNumber + 1
            while currentQueenRowNumber <= self.chromosomeLength and currentQueenColumnNumber <=self.chromosomeLength:
                for otherQueenColumnNumber in range(currentQueenColumnNumber, len(chessBoard)+1):
                    otherQueenRowNumber = chessBoard[otherQueenColumnNumber-1]
                    if currentQueenRowNumber == otherQueenRowNumber and currentQueenColumnNumber == otherQueenColumnNumber:
                        diagonalAttackingPairFound = True
                        rightUpDiagonalAttackingPair += 1
                        if InitialQueenRowNumber<otherQueenRowNumber:
                            pair = "("+str(InitialQueenRowNumber)+", "+str(InitialQueenColumnNumber)+"), ("+str(otherQueenRowNumber)+", "+str(otherQueenColumnNumber)+")"
                            diagonalAttackingPairList.append((pair))
                        else:               
                            pair = "("+str(otherQueenRowNumber)+", "+str(otherQueenColumnNumber)+"), ("+str(InitialQueenRowNumber)+", "+str(InitialQueenColumnNumber)+")"
                            diagonalAttackingPairList.append((pair))
                        break
                currentQueenRowNumber += 1
                currentQueenColumnNumber += 1
        queenToBeAnalaysed_ColumnNumber = 0

        #LEFT  DOWN
        leftDownDiagonalAttackingPair = 0
        for queenToBeAnalaysed_ColumnNumber in range(1, len(chessBoard)+1): #1-8
            diagonalAttackingPairFound = False
            InitialQueenRowNumber = chessBoard[queenToBeAnalaysed_ColumnNumber-1]
            InitialQueenColumnNumber = queenToBeAnalaysed_ColumnNumber
            currentQueenRowNumber = InitialQueenRowNumber - 1
            currentQueenColumnNumber = InitialQueenColumnNumber - 1
            while currentQueenRowNumber > 0 and currentQueenColumnNumber > 0:
                for otherQueenColumnNumber in range(currentQueenColumnNumber, len(chessBoard)+1):
                    otherQueenRowNumber = chessBoard[otherQueenColumnNumber-1]
                    if currentQueenRowNumber == otherQueenRowNumber and currentQueenColumnNumber == otherQueenColumnNumber:
                        diagonalAttackingPairFound = True
                        leftDownDiagonalAttackingPair += 1
                        if InitialQueenRowNumber<otherQueenRowNumber:
                            pair = "("+str(InitialQueenRowNumber)+", "+str(InitialQueenColumnNumber)+"), ("+str(otherQueenRowNumber)+", "+str(otherQueenColumnNumber)+")"
                            diagonalAttackingPairList.append((pair))
                        else:
                            pair = "("+str(otherQueenRowNumber)+", "+str(otherQueenColumnNumber)+"), ("+str(InitialQueenRowNumber)+", "+str(InitialQueenColumnNumber)+")"
                            diagonalAttackingPairList.append((pair))
                        break
                currentQueenRowNumber -= 1
                currentQueenColumnNumber -= 1

        #LEFT UP
        leftUpDiagonalAttackingPair = 0
        for queenToBeAnalaysed_ColumnNumber in range(1, len(chessBoard)+1): #1-8
            diagonalAttackingPairFound = False
            InitialQueenRowNumber = chessBoard[queenToBeAnalaysed_ColumnNumber-1]
            InitialQueenColumnNumber = queenToBeAnalaysed_ColumnNumber
            currentQueenRowNumber = InitialQueenRowNumber + 1
            currentQueenColumnNumber = InitialQueenColumnNumber - 1
            while currentQueenRowNumber <= self.chromosomeLength and currentQueenColumnNumber >0:
                for otherQueenColumnNumber in range(currentQueenColumnNumber, len(chessBoard)+1):
                    otherQueenRowNumber = chessBoard[otherQueenColumnNumber-1]
                    if currentQueenRowNumber == otherQueenRowNumber and currentQueenColumnNumber == otherQueenColumnNumber:
                        diagonalAttackingPairFound = True
                        leftUpDiagonalAttackingPair += 1
                        if InitialQueenRowNumber<otherQueenRowNumber:
                            pair = "("+str(InitialQueenRowNumber)+", "+str(InitialQueenColumnNumber)+"), ("+str(otherQueenRowNumber)+", "+str(otherQueenColumnNumber)+")"
                            diagonalAttackingPairList.append((pair))
                        else:
                            pair = "("+str(otherQueenRowNumber)+", "+str(otherQueenColumnNumber)+"), ("+str(InitialQueenRowNumber)+", "+str(InitialQueenColumnNumber)+")"
                            diagonalAttackingPairList.append((pair))
                        break
                currentQueenRowNumber += 1
                currentQueenColumnNumber -= 1

        diagonalAttackingPairList = list(set(diagonalAttackingPairList))
        diagonalAttackingPairCount = len(diagonalAttackingPairList)
        totalAttackingPairs =diagonalAttackingPairCount + horizontalAttackingPairs
        fitnessVal = self.maxFitness-totalAttackingPairs
        return fitnessVal

    def getFitnessProbability(self, chromosome):
        return self.getFitnessVal(chromosome)/self.maxFitness

    def getRandomChromosome(self, population, probabilities):
        populationWithProbabilty = zip(population, probabilities)
        probSum = 0
        for chromosome, prob in populationWithProbabilty:
            probSum += prob
        r = random.uniform(0, probSum)
        upto = 0
        for chromosome, prob in zip(population, probabilities):
            if upto + prob >= r:
                return chromosome
            upto += prob
        assert False, "Shouldn't get here"
            
    def performCrossOver(self, x, y):
        n = len(x)
        partitionPoint = random.randint(0, n - 1) #any number between 1 and 8
        #print(partitionPoint)
        partition1 = x[0:partitionPoint]
        partition2 = y[partitionPoint:n]
        child = partition1 + partition2
        #print(child)
        return child

    def mutate(self, x):
        n = len(x)
        genePosToBeMutated = random.randint(0, n - 1) #n-1 because list starts from 0, don't want an index error
        mutationVal = random.randint(1, n)
        x[genePosToBeMutated] = mutationVal
        #print(x)
        return x

    def getGeneticPopulation(self, population):
        mutation_probability = 0.03
        new_population = []
        probabilities = []
        for chromosome in population:
            probabilities.append(self.getFitnessProbability(chromosome))
        #Creat new population from old population
        for i in range(len(population)):
            #Pick two chromosomes
            x = self.getRandomChromosome(population, probabilities)
            y = self.getRandomChromosome(population, probabilities)
            #Create new chromosome by combining the previous two
            child = self.performCrossOver(x, y)
            #Mutate (or don't do anything at all) a gene from that new chromosome randomly
            if random.random() < mutation_probability: #random.random() = +ve FP < 0
                child = self.mutate(child)
            new_population.append(child)
            if self.getFitnessVal(child) == self.maxFitness: break
        return new_population

    def getChromosomeWithMaxFitness(self):
        population = self.getPopulation(self.chromosomeLength, self.populationSize)
        generation = 1
        startTime = time.time()
        fitnessVal = 0
        generationCount = 1
        solutionFound = False
        while fitnessVal != self.maxFitness:
            for chromosome in population:
                fitnessVal = self.getFitnessVal(chromosome)
                print("Generation: %d | Chromosome: %s | Fitness: %d"%(generationCount,str(chromosome),fitnessVal ))
                if fitnessVal == self.maxFitness:
                    solutionFound = True
                    print("\nSolution found at generation: %d for chromosome %s"%(generationCount,str(chromosome)))
                    print("Time taken: %0.2fs" %(time.time()-startTime))
                    break
            if solutionFound:
                break
            population = self.getGeneticPopulation(population)
            generationCount += 1

if __name__ == "__main__":
    chromosomeLength = 5
    populationSize = 100
    geneticAlgoObj = GeneticAlgorithm(chromosomeLength, populationSize)
    geneticAlgoObj.getChromosomeWithMaxFitness()
    #print(geneticAlgoObj.fitness([6, 3, 5, 7, 1, 4, 2, 8])) #to print fitness val of any chromosome