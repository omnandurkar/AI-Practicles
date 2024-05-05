# Implement Greedy search algorithm for any of the following application:
# I. Selection Sort

def selectionSort(array, size):
    for val in range(size):
        minvalue = val
        for i in range(val + 1, size):
            if array[i] < array[minvalue]:
                minvalue = i
        array[val], array[minvalue] = array[minvalue], array[val]  # Swap the elements

arr = [6, 3, 5, 2, 1, 4]
length = len(arr)
print("Before sorting:", arr)
selectionSort(arr, length)
print("After sorting:", arr)