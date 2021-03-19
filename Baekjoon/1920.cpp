#include<iostream>
#include<algorithm>

using namespace std;

int input[100001];

//binary search
void check(int *arr, int n, int temp){
	int i, low = 0, mid, high = n-1, result;
	while(low <= high){
		mid = (low + high)/2;
		
		if(arr[mid] > temp) high = mid-1;
		else if (arr[mid] == temp) {
			result = mid;
			break;
		}
		else low = mid+1;
	}
	if(arr[mid] == temp) printf("1\n");
	else printf("0\n");
}

int main(){
	int n, i, temp;
	scanf("%d", &n);
	
	for(i=0; i<n; i++){
		scanf("%d", &input[i]);
	}
	sort(input, input + n);
	
	int m;
	scanf("%d", &m);
	
	for(i=0; i<m; i++){
		scanf("%d", &temp);
		check(input, n, temp);
	}
	
	return 0;
}
