/*Filename: buffet.c *
*Created by: Shane Taylor*
*Created on: 9/3/2025*
*Last modified by: Shane Taylor*
*Last modified on: 9/10/2025*
*A590 Fall 2025
*Assignment 1: Prime Number Checker
* This program checks if a user-provided integer is a prime number.
*/

#include <stdio.h>

int main(void) {
    // Step 1: Declare variables
    int number;      // To store the user's input
    int isPrime = 1; // Prime flag. Start by assuming the number IS prime (1 = true).

    // Step 2: Get the number from the user
    printf("Enter a number to check if it is a prime:\n");
    scanf("%d", &number);

    // Handle edge cases: Numbers less than 2 are not prime by definition.
    if (number < 2) {
        isPrime = 0; // It is not prime.
    } else {
        // Step 3: Check for divisors from 2 to number/2
        for (int i = 2; i <= number / 2; i++) {
            // Use the modulus operator to check for divisibility
            if (number % i == 0) {
                isPrime = 0; // We found a divisor, so it's not prime.
                break;       // No need to check further, break out of the loop.
            }
        }
    }

    // Step 4: Use the 'isPrime' flag to control the output
    if (isPrime == 1) {
        printf("The number %d is a prime number.\n", number);
    } else {
        printf("The number %d is NOT a prime number.\n", number);
    }

    // Step 5: End the program
    return 0;
}


