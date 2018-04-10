#include <iostream>
#include <cmath>

using std::cout;
using std::endl;

int main(){
  float y = 1;
  float x = 0;
  float z = 0;
  float h = 0.001;
  int N = 10/h;
  for(int i = 0; i<N; i++){
    cout << x << " "<< y << " " << z  <<endl;
    x = x+h;
    y = y + z*h;
    z = z - y*h;
  }
  return 0;
}
