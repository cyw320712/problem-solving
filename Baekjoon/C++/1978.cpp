#include<iostream>
#include<cmath>

int count=0;

using namespace std;

//check for 2~root(num)
void check(int num){
	int i, max = (int)sqrt(num), flag = 1;
	for(i=2; i<=max; i++){
		if(num%i==0) flag = 0;
	}
	if(flag) count++;
}

int main(){
	int n, i, input;
	scanf("%d", &n);
	
	for(i=0; i<n; i++){
		scanf("%d", &input);
		if(input==1) continue;
		check(input);
	}
	
	printf("%d\n", count);
	return 0;
}
