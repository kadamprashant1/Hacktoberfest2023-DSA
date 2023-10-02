public class linear_search2d {
    public static void main(String[] args) {
        int[][] array2D = {
            {1, 2, 3},
            {4, 5, 6},
            {7, 8, 9}
        };
        
        int target = 5;
        boolean found = false;
        
        // Loop through each row of the 2D array
        for (int i = 0; i < array2D.length; i++) {
            // Loop through each element in the current row
            for (int j = 0; j < array2D[i].length; j++) {
                if (array2D[i][j] == target) {
                    found = true;
                    System.out.println("Element " + target + " found at row " + i + " and column " + j);
                    break; // Optional: To exit the inner loop when the element is found
                }
            }
            if (found) {
                break; // Optional: To exit the outer loop when the element is found
            }
        }
        
        if (!found) {
            System.out.println("Element " + target + " not found in the 2D array.");
        }
    }
}
