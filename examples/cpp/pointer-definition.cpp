
#include <cassert>
#include <vector>
#include <string>

int main() {

//x description="pointer"

//x pre={
int a = 1;
// task: define a pointer to a
//x }

//x step={
int *p = &a;
//x }

//x post={
*p = 2;
assert((2 == a));
//x }

return 0;
}
