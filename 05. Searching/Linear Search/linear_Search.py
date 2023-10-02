def linear_search(arr, target):
    """
    Perform a linear search to find the target element in the array.

    Args:
    - arr: A list or array to search through.
    - target: The element to search for.

    Returns:
    - The index of the target element if found, or -1 if not found.
    """
    for i in range(len(arr)):
        if arr[i] == target:
            return i  # Element found, return its index
    return -1  # Element not found

# Example usage:
my_list = [2, 4, 6, 8, 10]
target_element = 6
result = linear_search(my_list, target_element)

if result != -1:
    print(f"Element {target_element} found at index {result}.")
else:
    print(f"Element {target_element} not found in the list.")
