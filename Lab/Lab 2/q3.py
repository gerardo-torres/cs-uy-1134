n = [2**i for i in range(7, 13)]

import time
import random

class PolyTimer:
    def __init__(self):
        self.start = time.time()

    def elapsed(self):
        return time.time() - self.start

    def reset(self):
        self.start = time.time()


def maxSubsequenceSum2(vals):
    n = len(vals)
    maxSum = 0
    seqStart = 0
    seqEnd = 0
    for i in range(n):
        thisSum = 0
        for j in range(i, n):
            thisSum += vals[j]
            if (thisSum > maxSum):
                maxSum = thisSum
                seqStart = i
                seqEnd = j
    return maxSum, seqStart, seqEnd


def maxSubsequenceSum1(vals):
    n = len(vals)
    maxSum = 0
    seqStart = 0
    seqEnd = 0
    for i in range(n):
        for j in range(i, n):
            thisSum = 0
            for k in range(i, j + 1):
                thisSum += vals[k]
            if (thisSum > maxSum):
                maxSum = thisSum
                seqStart = i
                seqEnd = j
    return maxSum, seqStart, seqEnd

def maxSubsequenceSum3(vals):
    n = len(vals)
    thisSum = 0
    maxSum = 0
    i = 0
    seqStart = 0
    seqEnd = 0
    for j in range(n):
        thisSum += vals[j]
        if (thisSum > maxSum):
            maxSum = thisSum
            seqStart = i
            seqEnd = j
        elif (thisSum < 0):
            i = j + 1
            thisSum = 0
    return maxSum, seqStart, seqEnd

def main():
    file_in = open("results.csv", "w")
    t = PolyTimer()
    nuClicks = 0.0
    for i in range(len(n)):
        lst = [random.randint(-1000, 1000) for i in range(n[i])]
        t.reset()
        result1, start1, end1 = maxSubsequenceSum1(lst)
        nuClicks1 = t.elapsed()
        print(nuClicks1, file=file_in)
        t.reset()
        result2, start2, end2 = maxSubsequenceSum2(lst)
        nuClicks2 = t.elapsed()
        print(nuClicks2, file=file_in)
        t.reset()
        result3, start3, end3 = maxSubsequenceSum3(lst)
        nuClicks3 = t.elapsed()
        print(nuClicks3, file=file_in)
    file_in.close()
main()
