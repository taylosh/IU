/*Filename: A2.c *
*Created by: Shane Taylor*
*Created on: 9/18/2025*
*Last modified by: Shane Taylor*
*Last modified on: 9/23/2025*
*A590 Fall 2025
* Asignment: ASSIGNMENT 2*
*/


#include <stdio.h>

// Function prototypes
void arrayFunction();  
void matrixFunction();   
void calculatorFunction(); 
void transposeMatrix(int original[4][5], int transposed[5][4]); //helper function


int main() {
    /*Main function that calls all three required functions in order:
    1. Array 
    2. Matrix   
    3. Calculator 
    */
    
    printf("=== STARTING ARRAY FUNCTION ===\n");
    arrayFunction();
    
    printf("\n=== STARTING MATRIX FUNCTION ===\n");
    matrixFunction();
    
    printf("\n=== STARTING CALCULATOR FUNCTION ===\n");
    calculatorFunction();
    
    return 0;
}

void arrayFunction() {
    /*Performs array operations on two user-input arrays
    - Creates two arrays of the same size
    - Finds and displays their intersection (common elements)
    - Finds and displays their union (all unique elements)
    - Handles duplicate values appropriately
    */
    int size, i, j, k;
    
    // Get array size
    printf("Enter the size of the arrays:\n");
    scanf("%d", &size);
    
    // Create two arrays of the given size
    int arr1[size], arr2[size];
    
    // Get first array elements
    printf("Enter elements of the first array:\n");
    for(i = 0; i < size; i++) {
        scanf("%d", &arr1[i]);
    }
    
    // Get second array elements  
    printf("Enter elements of the second array:\n");
    for(i = 0; i < size; i++) {
        scanf("%d", &arr2[i]);
    }
    
    // Find and display intersection 
    printf("The intersection of two arrays is: ");
    int found_intersection = 0;
    
    for(i = 0; i < size; i++) {
        for(j = 0; j < size; j++) {
            if(arr1[i] == arr2[j]) {
                // Check if we already printed to avoid duplicates (hopefully)
                int duplicate = 0;
                for(k = 0; k < i; k++) {
                    if(arr1[k] == arr1[i]) {
                        duplicate = 1;
                        break;
                    }
                }
                if(!duplicate) {
                    printf("%d", arr1[i]);
                    found_intersection = 1;
                }
                break;  // Found match, move to next 
            }
        }
    }
    
    if(!found_intersection) {
        printf("(none)");
    }
    printf("\n");
    
    // Find and display union 
    printf("The union of two arrays is: ");
    int union_size = 0;
    int union_arr[size * 2];  // Maximum possible size if no duplicates
    
    // Add all elements from first array (checking for duplicates)
    for(i = 0; i < size; i++) {
        int duplicate = 0;
        for(j = 0; j < union_size; j++) {
            if(union_arr[j] == arr1[i]) {
                duplicate = 1;
                break;
            }
        }
        if(!duplicate) {
            union_arr[union_size] = arr1[i];
            union_size++;
        }
    }
    
    // Add elements from second array (check for duplicates)
    for(i = 0; i < size; i++) {
        int duplicate = 0;
        for(j = 0; j < union_size; j++) {
            if(union_arr[j] == arr2[i]) {
                duplicate = 1;
                break;
            }
        }
        if(!duplicate) {
            union_arr[union_size] = arr2[i];
            union_size++;
        }
    }
    
    // Display union
    for(i = 0; i < union_size; i++) {
        printf("%d", union_arr[i]);
    }
    printf("\n");
}

// Transpose heelper function that takes matrices as arguments
void transposeMatrix(int original[4][5], int transposed[5][4]) {
    int i, j;
    for(i = 0; i < 4; i++) {
        for(j = 0; j < 5; j++) {
            transposed[j][i] = original[i][j];
        }
    }
}

void matrixFunction() {
    /*Demonstrates matrix transposition with helper function
    * - Creates a 4x5 matrix with predefined values
    * - Transposes it to a 5x4 matrix 
    * - Displays original and transposed matrices
    */
    int i, j;
    
    // Create the 4x5 matrix
    int original[4][5] = {
        {1, 2, 3, 4, 5},
        {6, 7, 8, 9, 10},
        {10, 9, 8, 7, 6},
        {5, 4, 3, 2, 1}
    };
    
    // Create empty 5x4 matrix for transposed reslt
    int transposed[5][4];
    
    // Transpose matrix using helper function
    transposeMatrix(original, transposed);
    
    // Display original 
    printf("The original matrix was:\n");
    for(i = 0; i < 4; i++) {
        for(j = 0; j < 5; j++) {
            printf("%d ", original[i][j]);
        }
        printf("\n");
    }
    
    printf("\n");
    
    // Display transposed 
    printf("The transposed matrix is:\n");
    for(i = 0; i < 5; i++) {
        for(j = 0; j < 4; j++) {
            printf("%d ", transposed[i][j]);
        }
        printf("\n");
    }
}

void calculatorFunction() {
    /*Implements a calculator with accumulator
    - Supports operators: +, -, *, /, S, and E
    - Handles division by zero with error message
    - Handles unknown operators with error message  
    - Maintains accumulator state throughout calculations
    - Ends with 'E' operator
    */
    double accumulator = 0.0;
    double number;
    char operator;
    int initialized = 0;  // Track if accumulator has been initialized with 'S'
    
    printf("Begin Calculations\n\n");
    printf("Initialize Accumulator with data of the form\n");
    printf("\"number\" \"S\" which sets the Accumulator to the value of the number\n");
    
    // Main calculator loop
    while(1) {
        // Read input: number then operator
        scanf("%lf %c", &number, &operator);
        
        // Process operator
        switch(operator) {
            case 'S':
            case 's':
                // Set accumulator 
                accumulator = number;
                initialized = 1;
                break;
                
            case 'E':
            case 'e':
                // End calculation
                printf("Value in the Accumulator = %.6lf\n", accumulator);
                printf("End of Calculations.\n");
                return;  // Exit 
                
            case '+':
                if(!initialized) {
                    printf("Error: Accumulator not initialized. Use 'S' first.\n");
                    continue;
                }
                accumulator += number;
                break;
                
            case '-':
                if(!initialized) {
                    printf("Error: Accumulator not initialized. Use 'S' first.\n");
                    continue;
                }
                accumulator -= number;
                break;
                
            case '*':
                if(!initialized) {
                    printf("Error: Accumulator not initialized. Use 'S' first.\n");
                    continue;
                }
                accumulator *= number;
                break;
                
            case '/':
                if(!initialized) {
                    printf("Error: Accumulator not initialized. Use 'S' first.\n");
                    continue;
                }
                if(number == 0.0) {
                    printf("Can not divide by 0.\n");
                } else {
                    accumulator /= number;
                }
                break;
                
            default:
                // Handle unknown 
                printf("Unknown operator.\n");
                break;
        }
        
        // Display current accumulator value after each operation
        printf("Value in the Accumulator = %.6lf\n", accumulator);
    }
}