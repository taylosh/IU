/*Filename: callingfunc.c *
*Created by: Shane Taylor*
*Created on: 9/10/2025*
*Last modified by: Shane Taylor*
*Last modified on: 9/19/2025*
*A590 Fall 2025
* Assignment: PROGRAM 2*
*/

#include <stdio.h>

/* Function prototypes */
void loops(void);
void conditionals(void);
void firstswap(void);

int main(void) {
    /* Main function that calls all three required functions in order */
    printf("THIS IS MY LOOPS FUNCTION.\n\n");
    loops();

    printf("THIS IS MY CONDITIONALS FUNCTION.\n\n");
    conditionals();

    printf("THIS IS MY FIRST ARRAY FUNCTION.\n\n");
    firstswap();

    return 0;
}

/* Demonstrates basic for-loop functionality */
void loops(void) {
    int i;
    /* Loop 4 times, printing the current iteration value */
    for (i = 0; i < 4; i++) {
        printf("callingfunc: received %d\n", i);
    }
}

/* Demonstrates basic conditional if-else logic */
void conditionals(void) {
    int x = 5;
    /* Check if x is greater than 3 and print appropriate message */
    if (x > 3) {
        printf("x is greater than 3 (x=%d)\n", x);
    } else {
        printf("x is not greater than 3 (x=%d)\n", x);
    }
}

/* Demonstrates array swapping - one pass of bubble sort */
void firstswap(void) {
    int arr[] = {3, 1, 4, 2};
    int n = sizeof(arr) / sizeof(arr[0]);
    int i, tmp;

    /* Display array before swapping */
    printf("Before swap pass: ");
    for (i = 0; i < n; i++) printf("%d ", arr[i]);
    printf("\n");

    /*****************************************************
    * Explanation of "if (c[j]~c[k] < 10)" from class:
    * 
    * This line appears to contain a typo (~ instead of -). 
    * If it were "if (c[j]-c[k] < 10)", it would:
    * 1. Subtract the ASCII value of character c[k] from c[j]
    * 2. Check if the difference is less than 10
    * 
    * This could be used to:
    * - Check if two characters are within 10 ASCII values
    * - Validate character ranges or proximity
    * - Implement custom character-based algorithms
    * 
    * In our implementation, we use "if (arr[i] > arr[i + 1])" 
    * to compare integer values for sorting adjacent elements.
    *****************************************************/
    
    /* Perform one pass of bubble sort - swap adjacent elements if out of order */
    for (i = 0; i < n - 1; i++) {
        if (arr[i] > arr[i + 1]) {
            /* Swap elements at positions i and i+1 */
            tmp = arr[i];
            arr[i] = arr[i + 1];
            arr[i + 1] = tmp;
            printf("swapped indices %d and %d -> ", i, i+1);
            for (int k = 0; k < n; k++) printf("%d ", arr[k]);
            printf("\n");
        }
    }

    /* Display array after swapping */
    printf("After swap pass:  ");
    for (i = 0; i < n; i++) printf("%d ", arr[i]);
    printf("\n");
}