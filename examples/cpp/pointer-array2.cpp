
#include <cassert>
#include <vector>
#include <string>

int main() {

//x description="pointer and array"

//x pre={
int(* a)[];

int x = 1;
int y = 2;
int z[2] = {0,1};

// question: what is a?
//x }

//x step={
// an pointer to an array of length 2
a = &z;
(*a)[0] = 10;
assert((10 == z[0]));
//x }


return 0;
}
