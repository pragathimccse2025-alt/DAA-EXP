import time
import random
import sys

import matplotlib.pyplot as plt #type:ignore
sys.setrecursionlimit(10000)

# Global counters
ms_comp = 0
qs_comp = 0
hs_comp = 0

def merge(arr, l, m, r):
    global ms_comp # MUST be first
    n1 = m - l + 1
    n2 = r - m
    L = arr[l:l+n1]
    R = arr[m+1:m+1+n2]
    i = j = 0
    k = l
    while i < n1 and j < n2:
        ms_comp += 1
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1

def merge_sort(arr, l, r):
    global ms_comp # MUST be first
    if l < r:
        m = l + (r-l)//2
        merge_sort(arr, l, m)
        merge_sort(arr, m+1, r)
        merge(arr, l, m, r)

def partition(arr, low, high):
    global qs_comp # MUST be first
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        qs_comp += 1
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i+1

def quick_sort(arr, low, high):
    global qs_comp # MUST be first
    if low < high:
        pi = partition(arr, low, high)
        quick_sort(arr, low, pi-1)
        quick_sort(arr, pi+1, high)

def heapify(arr, n, i):
    global hs_comp # MUST be first
    largest = i
    l = 2*i + 1
    r = 2*i + 2
    if l < n:
        hs_comp += 1
        if arr[l] > arr[largest]:
            largest = l
    if r < n:
        hs_comp += 1
        if arr[r] > arr[largest]:
            largest = r
    if largest!= i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heap_sort(arr):
    global hs_comp # MUST be first
    hs_comp = 0
    n = len(arr)
    for i in range(n//2 - 1, -1, -1):
        heapify(arr, n, i)
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)

# Main testing
sizes = [1000, 2000, 3000, 4000, 5000]
ms_time, qs_time, hs_time = [], [], []
ms_comps, qs_comps, hs_comps = [], [], []

print("Running Program 3 tests... Please wait")
for n in sizes:
    arr = [random.randint(1, 100000) for _ in range(n)]

    # Merge Sort
    arr1 = arr.copy()
    ms_comp = 0
    start = time.time()
    merge_sort(arr1, 0, n-1)
    ms_time.append((time.time() - start)*1000)
    ms_comps.append(ms_comp)

    # Quick Sort
    arr2 = arr.copy()
    qs_comp = 0
    start = time.time()
    quick_sort(arr2, 0, n-1)
    qs_time.append((time.time() - start)*1000)
    qs_comps.append(qs_comp)

    # Heap Sort
    arr3 = arr.copy()
    start = time.time()
    heap_sort(arr3)
    hs_time.append((time.time() - start)*1000)
    hs_comps.append(hs_comp)

# Print Table
print("\n{:<8} {:<12} {:<12} {:<12}".format("Size","MS Time","QS Time","HS Time"))
for i in range(len(sizes)):
    print("{:<8} {:<12.4f} {:<12.4f} {:<12.4f}".format(sizes[i], ms_time[i], qs_time[i], hs_time[i]))

# PLOT 1: Time
plt.figure(figsize=(8,5))
plt.plot(sizes, ms_time, marker='o', label='Merge Sort')
plt.plot(sizes, qs_time, marker='s', label='Quick Sort')
plt.plot(sizes, hs_time, marker='^', label='Heap Sort')
plt.xlabel('Array Size')
plt.ylabel('Time (ms)')
plt.title('Program 3: Time Comparison')
plt.legend()
plt.grid(True)
plt.show()

# PLOT 2: Comparisons
plt.figure(figsize=(8,5))
plt.plot(sizes, ms_comps, marker='o', label='Merge Sort')
plt.plot(sizes, qs_comps, marker='s', label='Quick Sort')
plt.plot(sizes, hs_comps, marker='^', label='Heap Sort')
plt.xlabel('Array Size')
plt.ylabel('Number of Comparisons')
plt.title('Program 3: Comparisons')
plt.legend()
plt.grid(True)
plt.show()