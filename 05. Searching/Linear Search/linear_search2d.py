def linear_search_2d(array, target):
  """Performs a linear search on a 2D array.

  Args:
    array: A 2D array of elements.
    target: The element to search for.

  Returns:
    True if the target element is found in the array, False otherwise.
  """

  for row in range(len(array)):
    for col in range(len(array[row])):
      if array[row][col] == target:
        return True
  return False


# Example usage:

array = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
target = 5

if linear_search_2d(array, target):
  print("The target element is found in the array.")
else:
  print("The target element is not found in the array.")
