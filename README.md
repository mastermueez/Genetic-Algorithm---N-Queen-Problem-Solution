## Description
The n queen problem requires one to find possible arrangements of n queens in an n x n chessboard such that no queens are in attacking pairs. The code here finds such an arrangement when executed. This [video](https://www.youtube.com/watch?v=qt85_CinKwo) explains the problem well.

## Terminology
* Chromosome: a valid arrangement of n queens on an n x n chessboard
* Gene: any one position in the chessboard
* Population: a bunch of chromosomes
* Fitness value: number of non attacking pairs

## Samples
The following contains a few possible arrangements of 8 queens in an 8 x 8 standard chessboard where there are no queens in an attacking configuration:
* [6, 1, 5, 2, 8, 3, 7, 4]
* [5, 2, 6, 1, 7, 4, 8, 3]
* [4, 2, 7, 3, 6, 8, 1, 5]
* [4, 6, 8, 2, 7, 1, 3, 5]
* [5, 8, 4, 1, 3, 6, 2, 7]
* [5, 7, 1, 3, 8, 6, 4, 2]
* [4, 2, 7, 5, 1, 8, 6, 3]
* [7, 5, 3, 1, 6, 8, 2, 4]
* [5, 2, 4, 7, 3, 8, 6, 1]
* [6, 3, 5, 7, 1, 4, 2, 8]

## Code
The variable **chromosomeLength** in the main method determines the dimensions of the chessboard. If the value is 8, the code tries to find an arrangement of 8 queens such that there are 28 non attacking pairs in an 8 x 8 standard chessboard. Change it as you please.

Running getFitnessVal(chromosome) directly on an object of the class will return the number of non-attacking pairs. But note that the **chromosomeLength** variable used to initialize the class will also have to be changed accordingly.

## Personal Thought
Yes, the getFitnessVal() function looks really messy at the moment, but I'll try to remove all the redundant code once I have abundant time.
