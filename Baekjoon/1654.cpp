#include<iostream>

using namespace std;

bool check(long long *arr, int high, int end, long long var){
	int i, count = 0;
	for(i=0; i<high; i++)
		count += arr[i] / var;
	if(count >= end) return true;
	else return false;
}

int main(){
	int k, n;
	cin >> k >> n;
	
	long long *length = new long long[k];
	int i, count = 0;
	
	long long low = 1, max = 0, mid;
	
	for(i=0; i < k; i++){
		cin >> length[i];
		if(max < length[i]) max = length[i];
	}
	
	long long result = 0;
	
	while(low <= max){
		mid = (low+max)/2;
		
		if(check(length, k, n, mid)){
			if(result < mid) result = mid;
			low = mid + 1;
		}
		else{
			max = mid - 1;
		}
	}
	
	cout << result;
	
	return 0;
}
