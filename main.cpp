#include <iostream>
#include <string.h>
#include <stdlib.h>
#include <stdio.h>
#include <unistd.h>

using namespace std;

bool parse_message(char* message);
void scytale(char endeflag, char* message, int diameter = 2);

int main(int argc, char* argv[]) {
	char endeflag = 'e';
	char *fileName = NULL;
	char *message= NULL;
	char *algo = NULL;
	char *parameter = NULL; 
	int index;
	int c;

	opterr = 0;

	while ((c = getopt (argc, argv, "a:e::d::p:f:")) != -1) {
		switch (c) {
			case 'a': // a is the algoritm, choose from list in README.dm or man page
				algo = optarg; //cout << algo << endl;
				break;
			case 'e': // flag to encrypt
				//This is default behaviour //cout << "Encrypt" << endl;
				break;
			case 'd': // flag to decrypt
				endeflag = 'd'; //cout << "Decrypt" << endl;
				break;
			case 'f': // flag input is file
				fileName = optarg; //cout << fileName << endl;
				break;
			case 'p': // additional parameter that the cipher may need to endecode
				parameter = optarg;	//cout << parameter << endl;
				break;
			case '?':
				if(optopt == 'a')
					printf ("Option -%c requires an argument.\n", optopt);
				else if(isprint(optopt))
					printf ("Unknown option '-%c'.\n", optopt);
				else
					printf ("Unknown option character '\\x%x'.\n", optopt);
				return 1;
			default:
				break;
		}
	}
	message = argv[optind];
	//printf("%c\n%s\n%s\n%s\n%s\n", endeflag, fileName, algo, parameter, message);
	if(parse_message(message))
		if(strcmp(algo, "scytale") == 0)
			if(parameter != NULL) {
				scytale(endeflag, message, atoi(parameter));
			}
			else {
				scytale(endeflag, message);
			}
	return 0;
}

bool parse_message(char* message){
	bool parse = true;
	int index = 0;
	while(index < strlen(message)) {
		//printf("%c", message[index]);
		if(isprint(message[index]) == 0)
			parse = false;
		index++;
	}
	//if(parse)
		//printf("Accepted string\n");
	//else
		//printf("Not an accepted string\n");
}

void scytale(char endeflag, char* message, int diameter) {
	int length = ((strlen(message)-1)*diameter)+1; //the length is predictable
	char scymessage[length];
	int c, i = 0, j = 0, k = 0;
	srand(time(NULL));
	//printf("%d\n", length); checks that the legnth is correct
	if(endeflag == 'e'){
		while(i < (strlen(message)-1)) {
			scymessage[j] = message[i];
			while(k < diameter) {
				c = rand () % 57 + 65; c = c + 0; //printf("%c", c);
				scymessage[j] =(char)c;
				printf("%d %d %d %d %c\n", i, j, i+j, k, c);
				j++; k++;
			}
			i++;
			k = 0;
		}
	}
	else if(endeflag == 'd') {
		while(i < (strlen(message)-1)) {
			scymessage[j] = message[i];
			while(k < diameter) {
				//printf("%d %d %d %d %c\n", i, j, k);
				j++; k++;
			}
			i++;
			k = 0;
		}
	}
	printf("\n%s\n", scymessage);
}
