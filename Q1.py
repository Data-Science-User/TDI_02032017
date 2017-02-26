## Q1:
## We repeatedly toss a biased coin with probability 0.6 of landing on Heads (H)
## and probability 0.4 of landing on Tails (T). Within this sequence of heads and tails,
## a group is a maximal sequence of consecutive tosses that land on the same side.
## For instance, the groups of HTTTHTHTT are (H)(TTT)(H)(T)(H)(TT)

## For each of these problems, please give the answer to 10 digits of significance.
import random
from itertools import groupby
from itertools import chain
import scipy.stats as st
import statistics

# Function for biased coin
def flip(p):
    return 'H' if random.random() < p else 'T'

# Number of coin flips
N = 10
flips = [flip(0.6) for i in range(N)]
print (len(list(groupby(flips))))

# Function to simulate X iterations of N coin flips
def simulate(X, N):
    Outcome = []
    for i in range(X):
        flips = [flip(0.6) for j in range(N)]
        Outcome.append(len(list(groupby(flips))))
    print(sum(Outcome)/(X))

## (1) What is the expected number of groups after 10 tosses?
simulate(1000000,10)
# We expect 5.31985092 groups after 10 tosses.

## (2) What is the expected number of groups after 500 tosses?
simulate(1000000,500)
# We expect 240.51896439 groups after 500 tosses.

## (3) What is the probability of (strictly) exceeding 6 groups after 10 tosses?
def simulate_two(X, N, Y):
    Outcome = [] # List to store results
    for i in range(X):                            # For Loop to simulate X iterations
        flips = [flip(0.6) for j in range(N)]     # For Loop for N number of coin flips
        Outcome.append(len(list(groupby(flips)))) # Append outcome into list
    print(sum(Outcome)/(X))                       # Expected Value
    print(100-(st.norm.cdf((Y-(sum(Outcome)/(X)))/statistics.stdev(Outcome))*100)) # Print probability

simulate_two(10000000,10,6)
# There is a 33.0147991136 probability of strictly exceeding 6 groups after 10 tosses.

## (4) What is the probability of (strictly) exceeding 250 groups after 500 tosses?
simulate_two(10000000,500,250)
# There is a 20.64080991 probability of strictly exceeding 250 groups after 500 tosses.

## (5) What is the probability of (strictly) exceeding 6 groups given we (strictly) exceeded 5 groups after 10 tosses?
def simulate_three(X, N, Y, Z):
    Outcome = []         # List to store overall results
    Outcome_first = []   # List to store results from first condition
    Outcome_second = []  # List to store results from second condition
    for i in range(X):         # For Loop to simulate X iterations
        flips = [flip(0.6) for j in range(N)]       # For Loop to simulate N flips
        if len(list(groupby(flips))) >= Z:          # If condition for groups greater than Z [in first condition]
            Outcome_first.append(len(list(groupby(flips))))        # Store results into first condition
        if len(list(groupby(flips))) >= Y:          # If condition for groups greater than Y [in second condition]
            Outcome_second.append(len(list(groupby(flips))))       # Store results into second condition
        Outcome.append(len(list(groupby(flips))))   # Store results into overall results
    print(sum(Outcome) / (X))                           # Average groups from overall number of iterations
    print(sum(Outcome_first)/(len(Outcome_first)))      # Average groups who met the first condition only
    print(sum(Outcome_second)/(len(Outcome_second)))    # Average groups who met the second condition only
    # Print probability for first condition
    print(100-(st.norm.cdf((Z-(sum(Outcome)/(X)))/statistics.stdev(Outcome))*100))
    # Print probability for second condition
    print(100-(st.norm.cdf((Y-(sum(Outcome_first)/(len(Outcome_first))))/statistics.stdev(Outcome_first))*100))
    print((100-(st.norm.cdf((Z-(sum(Outcome)/(X)))/statistics.stdev(Outcome))*100))*
          (100-(st.norm.cdf((Y-(sum(Outcome_first)/(len(Outcome_first))))/statistics.stdev(Outcome_first)))))

simulate_three(1000000,10,6,5)
# There is a 31.2183607222 of (strictly) exceeding 6 groups given we (strictly) exceeded 5 groups after 10 tosses.

## (6) What is the probability of (strictly) exceeding 250 groups given we (strictly) exceeded 240 groups after 500 tosses?
simulate_three(1000000,500,250,240)

# There is a 23.4288185637 of (strictly) exceeding 250 groups given we (strictly) exceeded 240 groups after 500 tosses.

## (7) What is the probability of (strictly) exceeding 5 groups and (strictly) exceeding 5 heads after 10 tosses?
def simulate_four(X, N, Y, Z):
    Outcome = []         # List to store overall results
    Outcome_first = []   # List to store results from first condition
    Outcome_second = []  # List to store results from second condition
    for i in range(X):         # For Loop to simulate X iterations
        flips = [flip(0.6) for j in range(N)]       # For Loop to simulate N flips
        if len(list(groupby(flips))) >= Z:          # If condition for groups greater than Z [in first condition]
            Outcome_first.append(len(list(groupby(flips))))        # Store results into first condition
        if flips.count('H') >= Y:                   # If condition for number of heads is greater than 5 [in second condition]
            Outcome_second.append(len(list(groupby(flips))))       # Store results into second condition
        Outcome.append(len(list(groupby(flips))))   # Store results into overall results
    print(flips)                                        # Print flips
    print(sum(Outcome) / (X))                           # Average groups from overall number of iterations
    print(sum(Outcome_first)/(len(Outcome_first)))      # Average groups who met the first condition only
    print(sum(Outcome_second)/(len(Outcome_second)))    # Average groups who met the second condition only
    # Print probability for first condition
    print(100-(st.norm.cdf((Z-(sum(Outcome)/(X)))/statistics.stdev(Outcome))*100))
    # Print probability for second condition
    print(100-(st.norm.cdf((Y - (sum(Outcome) / (X))) / statistics.stdev(Outcome))*100))
    print((100 - (st.norm.cdf((Z - (sum(Outcome) / (X))) / statistics.stdev(Outcome)) * 100))*
    (100 - (st.norm.cdf((Y - (sum(Outcome) / (X))) / statistics.stdev(Outcome)) * 100)))

# There is a 0.3390305138 probability of (strictly) exceeding 5 groups and (strictly) exceeding 5 heads after 10 tosses.

## (8) What is the probability of (strictly) exceeding 100 groups and (strictly) exceeding 100 heads after 200 tosses?
simulate_four(1000000,200,100,100)

# There is a 0.1001451009 probability of (strictly) exceeding 5 groups and (strictly) exceeding 5 heads after 10 tosses.
