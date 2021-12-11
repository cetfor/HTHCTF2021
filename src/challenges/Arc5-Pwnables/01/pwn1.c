#include <stdlib.h>
#include <stdio.h>
#include <string.h>

/*
 * sudo gcc -O0 -fno-stack-protector /home/pwn1/pwn1.c -o /home/pwn1/pwn1
 * sudo chown -R pwn1 /home/pwn1
 *
 * Example payload: 
 * python -c "print('9\n' + 'KROM' + 'A'*40 + 'BASH'[::-1])" | ./pwn1
 *
 * You must keep stdin from closing using something like:
 * cat <(python -c "print('9\n' + 'KROM' + 'A'*40 + 'BASH'[::-1])") - | ./pwn1 
 */

void command_krom(int commandCode)
{
    int c;
    FILE *file;
    file = fopen("/home/pwn1/krom_log.txt", "r");
    if (file) {
        puts("Printing KROM logs...");
        while ((c = getc(file)) != EOF) {
            putchar(c);
        }
        fclose(file);
    }
    fflush(stdout);

    // 0x42415348 = BASH
    if (commandCode == 0x42415348)
    {
        puts("Welcome KROM!");
        fflush(stdout);
        system("/bin/sh");
    }
}

void command_st0ke(unsigned int commandCode)
{
    int c;
    FILE *file;
    file = fopen("/home/pwn1/st0ke_log.txt", "r");
    if (file) {
        puts("Printing st0ke logs...");
        while ((c = getc(file)) != EOF) {
            putchar(c);
        }
        fclose(file);
    }
    fflush(stdout);
}

int main(int argc, char** argv)
{
    char commandCodeStr[8];
    char commandString[24];
    int commandCode = 0;
    
    puts(" ****************************************************************************\n \
This is a Nexxus computer system, which may be accessed\n  \
and used only for authorized Nexxus business by authorized personnel.\n \
Unauthorized access or use of this computer system may subject violators\n \
to criminal, civil, and/or administrative action.\n\n \
All information on this computer system may be intercepted, recorded,\n \
read, copied, and disclosed by and to authorized personnel for official\n \
purposes, including criminal investigations. Such information includes\n \
sensitive data encrypted to comply with confidentiality and privacy\n \
requirements. Access or use of this computer system by any person, whether\n \
authorized or unauthorized, constitutes consent to these terms. There is no\n \
right of privacy in this system.\n \
****************************************************************************\n");

    fflush(stdout);
    fputs("Shell relay server.\nEnter command code: ", stdout);
    fgets(commandCodeStr, sizeof(commandCodeStr)-1, stdin);
    commandCodeStr[strcspn(commandCodeStr, "\r\n")] = 0;

    commandCode = atoi(commandCodeStr);
    if (commandCode <= 0) {
        printf("Invalid command code: \"%s\".\nDisconnected.\n", commandCodeStr);
        fflush(stdout);
        return -1;
    }

    fputs("\nEnter command: ", stdout);
    fflush(stdout);
    fgets(commandString, 64, stdin);
    commandString[strcspn(commandString, "\r\n")] = 0;

    if (!strncmp(commandString, "KROM", 4)) {
        command_krom(commandCode);
    } else if (!strncmp(commandString, "ST0KE", 5)) {
        command_st0ke(commandCode);
    } else {
        printf("Invalid command: \"%s\".\nDisconnected.\n", commandString);
        fflush(stdout);
        return -1;
    }

    puts("Disconnected.");
    fflush(stdout);

    return EXIT_SUCCESS;
}

