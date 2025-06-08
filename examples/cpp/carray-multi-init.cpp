
#include <cassert>
#include <vector>
#include <string>

int main() {

//x description="C-array"

//x pre={
// task: define a two dimensional C-array
// with values 0 1 2   3 4 5
//x }

//x step={
int a[2][3] = {{0,1,2},{3,4,5}};

// the first dimension is optional:
int b[][3] = {{0,1,2},{3,4,5}};
//x }

//x post={
assert((2 == a[0][2]));
assert((4 == a[1][1]));
//x }

return 0;
}
