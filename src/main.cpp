#include <iostream>
#include <string.h>
#include <stdlib.h>
#include <stdio.h>
#include <unistd.h>

using namespace std;

bool parse_message(char* message); //just checks if it is "printable" so alphanumeric or punctuation including spaces and newlines
void scytale(char endeflag, char* message, int diameter = 2); //first algorithm, an angled pole of certain number of faces or "diameter"
void atbash(char endeflag, char* message); //from the first, last, second, and second to last letter of the hebrew alphabet, subs first to last letters and so on
void polybius(char endeflag, char* message, const char* square = "3x9");//choose dimensions of a rectangle, use it to map letters to position numbers and return the positions, inverse to decrypt
void rot13(char* message);//ceasar cipher but only for 13
int affine(char endeflag, char* message, const char* parameter = "5,8"); 

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
			if(parameter != NULL)
				scytale(endeflag, message, atoi(parameter));
			else
				scytale(endeflag, message);
		else if (strcmp(algo, "atbash") == 0)
			atbash(endeflag, message);
		else if (strcmp(algo, "polybius") == 0)
			if(parameter != NULL)
				polybius(endeflag, message, parameter);
			else
				polybius(endeflag, message);
		else if (strcmp(algo, "rot13") == 0)
			rot13(message);
		else if (strcmp(algo, "affine") == 0)
			if(parameter != NULL)
				affine(endeflag, message, parameter);
			else
				affine(endeflag, message);
		else
			printf("Don't support that particular Algorithm");
	else
		printf("Message not parsed");
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
	int length;
	int c, i = 0, j = 0, k = 0;
	srand(time(NULL));
	//printf("%d\n", length); checks that the legnth is correct
	if(endeflag == 'e'){
		length = ((strlen(message)-1)*diameter)+1; //the length is predictable
		char enmessage[length];
		while(i < (strlen(message)-1)) {
			enmessage[j] = message[i];
			while(k < diameter) {
				//printf("%d %d %d %d %c\n", i, j, k, c, c);
				j++; k++;
				c = (rand () % 57 + 65);
				if(j < (length -1)) { enmessage[j] =(char)c;}
			}
			i++;
			if(j == (length -1)) { enmessage[j] = message[i];}

			k = 0;
		}
		printf("\n%s\n", enmessage);
	}
	else if(endeflag == 'd') {
		length = ((strlen(message)-1)/diameter)+1;
		char demessage[length];
		while(i < length) {
			demessage[i] = message[j];
			i++;
			j+=diameter;
		}
		demessage[i] = '\n';
		printf("%s", demessage);
	}
}

void atbash(char endeflag, char* message) {
	int i;
	char atmessage[strlen(message)];

	for(i = 0; i < strlen(message); i++) {
		if(!isalpha(message[i])) // its not a letter, stays the same 
			atmessage[i] = message[i];
		else if(!islower(message[i])) //its an upercase letter
			atmessage[i] = (90-(message[i]-65))+0;
		else //its a lowercase letter
			atmessage[i] = (122-(message[i]-97))+0;
	}
		atmessage[i] = '\n';
		printf("%s", atmessage);
}

void polybius(char endeflag, char* message, const char* square) {
	int i, j = 0, itemp;
	int m = square[0]-48;
	int n = square[2]-48;
	if(endeflag == 'e') { //flag for encryption
		int length = (strlen(message)*4)+1;
		char enmessage[length];
		for(i=0;i < strlen(message); i++) {
			//printf("Here --> %d %d\n", i, j);
			if(!isalpha(message[i])) { //it's punctuation
				enmessage[j] = '0';
				enmessage[j+1] = ',';
				enmessage[j+2] = '0';
				enmessage[j+3] = ';';
			} else if(!islower(message[i])) // it's upercase letter
				itemp = message[i] - 64;
			else // it's lowercase letter
				itemp = message[i] - 96;
			if(itemp%n == 0) {
				enmessage[j] = (itemp/n)+48;
				enmessage[j+2] = n+48;
			} else {
				enmessage[j] = (itemp/n)+49;
				enmessage[j+2] = (itemp%n)+48;
			}
				enmessage[j+1] = ',';
				enmessage[j+3] = ';';
			j+=4;
		}
		enmessage[j] = '\0';
		//printf("Here --> %d %d\n", i, j);
		printf("%s\n", enmessage);
	} else { //flag for decryption
		int length = ((strlen(message)-1)/4)+1;
		char demessage[length];
		for(i=0;i < strlen(message); i+=4) {
			demessage[j] = ((((message[i]-48)-1)*n)+(message[i+2]-48))+96;
			j++;
		}
		demessage[j] = '\0';
		printf("%s\n", demessage);
	}
}

void rot13(char* message) {
	int i = 0;
	char endemessage[strlen(message)+1];
	for(; i < strlen(message); i++) {
		if(islower(message[i]))
			if(message[i] < 110)
				endemessage[i] = message[i]+13;
			else {
				endemessage[i] = message[i]-13;
			}
		else if(isupper(message[i]))
			if(message[i] < 78)
				endemessage[i] = message[i]+13;
			else
				endemessage[i] = message[i]-13;
				
		else
			endemessage[i] = message[i];
	}
	endemessage[i] = '\0';
	printf("%s\n", endemessage);
}

int affine(char endeflag, char* message, const char* parameter) {
	int i = 0;
	int a = parameter[0]-48;
	int b = parameter[2]-48;
	if(a == 2 | a==4 | a==6 | a==8 | a==10 | a==12 | a==13 | a==14 | a==16 | a==18 | a==20 | a==22 | a==2) {
		printf("From: \"%s\" %c is not valid\n", parameter, parameter[0]);
		return 0;
	}
	if(endeflag == 'e') {
		char enmessage[strlen(message)+1];
		for(; i < strlen(message); i++) {
			if(islower(message[i]))
				enmessage[i] = (((a*(message[i]-97))+b)%26)+97;
			else if(isupper(message[i]))
				enmessage[i] = (((a*(message[i]-65))+b)%26)+65;
				else
				enmessage[i] = message[i];
		}
		enmessage[i] = '\0';
		printf("%s\n", enmessage);
	}
	else {
		char demessage[strlen(message)+1];
		demessage[i] = '\0';
	}
}
