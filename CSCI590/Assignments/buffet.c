/*Filename: buffet.c *
*Created by: Shane Taylor*
*Created on: 9/3/2025*
*Last modified by: Shane Taylor*
*Last modified on: 9/10/2025*
* Assignment: PROGRAM 1*
*/

#include <stdio.h>

int main() {
    // Display sizes of various data types
    printf("Size of char: %lu bytes\n", sizeof(char));
    printf("Size of short: %lu bytes\n", sizeof(short));
    printf("Size of int: %lu bytes\n", sizeof(int));
    printf("Size of long: %lu bytes\n", sizeof(long));
    printf("Size of float: %lu bytes\n", sizeof(float));
    printf("Size of double: %lu bytes\n", sizeof(double));
    
    // Declare and initialize variables of different data types
    int integerVar = 10;
    float floatVar = 3.14;
    char charVar = 'A';
    double doubleVar = 2.71828;
    short shortVar = 5;
    long longVar = 1000000;
    
    // Display initial values of variables
    printf("\nInitial values:\n");
    printf("Integer: %d\n", integerVar);
    printf("Float: %.2f\n", floatVar);
    printf("Char: %c\n", charVar);
    printf("Double: %.5lf\n", doubleVar);
    printf("Short: %d\n", shortVar);
    printf("Long: %ld\n", longVar);
    
    // Additional variables for arithmetic operations
    int a = 15;
    int b = 7;
    int sum, difference, product, quotient, remainder;
    
    // Perform basic arithmetic operations
    sum = a + b;
    difference = a - b;
    product = a * b;
    quotient = a / b;
    remainder = a % b;
    
    // Display results of arithmetic operations
    printf("\nArithmetic operations with %d and %d:\n", a, b);
    printf("Sum: %d\n", sum);
    printf("Difference: %d\n", difference);
    printf("Product: %d\n", product);
    printf("Quotient: %d\n", quotient);
    printf("Remainder: %d\n", remainder);
    
    // Additional operations using previous results
    int result1 = sum * 2;
    int result2 = difference + product;
    int result3 = quotient - remainder;
    
    // Display results of additional operations
    printf("\nAdditional operations:\n");
    printf("Sum * 2: %d\n", result1);
    printf("Difference + Product: %d\n", result2);
    printf("Quotient - Remainder: %d\n", result3);
    
    // Sum of squares algorithm
    // This section finds sums that can be formed by more than one pair of squares.
    printf("\nSums of squares with multiple solutions:\n");
    printf("(Format: Sum = a² + b² = c² + d²)\n");
    
    int n = 100; // Upper limit for numbers to square
    int total;    // Holds the sum of two squares
    
    // Loop through all possible sums
    for (total = 2; total <= 2 * n * n; total++) {
        int count = 0;        // Counter for pairs found for this total
        int first_a = 0, first_b = 0; // Store the first pair found
        int second_a = 0, second_b = 0; // Store the second pair found
        
        // Try all possible values for the first number (i)
        for (int i = 1; i <= n; i++) {
            // Calculate the square needed to complete the sum
            int remaining = total - (i * i);
            
            // If the remaining amount is negative or too large, skip
            if (remaining < 1 || remaining > n * n) continue;
            
            // Find an integer j such that j*j equals the remaining amount
            int j = 1;
            while (j <= n && j * j < remaining) {
                j++;
            }
            
            // Check if we found a valid pair
            if (j <= n && j * j == remaining) {
                // If this is the first pair found, store it
                if (count == 0) {
                    first_a = i;
                    first_b = j;
                    count = 1;
                } 
                // If this is a different pair, store it and we're done
                else if (i != first_b || j != first_a) { // Avoid duplicates like (1,2) and (2,1)
                    second_a = i;
                    second_b = j;
                    count = 2;
                    break; // Found two pairs, no need to continue
                }
            }
        }
        
        // If we found at least two distinct pairs, print the result
        if (count >= 2) {
            printf("%d = %d² + %d² = %d² + %d²\n", 
                   total, first_a, first_b, second_a, second_b);
        }
    }
    
    return 0;  // Indicate successful program execution
}