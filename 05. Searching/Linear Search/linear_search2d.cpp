#include <iostream>

using namespace std;

int main() {
    // Define a 2D array (matrix)
    int rows, cols;
    cout << "Enter the number of rows: ";
    cin >> rows;
    cout << "Enter the number of columns: ";
    cin >> cols;

    int arr[rows][cols];

    // Input elements into the 2D array
    cout << "Enter elements into the 2D array:" << endl;
    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < cols; j++) {
            cin >> arr[i][j];
        }
    }

    // Define the target value you want to search for
    int target;
    cout << "Enter the element you want to search for: ";
    cin >> target;

    // Perform the linear search
    bool found = false;
    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < cols; j++) {
            if (arr[i][j] == target) {
                found = true;
                cout << "Element " << target << " found at position (" << i << ", " << j << ")" << endl;
            }
        }
    }

    if (!found) {
        cout << "Element " << target << " not found in the 2D array." << endl;
    }

    return 0;
}
