#include <stdlib.h>
#include <stdio.h>
#include <string.h>

/*
 * sudo gcc /home/pwn2/pwn2.c -o /home/pwn2/pwn2
 * python3 -c "print('checkflag\n' + '%lx.'*80)" | ./pwn2
 */

int main(int argc, char** argv)
{
    char flag[64];
    char commandString[64];
    char userflag[256];

    memset(&flag, 0, 64);
    memset(&commandString, 0, 64);
    memset(&userflag, 0, 256);
    
    FILE *fp = fopen("/home/pwn2/flag.txt", "r");
    if (fp != NULL) {
        size_t newLen = fread(flag, sizeof(char), 63, fp);
        if ( ferror( fp ) != 0 ) {
            fputs("Error reading file", stderr);
        } else {
            flag[newLen++] = '\0'; /* Just to be safe. */
        }
        fclose(fp);
    }

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

    // prompt user
    fputs("Command: ", stdout);
    fflush(stdout);

    // get command remove newline chars
    fgets(commandString, 64, stdin);
    commandString[strcspn(commandString, "\r\n")] = 0;

    // check command
    if (!strncmp(commandString, "checkflag", strlen("checkflag"))) {
        fputs("flag: ", stdout);
        fflush(stdout);
        fgets(userflag, 256, stdin);
        userflag[strcspn(userflag, "\r\n")] = 0;
        if (!strncmp(userflag, flag, strlen(flag))) {
            printf("You got the correct flag! (%s)\n", flag);
        } else {
            puts("Wrong flag!");
            printf(userflag);
        }
    } else {
        puts("Invalid command!");
    }

    puts("Disconnected.");
    return EXIT_SUCCESS;
}
