
#include <cassert>
#include <vector>
#include <string>

int main() {

//x description="pointer and const"

//x pre={
int a = 1;
int b = 2;
const int * p = &a;

// question: is p=&b valid?
//x }

//x step={
// yes, p is a pointer to a "const" int
p = &b;

// the const means *p=3 is a compile error
//x }


return 0;
}
