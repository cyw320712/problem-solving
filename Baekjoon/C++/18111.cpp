#include<iostream>

using namespace std;

int main(){
	int n, m, b;
	int tile[500][500] = { -1, };
	cin >> n >> m >> b;
	int height[257] = {0, };
	
	int i, j, k, temp;
	for(i=0; i<n; i++){
		for(j=0; j<m; j++){
			cin >> temp;
			height[temp]++;
			tile[i][j] = temp;
		}
	}
	
	int max = 0, min = 256, minus;
	
	for(i=0; i<=256; i++){
		if(height[i]!=0 && min > i) min = i;
		if(height[i]!=0 && max < i) max  = i;
	}
	int limit;
	int *Tchange = new int[max+1];
	for(i=min; i<=max; i++) Tchange[i] = 0;
  
	for(i=min; i<=max; i++){
		limit = b;
		for(j=0; j<n; j++){
			for(k=0; k<m; k++){
				if(tile[j][k] > i) {
					Tchange[i] += ( tile[j][k] - i ) * 2;	
					limit += (tile[j][k] - i);
				}
				else if(tile[j][k] < i) {
					Tchange[i] += (i - tile[j][k]);
					limit -= (i - tile[j][k]);
				}
			}
		}
		if(limit < 0) Tchange[i] = (1 << 31 -1);
	}
	
	int result = ( 1 << 31 ) - 1, flag;
	for(i=min; i<=max; i++){
		if(result >= Tchange[i]){
			result = Tchange[i];
			flag = i;
		}
	}
	
	cout << result << " " << flag;
	return 0;
}
