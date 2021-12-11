#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

const char *boxers[] = {
	"Glass Joe",
	"Von Kaiser",
	"Piston Honda",
	"Don Flamenco",
	"King Hippo",
	"Great Tiger",
	"Bald Bull",
	"Soda Popinski",
	"Mr. Sandman",
	"Super Macho Man",
	"Mike Tyson"
};

const char *combatMoves[] = {
	"throws a right punch!", 
	"throws a left punch!", 
	"comes at you with a right kick! (is that legal?)", 
	"comes at you with a left kick! (there's no way that's legal!)" 
};

int artificialIntelligence() {
	return rand() % 4;
}

int combatAction(char *opponent, unsigned int playerAction) {
	unsigned int boxerAction = artificialIntelligence();
	printf("%s %s\n", opponent, combatMoves[boxerAction]);
	if (playerAction == boxerAction) {
		return 1;
	}
	return 0;
}

int main() {
	char userInput[32] = {0};
	unsigned int choice = 0;
	char boxerSelection = 0;
	char boxer[32] = {0};
	
    srand(time(NULL));

    system("clear");
	printf(                                                                      \
	"========================================================================\n" \
	"                              Punch-Out!!                               \n" \
    "                         ** Insert 25 cents **                          \n" \
	" (The screen flashes and shows Tyson kocking people out left and right) \n" \
	"========================================================================\n" \
	);
	
	printf("Choose your opponent: \n" \
		"0:  %s\n" \
		"1:  %s\n" \
		"2:  %s\n" \
		"3:  %s\n" \
		"4:  %s\n" \
		"5:  %s\n" \
		"6:  %s\n" \
		"7:  %s\n" \
		"8:  %s\n" \
		"9:  %s\n" \
		">> ", boxers[0], 
		boxers[1], boxers[2], boxers[3], 
		boxers[4], boxers[5], boxers[6], 
		boxers[7], boxers[8], boxers[9]);

	boxerSelection = getchar();
	switch(boxerSelection) {
		case '0':
			memcpy(&boxer, boxers[0], strlen(boxers[0]));
			printf("Calling %s to the ring!\n", boxer);
		 	break;
		case '1':
			memcpy(&boxer, boxers[1], strlen(boxers[1]));
			printf("Calling %s to the ring!\n", boxer);
		 	break;
		case '2':
			memcpy(&boxer, boxers[2], strlen(boxers[2]));
			printf("Calling %s to the ring!\n", boxer);
		 	break;
		case '3':
			memcpy(&boxer, boxers[3], strlen(boxers[3]));
			printf("Calling %s to the ring!\n", boxer);
		 	break;
		case '4':
			memcpy(&boxer, boxers[4], strlen(boxers[4]));
			printf("Calling %s to the ring!\n", boxer);
		 	break;
		case '5':
			memcpy(&boxer, boxers[5], strlen(boxers[5]));
			printf("Calling %s to the ring!\n", boxer);
		 	break;
		case '6':
			memcpy(&boxer, boxers[6], strlen(boxers[6]));
			printf("Calling %s to the ring!\n", boxer);
		 	break;
		case '7':
			memcpy(&boxer, boxers[7], strlen(boxers[7]));
			printf("Calling %s to the ring!\n", boxer);
		 	break;
		case '8':
			memcpy(&boxer, boxers[8], strlen(boxers[8]));
			printf("Calling %s to the ring!\n", boxer);
		 	break;
		case '9':
			memcpy(&boxer, boxers[9], strlen(boxers[9]));
			printf("Calling %s to the ring!\n", boxer);
		 	break;
		default:
			memcpy(&boxer, boxers[10], strlen(boxers[10]));
			printf("Sorry that boxer is not available. We're sending you in with Mike Tyson, smarty pants.\n" );
            srand(2021);
            // ========================================
            // DEBUG: Print out the flag for this seed
            // i.e. 2021: HTH{320022313232333130232031}
            // fputs("HTH{", stdout);
            // for (int i = 0; i < 24; i++) {
            //     printf("%d", rand()%4);
            // }
            // puts("}");
            // ========================================

	}

	getchar();
	getchar();

	printf("\nAction list: \n" \
	"0: Dodge and counter right punch.\n" \
	"1: Dodge and counter left punch.\n" \
	"2: Dodge and counter right kick.\n" \
	"3: Dodge and counter left kick.\n\n" \
	"%s's so fast, you need to pick your action before he does!\n", boxer);

	// fight sequence
	for (int i = 0; i < 24; i++) {
		printf("Action: ");
		fgets(userInput, sizeof(userInput), stdin);
		sscanf(userInput, "%u", &choice);
		if (!combatAction(boxer, choice)) {
			// you've lost
			printf("[Attack: %d] %s connects and knocks you down! KO!\n\n", i+1, boxer);
			return 0;
		} else {
			printf("[Attack: %d] You dodge %s's attack and connect with your own! Keep going!\n\n", i+1, boxer);
		}
	}

	// you've won!
	printf("\nRoll credits. You win! Your flag is the winning comabt sequence. i.e. HTH{222332230...}\n\n");

	return 0;
}

