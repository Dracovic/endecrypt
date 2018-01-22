#include <iostream>
#include <unistd.h>

using namespace std;

int main(int argc, char* argv[]) {
	int endeflag = 0;
	char* fileName;
	char *value = NULL;
	int index;
	int c;

	while ((c = getopt (argc, argv, "e::d::f::a:")) != -1)
		switch (c) {
			case 'e':
				endeflag = -1;
				//cout << "Encrypt" << endl;
				break;
			case 'd':
				endeflag = 1;
				//cout << "Decrypt" << endl;
				break;
			case 'f':
				fileName = argv[optind];
				cout << fileName << endl;
				break;
			case 'a':
				//cout << "This algo -> " << argv[optind-1] << endl;
				break;
			default:
			break;
		}
				
}
