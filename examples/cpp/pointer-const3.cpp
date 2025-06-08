
#include <cassert>
#include <vector>
#include <string>

int main() {

//x description="pointer and const"

//x pre={
int a = 1;
// p is a pointer to a "const int"
const int * p = &a;

// question: is the following valid?
// a = 10;
// what would be the value of *p?
//x }

//x step={
// yes, the const in "const int" means just
// unassignable, it may be changed by other means

a = 10;
assert((10 == *p));
//x }


return 0;
}
