#include <iostream>
#include <cmath>

using std::cout;
using std::endl;

int main(){
  float y = 1;
  float x = 0;
  float h = 0.001;
  int N = 3/h;
  for(int i = 0; i<N; i++){
    cout << x << " "<< y <<endl;
    x = x+h;
    y = y - y*h;
  }
  return 0;
}
