#include <stdio.h>

void main() {

    // for the purpose of example, declare variables
    int empty = 0;
    int box = 1;
    int bottle = 2;
    int green_folders = 3;

    // this contains all the items
    int container[7] = {0, box, 0, 0, bottle, 0, 0};
    
    // acquired item will go here
    int acquired_item;

    // go through each of the items
    for (int i=0; i<7; i++) {
        if (container[i] == green_folders) {
            acquired_item = container[i];
            container[i] = empty;   // 0
            break;
        }
    }

    
    // check if you got the green folders
    if (acquired_item == green_folders) {
        printf("*Tigershark grabs item*\nSuccess!");
    } else {
        printf("*Tigershark is confused*\nItem not found in container...");
    }

}