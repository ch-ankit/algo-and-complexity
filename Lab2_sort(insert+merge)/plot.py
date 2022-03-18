import matplotlib.pyplot as plt
import time

from sort import insertion_sort
from sort import merge_sort


def insertion_sort_complexity():
    bestCaseList = []
    worstCaseList = []
    randomList = range(10, 1000, 10)

    # For insertion sort best case
    for num in randomList:
        bestCaseStartTime = time.time_ns()
        insertion_sort(list(range(num)))
        bestCaseEndTime = time.time_ns()
        bestCaseList.append((bestCaseEndTime-bestCaseStartTime))
        # For insertion Sort Worst case
        worstCaseStartTime = time.time_ns()
        insertion_sort(list(reversed(range(num))))
        worstCaseEndTime = time.time_ns()
        worstCaseList.append((worstCaseEndTime-worstCaseStartTime))
    plt.figure("Insertion Best Case")
    plt.title("Insertion Sort(Best Case)")
    plt.xlabel("Array Size")
    plt.ylabel("Time(in nanoseconds)")
    plt.plot(randomList, bestCaseList, '*', label="Best Case")
    plt.legend()
    plt.figure("Insertion Worst Case")
    plt.title("Insertion Sort(Worst Case)")
    plt.xlabel("Array Size")
    plt.ylabel("Time(in nanoseconds)")
    plt.plot(randomList, worstCaseList, '.', label="Worst Case")
    plt.legend()


def merge_sort_complexity():
    bestCaseList = []
    randomList = range(10, 1000, 10)
    # For merge sort best case
    for num in randomList:
        bestCaseStartTime = time.time_ns()
        merge_sort(list(range(num)),0, len(range(num))-1)
        bestCaseEndTime = time.time_ns()
        bestCaseList.append((bestCaseEndTime-bestCaseStartTime))
    plt.figure("Merge Best Case")
    plt.title("Merge Sort(Best Case)")
    plt.xlabel("Array Size")
    plt.ylabel("Time(in nanoseconds)")
    plt.plot(randomList, bestCaseList, '.', label="Best Case")
    plt.legend()


if __name__ == '__main__':
    insertion_sort_complexity()
    merge_sort_complexity()
    plt.show()