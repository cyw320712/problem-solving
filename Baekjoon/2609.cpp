#include <iostream>

using namespace std;

int gcd2(int A,int B){
  if (B == 0)
      return A;
  gcd2(B, A%B);
}

int main(){
  int A, B;
  scanf("%d %d", &A, &B);
  int num = gcd2(A, B);
  printf("%d\n%d", num, A*B / num);
  return 0;
}
