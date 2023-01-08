#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <time.h>

int roll(int die);
int rollTotal(int count, int die);

int main(int argc, char **argv) {
    time_t t;
    srand((unsigned) time(&t));
    
}

int roll(int die){
    return rand()%die + 1;
}

int rollTotal(int count, int die) {
    int rtn = 0;
    for(int i = 0; i < count; i++) {
        rtn += roll(die);
    }
}