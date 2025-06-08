
#include <cassert>
#include <vector>
#include <string>


//x pre={
int global = 0;

class Foo {
public:
	Foo() {}
	Foo(const Foo& o) { global++; }
};
//x }


int main() {

//x description="class copy constructor"

//x pre={
Foo x;
Foo y = x;
int a = global;

// what is a?
//x }

//x step={
assert((1 == a));
//x }


return 0;
}
