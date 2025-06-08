
#include <cassert>
#include <vector>
#include <string>
#include <iostream>

int main() {

//x description="C-array"

//x pre={
int n = 4;
int a[] = {1000,200,30,4};

int sum = 0;
int* p = a;

for(int i=0; i<2; i++) {
	sum += *p++ + *p++;
}

// question: what is sum?
//x }

//x step={
assert((1234 == sum));
//x }

return 0;
}
