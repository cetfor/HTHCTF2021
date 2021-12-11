#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// 682491

unsigned char digit1(unsigned char digit) {
    if (atoi(&digit) == 6) {
        return 1;
    }
    return 0;
}

unsigned char digit2(unsigned char digit) { 
    if (atoi(&digit) == 8) {
        return 1;
    }
    return 0;
}

unsigned char digit3(unsigned char digit) { 
    if (atoi(&digit) == 2) {
        return 1;
    }
    return 0;
}

unsigned char digit4(unsigned char digit) { 
    if (atoi(&digit) == 4) {
        return 1;
    }
    return 0;
}

unsigned char digit5(unsigned char digit) { 
    if (atoi(&digit) == 9) {
        return 1;
    }
    return 0;
}

unsigned char digit6(unsigned char digit) { 
    if (atoi(&digit) == 1) {
        return 1;
    }
    return 0;
}

int main(int argc, char** argv)
{
    int c;
    FILE *file;
    char *pin = malloc(32);
    memset(pin, 0, 32);
    if (pin == NULL) {
        return -1;
    }

    fputs("Nexxus Data Warehouse East. Gate 3A PIN: ", stdout);
    fflush(stdout);
    fgets(pin, 7, stdin);
    if (strlen(pin) != 6) {
        puts("Invalid PIN.");
        fflush(stdout);
        return 1;
    }

    if (digit1(pin[0]) == 0 || digit2(pin[1]) == 0 || digit3(pin[2]) == 0 || 
        digit4(pin[3]) == 0 || digit5(pin[4]) == 0 || digit6(pin[5]) == 0) {
        puts("Incorrect PIN.");
        fflush(stdout);
        return 1;
    }
    else {
        puts("Welcome to Nexxus Data Warehouse East.");
        file = fopen("/home/re1/flag.txt", "r");
        if (file) {
            while ((c = getc(file)) != EOF) {
                putchar(c);
            }
            fclose(file);
        }
        fflush(stdout);
    }
    
    return 0;
}
