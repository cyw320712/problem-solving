#include<iostream>
#include<string.h>

using namespace std;

int main(){
	string input;
	int flag, i, size;
	
	while(1){
		flag = 1;
		cin >> input;
		size = input.size();
		if(input == "0") break;
		for(i=0; i < size / 2; i++){
			if(input[i] != input[size - i - 1]){
				flag = 0;
			}
		}
		if(flag == 1) cout << "yes" << endl;
		else cout << "no" << endl;
	}
	return 0;
}
