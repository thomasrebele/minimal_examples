
#include <cassert>
#include <vector>
#include <string>
#include <iostream>

//x pre={
int global = 0;

class Foo {
public:
	Foo() {}
	Foo(const Foo& o) { global++; }
};

Foo f(Foo x) {
	return x;
	// the following seems to not
	// call the copy constructor:
	// Foo tmp = x; return x;
}
//x }


int main() {

//x description="class copy constructor"

//x pre={
Foo x;
Foo y = f(x);
int a = global;

// question: what is a?
//x }

//x step={
assert((2 == a));
//x }


return 0;
}
