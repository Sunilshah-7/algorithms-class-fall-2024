import math
import time
import random

# insertion sort function
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


# partition function
def partition(arr, left, right, pivot_index):
    pivot = arr[pivot_index]
    arr[pivot_index], arr[right] = arr[right], arr[pivot_index]
    store_index = left
    for i in range(left, right):
        if arr[i] < pivot:
            arr[store_index], arr[i] = arr[i], arr[store_index]
            store_index += 1
    arr[right], arr[store_index] = arr[store_index], arr[right]
    return store_index

#quickselect function
def quickselect(arr, k):
    if len(arr) <= 5:
        return insertion_sort(arr)[k]

    # Step 1: Divide the array into groups of 5
    groups = [arr[i:i+5] for i in range(0, len(arr), 5)]

    # Step 2: Sort the small groups using insertion sort
    sorted_groups = [insertion_sort(group) for group in groups]

    # Step 3: Collect all the n/5 medians from the n/5 groups
    medians = [group[len(group)//2] for group in sorted_groups]

    # Step 4: Find the median of medians recursively
    median_of_medians = quickselect(medians, len(medians)//2)

    # Step 5: Partition the array on the median of medians
    pivot_index = arr.index(median_of_medians)
    partition_index = partition(arr, 0, len(arr) - 1, pivot_index)

    # Step 6: Recursively call QuickSelect on the appropriate partition
    if k == partition_index:
        return arr[k]
    elif k < partition_index:
        return quickselect(arr[:partition_index], k)
    else:
        return quickselect(arr[partition_index + 1:], k - partition_index - 1)


#find the experimental results for time taken to find the median
def quickselect_experiment(n):
    arr = [random.randint(1, 1000000) for _ in range(n)]
    k = n // 2  # Finding median
    
    start_time = time.time_ns()
    result = quickselect(arr, k)
    end_time = time.time_ns()
    
    return end_time - start_time


n_values = [500, 1000, 5000, 10000, 50000]
experimental_results = []

for n in n_values:
    trials = 5
    times = [quickselect_experiment(n) for _ in range(trials)]
    average_time = sum(times) / trials
    print(f"Average time for n={n}: {average_time} ns")
