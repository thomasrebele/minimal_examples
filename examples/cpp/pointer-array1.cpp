
#include <cassert>
#include <vector>
#include <string>

int main() {

//x description="pointer and array"

//x pre={
int* a[2];

int x = 1;
int y = 2;
int z[2] = {0,1};

// question: what is a?
//x }

//x step={
// an array of 2 pointers
a[0] = &x;
*(a[0]) = 10;
assert((10 == x));
//x }


return 0;
}
