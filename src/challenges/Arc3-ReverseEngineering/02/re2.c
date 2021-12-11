#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

/*
*Type: Generate a key based on a challenge seed*

This is a server-side challenge that gives a user a challenge and expects a specific response.
The challenge is a 15 byte value and completely random, seeded correctly from the OS. The user 
needs to reverse engineer the algorithm and present the correct response back to the server.

Upon submitting a successful response, the challenge will read a flag.txt file and print the value to the user.
*/

char *getChallenge(char *challenge, size_t size)
{
    const char charset[] = "abcdefghijklmnopqrstuvwxyz";
    if (size) {
        --size;
        for (size_t n = 0; n < size; n++) {
            int key = rand() % (int) (sizeof charset - 1);
            challenge[n] = charset[key];
        }
        challenge[size] = '\0';
    }
    return challenge;
}

char* rotX(char* message, int shift)
{
    char* cipher = malloc(strlen(message));
    memset(cipher, 0, strlen(message));
    const char charset[] = "abcdefghijklmnopqrstuvwxyz";
    
    for(int i = 0; i < strlen(message); i++)
    {
        int num = (message[i] - 'a' + shift) % 26;
        cipher[i] = charset[num];
    }
    return cipher;
}

void giveFlag() {
    // open flag.txt and print the flag.
    int c;
    FILE *fp;
    fp = fopen("/home/re2/flag.txt", "r");
    if (fp) {
        while ((c = getc(fp)) != EOF)
            putchar(c);
        fclose(fp);
    }
}

int main(int argc, char** argv)
{
    // seed prng
    srand(time(NULL));

    // setup challenge buffer
    size_t challengeSize = 32;
    size_t challengeLength = 16;
    char *challenge = malloc(challengeSize);
    memset(challenge, 0, challengeSize);
    if (challenge == NULL) {
        return -1;
    }

    // setup user input buffer
    char *userResponse = malloc(challengeSize);
    memset(userResponse, 0, challengeSize);
    if (userResponse == NULL) {
        return -1;
    }

    // prompt user with challenge, get userResponse;
    printf("Challenge: %s\n", getChallenge(challenge, challengeLength));

    char* expectedResponse = rotX(challenge, challenge[0]);
    //printf("I expect a response of: %s\n", expectedResponse);
    fputs("Response: ", stdout);
    fgets(userResponse, challengeLength+1, stdin);

    // verify response is correct length
    if (strlen(userResponse) != challengeLength)  {
        puts("Invalid response. This attempt has been logged.");
        return 1;
    }

    // check user's value
    if (strncmp(expectedResponse, userResponse, strlen(expectedResponse)) == 0) {
        fputs("Welcome to The Nexxus: ", stdout);
        giveFlag();
    } else {
        puts("Incorrect response. This attempt has been logged.");
    }

    return 0;
}
