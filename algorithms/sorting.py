# Bubble Sort Algorithm

def bubble_sort(arr):
    for i in range(len(arr) - 1):
        # i represents each value in the array, the range 
        # is the 1 minus the length of the array 
        for j in range(len(arr)- i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
        # loop through each index of the array, swap if the first index value is 
        # larger than the second index value
    return arr

print(bubble_sort([4, 3, 5, 6]))