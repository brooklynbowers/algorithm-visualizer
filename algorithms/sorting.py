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

# print statement to check if the code is working correctly
# print(bubble_sort([4, 3, 5, 6]))

# creating a section for user input
user_input = input('Enter a list of numbers where each number entered is separated by a space: ')

arr = list(map(int, user_input.split()))

sorted_arr = bubble_sort(arr)

print('Here is your sorted array: ', sorted_arr)
