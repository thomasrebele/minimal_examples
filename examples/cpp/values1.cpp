
#include <cassert>
#include <vector>
#include <string>

//x pre={
int f1();
int& f2();
// question: can we the following?
// &f1();
// &f2();
//x }

int main() {

//x description="value categories"

//x step={
// f1 returns an rvalue, int,
// so we cannot take its address
// (the function call f1() is a prvalue)
int* b = &f2();
// f2 returns an lvalue, int&,
// so the function call is itself an lvalue
// and we can take its address

//x }

//x post={
// rough meaning of lvalue / rvalue:
// lvalue: "sth that has an address"
//         (e.g., variables, addresses, pointers)
// rvalue: "everything else"
// (though it's more complicated)
//x }

return 0;
}

int f1() {
	return 0;
}

int foo = 0;
int& f2() {
	return foo;
}
