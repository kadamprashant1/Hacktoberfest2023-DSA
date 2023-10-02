public class linear_Search {
    public static int linearSearch(int[] arr, int target) {
        // Iterate through the array
        for (int i = 0; i < arr.length; i++) {
            // If the current element is equal to the target, return its index
            if (arr[i] == target) {
                return i;
            }
        }
        // If the target is not found in the array, return -1 to indicate that it's not present
        return -1;
    }

    public static void main(String[] args) {
        int[] arr = {10, 20, 30, 40, 50};
        int target = 30;

        // Perform a linear search to find the target element in the array
        int result = linear_Search(arr, target);

        // Check the result and display the appropriate message
        if (result != -1) {
            System.out.println("Element found at index " + result);
        } else {
            System.out.println("Element not found in the array.");
        }
    }
}
