import matplotlib.pyplot as plt
import time

from search import linenar_search
from search import binary_search

fig, (plt1, plt2) = plt.subplots(nrows=1, ncols=2)


def linear_search_complexity():
    bestCaseList = []
    worstCaseList = []
    randomList = range(100, 100000, 100)

    # For Linear Search best case
    for num in randomList:
        bestCaseStartTime = time.time()
        linenar_search(range(num), 0)
        bestCaseEndTime = time.time()
        bestCaseList.append((bestCaseEndTime-bestCaseStartTime)*1000*1000)
        # For Linear Search Worst case
        worstCaseStartTime = time.time()
        linenar_search(range(num), -5)
        worstCaseEndTime = time.time()
        worstCaseList.append((worstCaseEndTime-worstCaseStartTime)*1000*1000)

    plt1.set_title("Linear Search")
    plt1.set_xlabel("Array Size")
    plt1.set_ylabel("Time(in microseconds)")
    plt1.plot(randomList, bestCaseList, '*', label="Best Case")
    plt1.plot(randomList, worstCaseList, '.', label="Worst Case")
    plt1.legend()


def binary_search_complexity():
    bestCaseList = []
    worstCaseList = []
    randomList = range(100, 1000000, 100)
    # For Linear Search best case
    for num in randomList:
        bestCaseStartTime = time.time()
        binary_search(range(num), (num-1)//2)
        bestCaseEndTime = time.time()
        bestCaseList.append((bestCaseEndTime-bestCaseStartTime)
                            * 1000*1000)  # Append time in best case time in microseconds
        worstCaseStartTime = time.time()
        binary_search(range(num), num)
        worstCaseEndTime = time.time()
        worstCaseList.append((worstCaseEndTime-worstCaseStartTime)
                             * 1000*1000)  # Append time in worst case time in microseconds

    plt2.set_title("Binary Search")
    plt2.set_xlabel("Array Size")
    plt2.set_ylabel("Time(in microseconds)")
    plt2.plot(randomList, bestCaseList, '.', label="Best Case")
    plt2.plot(randomList, worstCaseList, '*', label="Worst Case")
    plt2.legend()


if __name__ == '__main__':
    linear_search_complexity()
    binary_search_complexity()
    plt.show()
