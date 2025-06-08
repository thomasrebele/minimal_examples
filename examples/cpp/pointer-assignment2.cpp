
#include <cassert>
#include <vector>
#include <string>

int main() {

//x description="pointer"

//x pre={
int a = 1;
int *p;

// task: prepare the pointer
// so that we can change the value of a
//x }

//x step={
p = &a;
//x }

//x post={
*p = 2;
assert((2 == a));
//x }

return 0;
}
