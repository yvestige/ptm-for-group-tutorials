#include <stdio.h>
#include <string.h>

void main() {

    // variable manipulation
    char string[] = "word";

    // print original values
    printf("String value before manipulation: %s\n", string);

    // accessing characters and manipulating
    for(int i=0; i<strlen(string); i++) {
        string[i]++; // add one ascii value to it
    }

    // print original values
    printf("String value after manipulation: %s\n", string);



}