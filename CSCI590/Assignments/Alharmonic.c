/*Filename: buffet.c *
*Created by: Shane Taylor*
*Created on: 9/3/2025*
*Last modified by: Shane Taylor*
*Last modified on: 9/10/2025*
*A590 Fall 2025
*Assignment 1: Harmonic Series Calculator
* This program calculates the sum of the harmonic series up to a user-provided positive integer n.
*/

#include <stdio.h>

int main(void) {
    // Step 1: Declare variables
    int n;
    float sum = 0.0; // Initialize the sum to 0. Use float for decimal precision.

    // Step 2: Get the initial value from the user
    printf("Enter a value to calculate the value of this harmonic series:\n");
    scanf("%d", &n);

    // Step 3: Input Validation - Check if the number is negative
    // Use a while loop to keep asking until a positive number is entered.
    while (n <= 0) {
        printf("Please enter a POSITIVE Number: \n\n");
        scanf("%d", &n); // Get a new value for n
    }

    // Step 4: Calculate the harmonic series
    // We need to go from 1 to n. The term is 1 / i.
    for (int i = 1; i <= n; i++) {
        sum += 1.0 / i; // Add the current term (1/i) to the running total (sum)
    }

    // Step 5: Print the result with 6 decimal places as shown in the sample
    printf("The value for the series is: %f.\n", sum);

    // Step 6: End the program
    return 0;
}