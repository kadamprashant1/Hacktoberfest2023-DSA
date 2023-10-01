# Define a function for comb sort
def comb_sort(arr):
    # Get the length of the input array
    n = len(arr)
    # Initialize the initial gap as the length of the array
    gap = n
    # Define the shrink factor for the gap
    shrink = 1.3
    # Initialize a variable to keep track of whether any swaps were made
    swapped = True

    # Continue looping until the gap becomes 1 and no swaps are made
    while gap > 1 or swapped:
        # Calculate the new gap by shrinking the current gap
        gap = int(gap / shrink)
        # Reset the swapped flag to False at the beginning of each pass
        swapped = False
        i = 0

        # Iterate through the array with the current gap
        while i + gap < n:
            # Compare elements that are 'gap' distance apart and swap them if necessary
            if arr[i] > arr[i + gap]:
                arr[i], arr[i + gap] = arr[i + gap], arr[i]  # Swap elements
                swapped = True  # Set swapped flag to True to indicate a swap
            i += 1

    # Return the sorted array
    return arr

# Driver code to test the sorting algorithm
list_a = [0.12, 0.45, 0.57, 0.23, 0.24]
print(comb_sort(list_a))  # Print the sorted result
