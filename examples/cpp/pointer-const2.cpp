
#include <cassert>
#include <vector>
#include <string>

int main() {

//x description="pointer and const"

//x pre={
int a = 1;
int b = 2;
int * const p = &a;

// question: is p=&b valid?
//x }

//x step={
// no, p is a const pointer to an int
// so reassignment of p leads to a compile error
//x }

assert((1 == *p));

return 0;
}
