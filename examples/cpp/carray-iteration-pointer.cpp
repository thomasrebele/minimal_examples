
#include <cassert>
#include <vector>
#include <string>

int main() {

//x description="C-array"

//x pre={
int n = 3;
int a[] = {1,2,3};

// task: sum all elements of the array
// using the pointer p
int sum = 0;
int* p = a;
//x }

//x step={
for(int i=0; i<n; i++) {
	sum += *p;
	p += 1;

	// could be shortened to:
	//sum += *p++;
}
//x }

//x post={
assert((6 == sum));
//x }

return 0;
}
