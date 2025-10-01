/*Filename: buffet.c *
*Created by: Shane Taylor*
*Created on: 9/3/2025*
*Last modified by: Shane Taylor*
*Last modified on: 9/10/2025*
*A590 Fall 2025
*Assignment 1: Depreciation Calculator
* This program calculates the salvage value of an item
* given its purchase price, years of service, and annual depreciation.
*/

#include <stdio.h>

int main(void) {
    // Step 1: Declare variables to store user input and the result
    float purchasePrice;
    int yearsService;
    float annualDepreciation;
    float salvageValue;

    // Step 2: Prompt the user and read their input
    printf("Enter the purchase price, years of service, annual depreciation:\n");
    scanf("%f %d %f", &purchasePrice, &yearsService, &annualDepreciation);

    // Step 3: Perform the calculation using the rearranged formula
    salvageValue = purchasePrice - (annualDepreciation * yearsService);

    // Step 4: Print the result
    printf("The salvage value of the item is %f\n", salvageValue);

    // Step 5: End the program
    return 0;
}


