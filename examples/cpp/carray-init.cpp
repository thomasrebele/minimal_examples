
#include <cassert>
#include <vector>
#include <string>

int main() {

//x description="C-array"

//x pre={
// task: define a C-array with int values 1,2,3
// (2 ways)
//x }

//x step={
int a[] = {1,2,3};
// [] MUST follow the variable name!
int b[3] {1,2,3};

// caveat: the array is allocated on the stack
// so it might cause a stack overflow
//x }

//x post={
assert((1 == a[0]));
assert((1 == b[0]));
//x }

return 0;
}
