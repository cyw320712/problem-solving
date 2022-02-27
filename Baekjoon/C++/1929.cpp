#include<iostream>
#include<cmath>

using namespace std;

void check(int num){
	int i, max = (int)sqrt(num), flag = 1;
    if(num == 1) flag = 0;
	for(i=2; i<=max; i++){
		if(num%i==0) flag = 0;
	}
	if(flag) printf("%d\n", num);
}

int main(){
	int n, m, i;
	scanf("%d %d", &n, &m);
	
	for(i=n; i<=m; i++)
		check(i);
	
	return 0;
}
