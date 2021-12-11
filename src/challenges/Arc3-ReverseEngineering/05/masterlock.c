#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void giveFlag() {
    int c;
    FILE *fp;
    fp = fopen("/home/re5/flag.txt", "r");
    if (fp) {
        while ((c = getc(fp)) != EOF)
            putchar(c);
        fclose(fp);
    }
}

int checkRotations(double* rotations) {
    double rotation01 = rotations[0];
    double rotation02 = rotations[1];
    double rotation03 = rotations[2];
    double rotation04 = rotations[3];
    double rotation05 = rotations[4];
    double rotation06 = rotations[5];
    double rotation07 = rotations[6];
    double rotation08 = rotations[7];
    double rotation09 = rotations[8];
    double rotation10 = rotations[9];
    double rotation11 = rotations[10];
    double rotation12 = rotations[11];
    double rotation13 = rotations[12];
    double rotation14 = rotations[13];
    double rotation15 = rotations[14];
    double rotation16 = rotations[15];
    double rotation17 = rotations[16];
    double rotation18 = rotations[17];
    double rotation19 = rotations[18];
    double rotation20 = rotations[19];
    double rotation21 = rotations[20];
    double rotation22 = rotations[21];
    double rotation23 = rotations[22];
    double rotation24 = rotations[23];
    double rotation25 = rotations[24];
    double rotation26 = rotations[25];
    double rotation27 = rotations[26];
    double rotation28 = rotations[27];
    double rotation29 = rotations[28];
    double rotation30 = rotations[29];
    double rotation31 = rotations[30];
    double rotation32 = rotations[31];
    double rotation33 = rotations[32];
    double rotation34 = rotations[33];
    double rotation35 = rotations[34];
    double rotation36 = rotations[35];

    // There is a major issue here that makes this challenge easy to solve.
    // These predicates should be joined by logical ANDs (&&). In its current state
    // you only need get the first two rotations correct (e.g., 1 + 74.5 = 75.4)
    // The people who solved this identified that flaw and used it to solve the
    // challenge without needing an SMT solver. The YouTube video for this challenge:
    // https://www.youtube.com/watch?v=vAwInxB9pEM shows the method for solving this 
    // based on how it -should- have been written. Oops!
    if (rotation01 + rotation02 != 75.4) 
        return 0;
    else if (rotation03 + rotation04 != 92.72)
        return 0;
    else if (rotation05 + rotation06 != 321.58)
        return 0;
    else if (rotation07 + rotation08 != 123.00)
        return 0;
    else if (rotation09 + rotation10 != 33.33)
        return 0;
    else if (rotation11 + rotation12 != 267.91)
        return 0;
    else if (rotation13 + rotation14 != 359.99)
        return 0;
    else if (rotation15 + rotation16 != 80.72)
        return 0;
    else if (rotation17 + rotation18 != 43.87)
        return 0;
    else if (rotation19 + rotation20 != 89.76)
        return 0;
    else if (rotation21 + rotation22 != 13.37)
        return 0;
    else if (rotation23 + rotation24 != 180.18)
        return 0;
    else if (rotation25 + rotation26 != 56.32)
        return 0;
    else if (rotation27 + rotation28 != 80.36)
        return 0;
    else if (rotation29 + rotation30 != 27.11)
        return 0;
    else if (rotation31 + rotation32 != 184.23)
        return 0;
    else if (rotation33 + rotation34 != 277.32)
        return 0;
    else if (rotation35 + rotation36 != 312.21)
        return 0;
    else if (rotation01 + rotation02 != 75.4)
        return 0;
    else if (rotation03 + rotation04 != 92.72)
        return 0;
    else if (rotation05 + rotation06 != 321.58)
        return 0;
    else if (rotation07 + rotation08 != 123.00)
        return 0;
    else if (rotation09 + rotation10 != 33.33)
        return 0;
    else if (rotation11 + rotation12 != 267.91)
        return 0;
    else if (rotation13 + rotation14 != 359.99)
        return 0;
    else if (rotation15 + rotation16 != 80.72)
        return 0;
    else if (rotation17 + rotation18 != 43.87)
        return 0;
    else if (rotation19 + rotation20 != 89.76)
        return 0;
    else if (rotation21 + rotation22 != 13.37)
        return 0;
    else if (rotation23 + rotation24 != 180.18)
        return 0;
    else if (rotation25 + rotation26 != 56.32)
        return 0;
    else if (rotation27 + rotation28 != 80.36)
        return 0;
    else if (rotation29 + rotation30 != 27.11)
        return 0;
    else if (rotation31 + rotation32 != 184.23)
        return 0;
    else if (rotation33 + rotation34 != 277.32)
        return 0;
    else if (rotation35 + rotation36 != 312.21)
        return 0;
    return 1;
}

int main() {
    double rotations[36]; // 36 doubles

    system("clear");
    printf(                                                                     \
    "=======================================================================\n" \
    "                  Nexxus Digital NeXT Lock Interface                   \n" \
    "                  --- 36 Concentric Wafer System ---                   \n" \
    "             \"Completely unbreakable!\" -LockPickingLawyer            \n" \
    "=======================================================================\n" \
    );

    //getchar();
    for (int i = 0; i < 36; i++) {
        printf("[Wafer %d] Degree rotation: ", i+1);
        scanf("%lf", &rotations[i]);
    }

    if (checkRotations(rotations)) {
        puts("\n\nYou hear the loud clunk of 36 large metal objects interacting with each other. A whine of metal and gears spinning faster and faster.\nYou're in. Welcome to the vault.\n");
        giveFlag();
        puts("");
    } else {
        puts("\n\nYou hear the clunk, clunk, clunk of the lock over the audio feed followed by a grinding sound. The lever doesn't budge. You must have gotten a rotation wrong.");
    }

    return 0;
}
