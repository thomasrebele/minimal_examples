
#include <cassert>
#include <vector>
#include <string>

int main() {

//x description="pointer"

//x pre={
int a = 1;
int *p = &a;

// task: use the pointer to set a to 2
//x }

//x step={
*p = 2;
//x }

//x post={
assert((2 == a));
//x }

return 0;
}
