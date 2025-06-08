
#include <cassert>
#include <vector>
#include <string>


//x pre={
void p(int a[]) {
	// [] must follow the parameter name!
	a[0] = 123;
}
//x }

int main() {

//x description="C-array"

//x pre={
int a[] = {0,1,2,3};
p(a);

// task: what is stored in a?
//x }

//x step={
// arrays are passed by reference,
// not by value
assert((123 == a[0]));
//x }

return 0;
}
